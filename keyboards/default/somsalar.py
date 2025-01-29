from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menyu_somsa = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("QOY GO'SHTI"),
            KeyboardButton("MOL GOSHTLI KATTA"),
        ],
        [
            KeyboardButton("MOL GO'SHTLI KICHIK"),
            KeyboardButton("TOVUQ SIRLI"),
        ],
        [
            KeyboardButton("AVASHNOY"),
            KeyboardButton("KARTOSHKALI"),

        ],
        [
        KeyboardButton("KO'KATLI"),
            KeyboardButton("QOVOQLI")
        ]
    ],
    resize_keyboard=True
)