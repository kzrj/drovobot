# -*- coding: utf-8 -*-
import json 

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
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from main.models import Customer, Ad
from viber_app.viber_services import SAMPLE_KEYBOARD


viber = Api(BotConfiguration(
    name='drovobot',
    avatar='http://site.com/avatar.jpg',
    auth_token='495624962167d356-894001973007218c-448b90921c20d990'
))


# def 

@csrf_exempt
def viber_view(request):
    
    # if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
    #     return HttpResponse(status=403)

    print(request.body)
    viber_request = viber.parse_request(request.body)
    print(viber_request)



    if isinstance(viber_request, ViberMessageRequest):
        # get or create customer.
        customer, created = Customer.objects.get_or_create(
            viber_id=viber_request.sender.id,
            viber_name=viber_request.sender.name,
            viber_avatar=viber_request.sender.avatar,
            )

        text_message = TextMessage(text="Привет! ты уже зарегистрирован!")
        
        if created:
            text_message = TextMessage(text="Поздравляем ты создан!")

        send_main_keyboard = True
        entering_phone = False

        # check TRACKING DATA
        if viber_request.message.tracking_data == 'TRACKING_CREATE_AD_PHONE':
             Ad.objects.create(owner=customer, active=True, phone=viber_request.message.text)
             send_main_keyboard = True
             viber.send_messages(viber_request.sender.id, [ TextMessage(text="Объявление создано.") ])

        else:
            message = KeyboardMessage(tracking_data='tracking_data', keyboard=SAMPLE_KEYBOARD)

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
                        [ TextMessage(text="Куплю дрова {} {}".format(str(ad), ad.owner.viber_name)) ])

            # create ad
            if viber_request.message.text == 'CREATE_AD':
                ad = Ad.objects.filter(owner=customer).first()
                if ad:
                    if ad.active:
                        ad_message = TextMessage(text="У вас уже есть объявление.")
                        viber.send_messages(viber_request.sender.id, [ ad_message ])
                    else:
                        # create new 
                        viber.send_messages(viber_request.sender.id, [ 
                            TextMessage(text="Введите номер телефона.", tracking_data='TRACKING_CREATE_AD_PHONE') ])
                        send_main_keyboard = False
                        # ad.active = True
                        # ad.save()
                        # ad_message = TextMessage(text="Объявление создано.")
                else:
                    # create new
                    viber.send_messages(viber_request.sender.id, [ 
                            TextMessage(text="Введите номер телефона.", tracking_data='TRACKING_CREATE_AD_PHONE') ])
                    send_main_keyboard = False
                    # Ad.objects.create(owner=customer, active=True)
                    # ad_message = TextMessage(text="Объявление создано.")

                # viber.send_messages(viber_request.sender.id, [ ad_message ])

            # deactivate ad
            if viber_request.message.text == 'DEACTIVATE_AD':
                ad = Ad.objects.filter(owner=customer, active=True).first()
                if ad:
                    ad.active = False
                    ad.save()
                    ad_message = TextMessage(text="Объявление удалено.")
                else:
                    ad_message = TextMessage(text="У вас нет объявлений.")
                viber.send_messages(viber_request.sender.id, [ ad_message ])    

            # send keyboard
            if send_main_keyboard:
                viber.send_messages(viber_request.sender.id, [
                    message
                ])



    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!")
        ])

    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return HttpResponse('Hello, World!')