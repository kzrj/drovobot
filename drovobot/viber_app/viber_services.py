# -*- coding: utf-8 -*-
from viberbot.api.messages import (
        TextMessage,
        ContactMessage,
        PictureMessage,
        VideoMessage,
        KeyboardMessage,
        RichMediaMessage
    )


MAIN_MENU_BUTTONS = [
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


MAIN_MENU_KEYBOARD = {
    "Type": "keyboard",
    "Buttons": buttons
    }


def viber_send_main_menu(viber, sender_id):
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
            
    keyboard = {
        "Type": "keyboard",
        "Buttons": buttons
        }

    message = KeyboardMessage(tracking_data='TRACKING_MAIN_MENU', keyboard=keyboard)
    viber.send_messages(sender_id, [ message ])


# def start_conversation_messages():



def viber_send_confirm_phone(viber, sender_id):
    buttons = [
        {
            "Columns": 3,
            "Rows": 2,
            "BgColor": "#e6f5ff",
            "BgMedia": "http://link.to.button.image",
            "BgMediaType": "picture",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "CONFIRM_PHONE_YES",
            "ReplyType": "message",
            "Text": "Да. Все правильно."
        },
        {
            "Columns": 3,
            "Rows": 2,
            "BgColor": "#e6f5ff",
            "BgMedia": "http://link.to.button.image",
            "BgMediaType": "picture",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "CONFIRM_PHONE_NO",
            "ReplyType": "message",
            "Text": "Нет. Нужно исправить."
        }
    ]
            
    keyboard = {
        "Type": "keyboard",
        "Buttons": buttons
        }

    message = KeyboardMessage(tracking_data='CHECK_PHONE', keyboard=keyboard)
    viber.send_messages(sender_id, [ message ])

def viber_send_start(viber, sender_id):
    buttons = [
        {
            "Columns": 6,
            "Rows": 2,
            "BgColor": "#e6f5ff",
            "BgMedia": "http://link.to.button.image",
            "BgMediaType": "picture",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "",
            "ReplyType": "message",
            "Text": "МЕНЮ"
        },
    ]
            
    keyboard = {
        "Type": "keyboard",
        "Buttons": buttons
        }

    message = KeyboardMessage(tracking_data='TRACKING_MAIN_MENU', keyboard=keyboard)
    viber.send_messages(sender_id, [ message ])