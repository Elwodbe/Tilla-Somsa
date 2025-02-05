from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

choiser = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➖", callback_data="minus"),
            InlineKeyboardButton(text="0", callback_data="natija"),
            InlineKeyboardButton(text="➕", callback_data="pilus"),
        ],
        [
            InlineKeyboardButton(text="Savatchaga qo`shish📥", callback_data="buy"),

        ]
    ]
)