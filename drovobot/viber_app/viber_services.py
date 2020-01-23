# -*- coding: utf-8 -*-
from viberbot.api.messages import (
        TextMessage,
        ContactMessage,
        PictureMessage,
        VideoMessage,
        KeyboardMessage,
        RichMediaMessage
    )

# HELP TEXT

HELP_TEXT = 'Чтобы купить дрова - нажмите "Купить дрова!" и создайте объявление. \n Его видно 24 часа. Или вы можете удалить его нажав "Удалить объявление". \n Чтобы продать дрова - нажмите "Посмотреть объявления".'

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
            "Text": "Я продаю дрова. Посмотреть объявления. Получать новые объявления."
        },
        {
            "Columns": 2,
            "Rows": 2,
            "BgColor": "#e6f5ff",
            "BgMedia": "http://link.to.button.image",
            "BgMediaType": "picture",
            "BgLoop": True,
            "ActionType": "reply",
            "ActionBody": "UNSUBSCRIBE",
            "ReplyType": "message",
            "Text": "Отписаться от объявлений."
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
        "Text":'<font color=#323232><b>Дровобот!</b></font> \
            <font color=#777777><br>Вас приветствует ДровоБот! :) \
            Этот бот поможет вам купить и продать дрова! \
            Нажмите</font> <font color=#6fc133>"СТАРТ!"</font>',
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
    }, {
        "Columns": 2,
        "Rows": 2,
        "Text": "<br><font color=#494E67><b>МЕНЮ</b></font>",
        "TextSize": "regular",
        "TextHAlign": "center",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "MAIN_MENU",
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
    }, {
        "Columns": 2,
        "Rows": 2,
        "Text": "<br><font color=#494E67><b>МЕНЮ</b></font>",
        "TextSize": "regular",
        "TextHAlign": "center",
        "TextVAlign": "middle",
        "ActionType": "reply",
        "ActionBody": "MAIN_MENU",
        "BgColor": "#dd8157",
        "Image": "https://s18.postimg.org/x41iip3o5/itallian.png"
    }
]

CREATE_AD_AMOUNT_KEYBOARD = {
    "Type": "keyboard",
    "Buttons": CREATE_AD_AMOUNT_BUTTONS,
    "InputFieldState": 'hidden'
    }
    

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