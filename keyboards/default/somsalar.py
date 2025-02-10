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
        ],
        [
            KeyboardButton('🔙 Orqaga')
        ]
    ],
    resize_keyboard=True
)


menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🍽 Menyu")],
        [KeyboardButton('🔁Buyurtmalar tarixi'), KeyboardButton("Savatcha")],
        [KeyboardButton("ℹ️ Ma'lumot"), KeyboardButton("☎️ Biz bilan aloqa")],
        [KeyboardButton("✍️ Fikr bildirish"),KeyboardButton("⚙️Sozlamalar")]
    ],
    resize_keyboard=True
)