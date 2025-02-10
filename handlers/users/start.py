from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from keyboards.default.somsalar import menu_kb
from loader import dp





@dp.message_handler(CommandStart(),state='*')
async def bot_start(message: types.Message):
    with open('images/beta.jpg', "rb") as photo:
        await message.answer_photo(
            photo=photo,
            caption="""
<b>ASSALOMU ALEYKUM</b>

Siz <b>"Tilla Somsa"</b> rasmiy botiga xush kelibsiz!
Bot beta rejimda ishlamoqda. Talab va takliflar uchun: @tillasomsa_admin
            """,
            reply_markup=menu_kb,
            parse_mode="HTML"
        )




#Menyu
#Mening Buyurtmalarim
#Savatcha
#Sozlamalar