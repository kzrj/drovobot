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
    "Buttons": MAIN_MENU_BUTTONS,
    "InputFieldState": 'hidden'
    }



SAMPLE_RICH_MEDIA = {
  "BgColor": "#69C48A",
  "Buttons": [
    {
        "Columns":6,
        "Rows":2,
        "Text":"<font color=#323232><b>\
            Дровобот!</b></font>\
            <font color=#777777><br>Sound Intone </font><font color=#6fc133>$17.99</font>",
        "ActionType":"none",
        "ActionBody":"https://www.google.com",
        "TextSize":"medium",
        "TextVAlign":"middle",
        "TextHAlign":"left"
    },
    {
        "Columns": 6,
        "Rows": 2,
        "BgColor": "#CB6F1F",
        "BgLoop": "true",
        "ActionType": "reply",
        "Silent": "true",
        "ActionBody": "Welcome",
        "Text": "<b>СТАРТ!</b> button",
        "TextOpacity": 10,
        "TextSize":"large",
        "TextVAlign":"middle",
        "TextHAlign":"middle",
    }
  ]
}

SAMPLE_RICH_MEDIA2 = {
  "BgColor": "#69C48A",
  "Buttons": [
    {
        "Columns":6,
        "Rows":2,
        "Text":"<font color=#323232><b>\
            Дровобот!</b></font>\
            <font color=#777777><br>Sound Intone </font><font color=#6fc133>$17.99</font>",
        "ActionType":"share-phone",
        "ActionBody":"https://www.google.com",
        "TextSize":"medium",
        "TextVAlign":"middle",
        "TextHAlign":"left"
    },
    {
        "Columns": 6,
        "Rows": 2,
        "BgColor": "#CB6F1F",
        "BgLoop": "true",
        "ActionType": "reply",
        "Silent": "true",
        "ActionBody": "Welcome",
        "Text": "<b>СТАРТ!</b> button",
        "TextOpacity": 10,
        "TextSize":"large",
        "TextVAlign":"middle",
        "TextHAlign":"middle",
    }
  ]
}

SAMPLE_ALT_TEXT = "upgrade now!"

# message = RichMediaMessage(rich_media=SAMPLE_RICH_MEDIA, alt_text=SAMPLE_ALT_TEXT)


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