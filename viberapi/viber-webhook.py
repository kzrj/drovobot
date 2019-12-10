from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages import VideoMessage
from viberbot.api.messages.text_message import TextMessage


from viberbot.api.viber_requests import ViberConversationStartedRequest
from viberbot.api.viber_requests import ViberFailedRequest
from viberbot.api.viber_requests import ViberMessageRequest
from viberbot.api.viber_requests import ViberSubscribedRequest
from viberbot.api.viber_requests import ViberUnsubscribedRequest


# 4aa8cfe4f5a7d667-98afa3e99e58bfe6-9698235b67973816
# 4aa8cfe4f5a7d667-98afa3e99e58bfe6-9698235b67973816
# 495624962167d356-894001973007218c-448b90921c20d990
viber = Api(BotConfiguration(
    name='drovobot',
    avatar='http://site.com/avatar.jpg',
    auth_token='495624962167d356-894001973007218c-448b90921c20d990'
))

viber.set_webhook('https://neo-boudoir.ru:443/')
