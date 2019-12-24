# -*- coding: utf-8 -*-
from viberbot.api.messages import (
        TextMessage,
        ContactMessage,
        PictureMessage,
        VideoMessage,
        KeyboardMessage,
        RichMediaMessage
    )

# MAIN_MENU
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


# SAMPLE RICH_MEDIA
SAMPLE_RICH_MEDIA = {
  "Buttons": [
    {
        "Columns":6,
        "Rows":4,
        "Text":"<font color=#323232><b>Дровобот!</b></font> \
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
        "ActionType": "reply",
        "ActionBody": "START",
        "Text": "<font color=#323232><b>СТАРТ!</b></font>",
        "TextSize":"large",
        "TextVAlign":"middle",
        "TextHAlign":"middle",
    }
  ]
}


# CREATE AD
# CREATE AD LOCATION
CREATE_AD_LOCATION_BUTTONS = [
   {
        "Columns": 2,
        "Rows": 2,
        "Text": "<br><font color=#494E67><b>Левый берег</b></font>",
        "TextSize": "regular",
        "TextHAlign": "center",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "Левый берег",
        "BgColor": "#f7bb3f",
        "Image": "https://s18.postimg.org/9tncn0r85/sushi.png"
    }, {
        "Columns": 2,
        "Rows": 2,
        "Text": "<br><font color=#494E67><b>Советский район</b></font>",
        "TextSize": "regular",
        "TextHAlign": "center",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "Советский район",
        "BgColor": "#7eceea",
        "Image": "https://s18.postimg.org/ntpef5syd/french.png"
    }, {
        "Columns": 2,
        "Rows": 2,
        "Text": "<br><font color=#494E67><b>Железнодорожный район</b></font>",
        "TextSize": "regular",
        "TextHAlign": "center",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "Железнодорожный район",
        "BgColor": "#f6f7f9",
        "Image": "https://s18.postimg.org/t8y4g4kid/mexican.png"
    }, {
        "Columns": 2,
        "Rows": 2,
        "Text": "<br><font color=#494E67><b>Октябрьский район</b></font>",
        "TextSize": "regular",
        "TextHAlign": "center",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "Октябрьский район",
        "BgColor": "#dd8157",
        "Image": "https://s18.postimg.org/x41iip3o5/itallian.png"
    }, {
        "Columns": 2,
        "Rows": 2,
        "Text": "<br><font color=#494E67><b>Вахмистрово</b></font>",
        "TextSize": "regular",
        "TextHAlign": "center",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "Вахмистрово",
        "BgColor": "#f6f7f9",
        "Image": "https://s18.postimg.org/wq06j3jkl/indi.png"
    },
]

CREATE_AD_LOCATION_KEYBOARD = {
    "Type": "keyboard",
    "Buttons": CREATE_AD_LOCATION_BUTTONS,
    "InputFieldState": 'hidden'
    }

# CREATE AD AMOUNT
CREATE_AD_AMOUNT_BUTTONS = [
    {
        "Columns": 2,
        "Rows": 2,
        "Text": "<br><font color=#494E67><b>от 2 до 4 т.р.</b></font>",
        "TextSize": "regular",
        "TextHAlign": "center",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "от 2 до 4 т.р.",
        "BgColor": "#f7bb3f",
        "Image": "https://s18.postimg.org/9tncn0r85/sushi.png"
    }, {
        "Columns": 2,
        "Rows": 2,
        "Text": "<br><font color=#494E67><b>от 4 до 6 т.р.</b></font>",
        "TextSize": "regular",
        "TextHAlign": "center",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "от 4 до 6 т.р.",
        "BgColor": "#7eceea",
        "Image": "https://s18.postimg.org/ntpef5syd/french.png"
    }, {
        "Columns": 2,
        "Rows": 2,
        "Text": "<br><font color=#494E67><b>от 6 до 8 т.р.</b></font>",
        "TextSize": "regular",
        "TextHAlign": "center",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "от 6 до 8 т.р.",
        "BgColor": "#f6f7f9",
        "Image": "https://s18.postimg.org/t8y4g4kid/mexican.png"
    }, {
        "Columns": 2,
        "Rows": 2,
        "Text": "<br><font color=#494E67><b>от 8 т.р. и выше</b></font>",
        "TextSize": "regular",
        "TextHAlign": "center",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "от 8 т.р. и выше",
        "BgColor": "#dd8157",
        "Image": "https://s18.postimg.org/x41iip3o5/itallian.png"
    }
]

CREATE_AD_AMOUNT_KEYBOARD = {
    "Type": "keyboard",
    "Buttons": CREATE_AD_AMOUNT_BUTTONS,
    "InputFieldState": 'hidden'
    }


# XZ
SAMPLE_RICH_MEDIA2 = {
  "BgColor": "#69C48A",
  "Buttons": [
    {
        "Columns":6,
        "Rows":2,
        "Text":"<font color=#323232><b>\
            Кнопка</b></font>\
            <font color=#777777><br>Share phone </font><font color=#6fc133>$17.99</font>",
        "ActionType":"share-phone",
        "TextSize":"medium",
        "TextVAlign":"middle",
        "TextHAlign":"left"
    },
    {
        "Columns": 6,
        "Rows": 2,
        "BgLoop": "true",
        "ActionType": "reply",
        "Silent": "true",
        "ActionBody": "Welcome",
        "Text": "<b>СТАРТ!</b>",
        "TextOpacity": 10,
        "TextSize":"large",
        "TextVAlign":"middle",
        "TextHAlign":"middle",
    }
  ]
}

SAMPLE_ALT_TEXT = "upgrade now!"

# CHANGE_AD
CHANGE_AD_BUTTONS = [
   {
        "Columns": 3,
        "Rows": 2,
        "Text": "<br><font color=#494E67><b>Изменить</b></font>",
        "TextSize": "regular",
        "TextHAlign": "center",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "CHANGE_AD",
        "BgColor": "#f7bb3f",
        "Image": "https://s18.postimg.org/9tncn0r85/sushi.png"
    }, {
        "Columns": 3,
        "Rows": 2,
        "Text": "<br><font color=#494E67><b>Меню</b></font>",
        "TextSize": "regular",
        "TextHAlign": "center",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "MAIN_MENU",
        "BgColor": "#7eceea",
        "Image": "https://s18.postimg.org/ntpef5syd/french.png"
    }, 
]

CHANGE_AD_KEYBOARD = {
    "Type": "keyboard",
    "Buttons": CHANGE_AD_BUTTONS,
    "InputFieldState": 'hidden'
    }


# ESCAPE
ESCAPE_BUTTONS = [
   {
        "Columns": 3,
        "Rows": 2,
        "Text": "<br><font color=#494E67><b>Отменить и вернуться в меню</b></font>",
        "TextSize": "regular",
        "TextHAlign": "center",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "MAIN_MENU",
        "BgColor": "#f7bb3f",
        "Image": "https://s18.postimg.org/9tncn0r85/sushi.png"
    }
]

ESCAPE_AD_KEYBOARD = {
    "Type": "keyboard",
    "Buttons": ESCAPE_BUTTONS,
    "InputFieldState": 'regular'
    }

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