# -*- coding: utf-8 -*-


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


class ViberView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        print(request)
        print(request.POST)
        print('Oppa')
        return HttpResponse('Hello, World!')