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

viber = Api(BotConfiguration(
    name='drovobot',
    avatar='http://site.com/avatar.jpg',
    auth_token='495624962167d356-894001973007218c-448b90921c20d990'
))

class ViberView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        print(request)
        print(request.POST)
        print('Oppa')
        return HttpResponse('Hello, World!')

@csrf_exempt
def viber_view(request):
    print(request)
    print(request.POST)
    print(request.GET)
    print(request.headers)
    print(request.body)
    print(request.content_type)
    print(request.COOKIES)
    print(request.META)
    print('Oppa')
    data_json = json.dumps(request.COOKIES)
    # if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
    #     return Response(status=403)

    viber_request = viber.parse_request(data_json)


    if isinstance(viber_request, ViberMessageRequest):
        text_message = TextMessage(text="Ты заебал! Звони сюда!")
        # message = viber_request.message
        
        contact = Contact(name="Bato Rinchinov",
            phone_number="+79913693190",
            avatar="http://link.to.avatar")
        contact_message = ContactMessage(contact=contact)

        viber.send_messages(viber_request.sender.id, [
            text_message, contact_message
        ])

    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!")
        ])

    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return HttpResponse('Hello, World!')