# -*- coding: utf-8 -*-
import json 

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages import (
        TextMessage,
        ContactMessage,
        PictureMessage,
        VideoMessage
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

from main.models import Customer


viber = Api(BotConfiguration(
    name='drovobot',
    avatar='http://site.com/avatar.jpg',
    auth_token='495624962167d356-894001973007218c-448b90921c20d990'
))


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
        
        SAMPLE_KEYBOARD = {
            "Type": "keyboard",
            "Buttons": [
                {
                "Columns": 3,
                "Rows": 2,
                "BgColor": "#e6f5ff",
                "BgMedia": "http://link.to.button.image",
                "BgMediaType": "picture",
                "BgLoop": True,
                "ActionType": "reply",
                "ActionBody": "This will be sent to your bot in a callback",
                "ReplyType": "message",
                "Text": "Push me!"
                }
                ]
            }

        message = KeyboardMessage(tracking_data='tracking_data', keyboard=SAMPLE_KEYBOARD)
        # text_message = TextMessage(text="Ты заебал! Звони сюда!")
        # message = viber_request.message
        
        # contact = Contact(name="Bato Rinchinov",
        #     phone_number="+79913693190",
        #     avatar="http://link.to.avatar")
        # contact_message = ContactMessage(contact=contact)

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