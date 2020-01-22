# -*- coding: utf-8 -*-
import json
import datetime

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages import (
        TextMessage,
        ContactMessage,
        PictureMessage,
        VideoMessage,
        KeyboardMessage,
        RichMediaMessage
    )
from viberbot.api.messages.data_types.contact import Contact

from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

import main.tasks as celery_tasks
from main.models import Customer, Ad
from viber_app.viber_services import (
    MAIN_MENU_BUTTONS, MAIN_MENU_KEYBOARD, CREATE_AD_LOCATION_KEYBOARD, CREATE_AD_AMOUNT_KEYBOARD,
    CHANGE_AD_KEYBOARD, ESCAPE_AD_KEYBOARD, SAMPLE_RICH_MEDIA, HELP_TEXT
    )


viber = Api(BotConfiguration(
    name='drovobot',
    avatar='http://site.com/avatar.jpg',
    auth_token='495624962167d356-894001973007218c-448b90921c20d990'
))

COUNTDOWN = 86400
# 86400 = 24h

sellers = Customer.objects.filter(phone=None)


@csrf_exempt
def viber_view(request):
    viber_request = viber.parse_request(request.body)
    if isinstance(viber_request, ViberMessageRequest):
        # get or create customer.
        customer, created = Customer.objects.get_or_create(
            viber_id=viber_request.sender.id,
            viber_name=viber_request.sender.name,
            viber_avatar=viber_request.sender.avatar,
            )

        if customer.banned:
            viber.send_messages(viber_request.sender.id, [ 
                TextMessage(text="Заблокировано(",
                     tracking_data='BANNED'),
                      ])
            return HttpResponse('Banned!')

        if viber_request.message.tracking_data == 'TRACKING_CREATE_AD_LOCATION':
            if viber_request.message.text == 'CHANGE_AD':
                viber.send_messages(viber_request.sender.id, [ 
                        TextMessage(text="Укажите в какой район привезти дрова:",
                             tracking_data='TRACKING_CREATE_AD_LOCATION'),
                        KeyboardMessage(tracking_data='TRACKING_CREATE_AD_LOCATION',
                         keyboard=CREATE_AD_LOCATION_KEYBOARD,  min_api_version=6), 
                              ])
            elif viber_request.message.text == 'MAIN_MENU':
                viber.send_messages(viber_request.sender.id, [ 
                    KeyboardMessage(tracking_data='TRACKING_MAIN_MENU', keyboard=MAIN_MENU_KEYBOARD, 
                        min_api_version=6) ])
            else:
                ad = customer.get_ad
                if ad.validate_location(viber_request.message.text):
                    ad.location = viber_request.message.text
                    ad.save()

                    # send choose amount
                    viber.send_messages(viber_request.sender.id, [
                        TextMessage(text="Укажите на какую сумму:",
                                     tracking_data='TRACKING_CREATE_AD_AMOUNT'),
                        KeyboardMessage(tracking_data='TRACKING_CREATE_AD_AMOUNT',
                                     keyboard=CREATE_AD_AMOUNT_KEYBOARD, min_api_version=6),        
                    ])
                else:
                    # repeat location choose
                    viber.send_messages(viber_request.sender.id, [ 
                        TextMessage(text="Укажите в какой район привезти дрова:",
                             tracking_data='TRACKING_CREATE_AD_LOCATION'),
                        KeyboardMessage(tracking_data='TRACKING_CREATE_AD_LOCATION',
                         keyboard=CREATE_AD_LOCATION_KEYBOARD,  min_api_version=6), 
                              ])

        elif viber_request.message.tracking_data == 'TRACKING_CREATE_AD_AMOUNT':
            ad = customer.get_ad

            # check amount
            if ad.validate_amount(viber_request.message.text):
                ad.amount = viber_request.message.text
                ad.save()
               
                # send input phone or main_menu
                if customer.phone:
                    customer.get_ad.activate
                    celery_tasks.deactivate_ad.apply_async(
                        args=[customer.get_ad.pk],
                        countdown=COUNTDOWN
                    )

                    # SEND AD TO SELLERS
                    for seller in sellers:
                        try:
                            viber.send_messages(seller.viber_id, [
                                TextMessage(text="Новое объявление:"),
                                TextMessage(text=str(customer.get_ad)),
                                KeyboardMessage(tracking_data='TRACKING_MAIN_MENU', keyboard=MAIN_MENU_KEYBOARD,
                     min_api_version=6)])
                        except:
                            pass

                    viber.send_messages(viber_request.sender.id, [
                        TextMessage(text="Объявление изменено и опубликовано. Оно удалится через 24 часа.",
                             tracking_data='TRACKING_MAIN_MENU'),
                        TextMessage(text=customer.get_ad.to_text, tracking_data='TRACKING_MAIN_MENU'),
                        KeyboardMessage(tracking_data='TRACKING_MAIN_MENU', keyboard=MAIN_MENU_KEYBOARD,
                             min_api_version=6),        
                    ])
                else:
                    viber.send_messages(viber_request.sender.id, [ 
                                    TextMessage(text="Введите номер телефона в формате 8хххххххххх. \
                                        Проверьте правильность. Изменить телефон нельзя!",
                                     tracking_data='TRACKING_CREATE_AD_PHONE'),
                                    KeyboardMessage(tracking_data='TRACKING_CREATE_AD_PHONE', 
                                        keyboard=ESCAPE_AD_KEYBOARD,
                                        min_api_version=6)
                                      ])

            elif viber_request.message.text == 'MAIN_MENU':
                viber.send_messages(viber_request.sender.id, [ 
                    TextMessage(text=HELP_TEXT),
                    KeyboardMessage(tracking_data='TRACKING_MAIN_MENU', keyboard=MAIN_MENU_KEYBOARD, 
                        min_api_version=6) ])

        elif viber_request.message.tracking_data == 'TRACKING_CREATE_AD_PHONE':
            if viber_request.message.text == 'MAIN_MENU':
                viber.send_messages(viber_request.sender.id, [
                    TextMessage(text=HELP_TEXT),
                    KeyboardMessage(tracking_data='TRACKING_MAIN_MENU', keyboard=MAIN_MENU_KEYBOARD,
                     min_api_version=6),
                ])

            # Check phone
            elif customer.validate_phone(viber_request.message.text):
                customer.phone = viber_request.message.text
                customer.save()
                customer.get_ad.activate
                celery_tasks.deactivate_ad.apply_async(
                    args=[customer.get_ad.pk],
                    countdown=COUNTDOWN
                )

                # SEND AD TO SELLERS
                for seller in sellers:
                    try:
                        viber.send_messages(seller.viber_id, [
                            TextMessage(text="Новое объявление:"),
                            TextMessage(text=str(customer.get_ad)),
                            KeyboardMessage(tracking_data='TRACKING_MAIN_MENU', keyboard=MAIN_MENU_KEYBOARD,
                     min_api_version=6)])
                    except:
                        pass

                # send choose amount
                viber.send_messages(viber_request.sender.id, [
                    TextMessage(text='''Объявление создано. Нужно нажать кнопку "Удалить объявление" для удаления объявления или оно автоматически удалится через 24 часа . Ваше объявление:''',
                     tracking_data='TRACKING_MAIN_MENU'),
                    TextMessage(text=customer.get_ad.to_text, tracking_data='TRACKING_MAIN_MENU'),
                    KeyboardMessage(tracking_data='TRACKING_MAIN_MENU', keyboard=MAIN_MENU_KEYBOARD,
                         min_api_version=6),        
                ])
            else:
                viber.send_messages(viber_request.sender.id, [ 
                                TextMessage(text='''Неверный номер. Введите номер телефона в формате 8хххххххххх. 11 цифр. Проверьте правильность. Изменить телефон нельзя!''',
                                 tracking_data='TRACKING_CREATE_AD_PHONE'),
                                KeyboardMessage(tracking_data='TRACKING_CREATE_AD_PHONE', 
                                    keyboard=ESCAPE_AD_KEYBOARD,
                                    min_api_version=6) ])

        elif viber_request.message.tracking_data == 'TRACKING_MAIN_MENU':
            # show ads
            if viber_request.message.text == 'SHOW_ADS':
                ads = Ad.objects.filter(active=True)
                viber.send_messages(viber_request.sender.id, 
                        [ TextMessage(text='Все объявления:') ])
                if ads.count() == 0:
                    viber.send_messages(viber_request.sender.id, 
                        [ TextMessage(text='нет обьявлений') ])
                for ad in ads:
                    viber.send_messages(viber_request.sender.id, 
                        [ TextMessage(text=ad.to_text) ])
                # send main menu
                viber.send_messages(viber_request.sender.id, [
                    KeyboardMessage(tracking_data='TRACKING_MAIN_MENU', keyboard=MAIN_MENU_KEYBOARD,
                     min_api_version=6),
                ])

            # create ad
            if viber_request.message.text == 'CREATE_AD':
                ad = customer.get_ad
                if ad:
                    if ad.active:
                        viber.send_messages(viber_request.sender.id, [ 
                            TextMessage(text="У вас уже есть объявление. Можно изменить район и сумму."),
                            KeyboardMessage(tracking_data='TRACKING_CREATE_AD_LOCATION',
                             keyboard=CHANGE_AD_KEYBOARD,  min_api_version=6), 
                        ])
                    else:
                        # continue creating or change
                        viber.send_messages(viber_request.sender.id, [ 
                            TextMessage(text="Укажите в какой район привезти дрова:",
                                 tracking_data='TRACKING_CREATE_AD_LOCATION'),
                            KeyboardMessage(tracking_data='TRACKING_CREATE_AD_LOCATION',
                             keyboard=CREATE_AD_LOCATION_KEYBOARD,  min_api_version=6), 
                                  ])

                else:
                    # create new
                    Ad.objects.create(owner=customer, active=False)

                    viber.send_messages(viber_request.sender.id, [ 
                        TextMessage(text="Укажите в какой район привезти дрова:",
                             tracking_data='TRACKING_CREATE_AD_LOCATION'),
                        KeyboardMessage(tracking_data='TRACKING_CREATE_AD_LOCATION',
                         keyboard=CREATE_AD_LOCATION_KEYBOARD,  min_api_version=6), 
                              ])

            # deactivate ad
            if viber_request.message.text == 'DEACTIVATE_AD':
                # CHANGE OR DEACTIVATE
                ad = Ad.objects.filter(owner=customer, active=True).first()
                if ad:
                    ad.active = False
                    ad.save()
                    ad_message = TextMessage(text="Объявление удалено.")
                else:
                    ad_message = TextMessage(text="У вас нет объявлений.")
                viber.send_messages(viber_request.sender.id, [ ad_message,
                    KeyboardMessage(tracking_data='TRACKING_MAIN_MENU', keyboard=MAIN_MENU_KEYBOARD, 
                        min_api_version=6) ])

        else:
            # send main menu
            viber.send_messages(viber_request.sender.id, [
                TextMessage(text=HELP_TEXT),
                KeyboardMessage(tracking_data='TRACKING_MAIN_MENU', keyboard=MAIN_MENU_KEYBOARD, 
                    min_api_version=6),        
            ])

    elif isinstance(viber_request, ViberConversationStartedRequest):
        # viber_send_main_menu(viber, viber_request.user.id)
        viber.send_messages(viber_request.user.id, [
            RichMediaMessage(rich_media=SAMPLE_RICH_MEDIA, alt_text='ALT TEXT!', min_api_version=3)
        ])

    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.user.id, [
            TextMessage(text="thanks for subscribing!")
        ])

    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return HttpResponse('viber client only')