# -*- coding: utf-8 -*-

from viberbot.api.messages import (
        TextMessage,
        ContactMessage,
        PictureMessage,
        VideoMessage,
        KeyboardMessage,
        RichMediaMessage
    )
from viberbot.api.messages.data_types.contact import Contact


buttons = [
    {
        "Columns": 2,
        "Rows": 2,
        "BgColor": "#e6f5ff",
        "BgMedia": "http://link.to.button.image",
        "BgMediaType": "picture",
        "BgLoop": True,
        "ActionType": "reply",
        "ActionBody": "CREATE_AD",
        "ReplyType": "message",
        "Text": "Купить дрова!"
    },
    {
        "Columns": 2,
        "Rows": 2,
        "BgColor": "#e6f5ff",
        "BgMedia": "http://link.to.button.image",
        "BgMediaType": "picture",
        "BgLoop": True,
        "ActionType": "reply",
        "ActionBody": "DEACTIVATE_AD",
        "ReplyType": "message",
        "Text": "Уже купил. Убрать объявление."
    },
    {
        "Columns": 2,
        "Rows": 2,
        "BgColor": "#e6f5ff",
        "BgMedia": "http://link.to.button.image",
        "BgMediaType": "picture",
        "BgLoop": True,
        "ActionType": "reply",
        "ActionBody": "SHOW_ADS",
        "ReplyType": "message",
        "Text": "Я продаю дрова. Посмотреть объявления."
    }
]
        
SAMPLE_KEYBOARD = {
    "Type": "keyboard",
    "Buttons": buttons
    }


# rich media
form = {
            "Type": "rich_media",
            "ButtonsGroupColumns": 6,
            "ButtonsGroupRows": 6,
            "BgColor": "#E6E6FA",
            "Buttons": [
                {
                "Columns": 6,
                "Rows": 5,
                "BgColor": "#FFFFFF",
                "Text": '<font color="#545265">В любой момент можете задать интересующий Вас вопрос, просто написав его в этот чат. Чтобы еще раз вызвать это меню просто напишите в чат "меню" или нажмите 👇</font>',
                "TextSize": "medium",
                "TextVAlign": "middle",
                "TextHAlign": "middle",
                "ActionType": None,
                "ActionBody": "",
                "Silent": True
                },
                {
                "Columns": 6,
                "Rows": 1,
                "BgColor": "#E6E6FA",
                "Text": '<font color="#545265"><b>Меню</b></font>',
                "TextSize": "medium",
                "TextVAlign": "middle",
                "TextHAlign": "middle",
                "ActionType": 'reply',
                "ActionBody": "Меню",
                }
            ]
        }
# viber.send_messages(viber_request.sender.id, [
#     RichMediaMessage(rich_media=form, min_api_version=2, keyboard=SAMPLE_KEYBOARD)
#     ])

def viber_send_main_menu(viber, sender_id):
	message = KeyboardMessage(tracking_data='TRACKING_MAIN_MENU', keyboard=SAMPLE_KEYBOARD)
	viber.send_messages(sender_id, [ message ])