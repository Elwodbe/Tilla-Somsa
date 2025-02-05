from loader import dp
from aiogram import types
from keyboards.default.somsalar import menyu_somsa
from states.tilla_state import Xonachalar
#import state FSMCONTEXT
from aiogram.dispatcher import FSMContext
from utils.db_api.database import search_somsa,update_busket,update_busket1,update_product_status


@dp.message_handler(text='🍽 Menyu')
async def menyu_uchun(message:types.Message):
    await message.answer("Somsalardan birini tanlang",reply_markup=menyu_somsa)
    await Xonachalar.choise_somsa.set()

from keyboards.inline.all_inline import choiser
kichkina_savatcha = {}

@dp.message_handler(state=Xonachalar.choise_somsa)
async def tanlangan_somsa(message: types.Message,state :FSMContext):
    somsa_nomi = message.text
     
    qandaydir = await search_somsa(somsa_nomi=somsa_nomi)
    product_id = qandaydir[0]
    kichkina_savatcha[message.from_user.id] = product_id

    await message.answer_photo(photo=open(f'images/{qandaydir[-1]}','rb'),caption=f"""
<b>{qandaydir[1]}</b>
💸<b>Narx</b>:<code>{qandaydir[2]}</code>
""",reply_markup=choiser)












from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


@dp.callback_query_handler(text='pilus',state="*")
async def pilus_button(call:types.CallbackQuery):
    data = await update_busket(user_id=call.message.chat.id,product_id=kichkina_savatcha.get(call.message.chat.id),count_product=1,status='disabled')
    yangi_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➖", callback_data="minus"),
            InlineKeyboardButton(text=f"{data}", callback_data="natija"),
            InlineKeyboardButton(text="➕", callback_data="pilus"),
        ],
        [
            InlineKeyboardButton(text="Savatchaga qo`shish📥", callback_data="buy"),

        ]
    ]

)
    await call.message.edit_reply_markup(yangi_button)


@dp.callback_query_handler(text='minus',state="*")
async def pilus_button(call:types.CallbackQuery):
    data = await update_busket1(user_id=call.message.chat.id,product_id=kichkina_savatcha.get(call.message.chat.id),count_product=1,status='disabled')
    yangi_button1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➖", callback_data="minus"),
            InlineKeyboardButton(text=f"{data}", callback_data="natija"),
            InlineKeyboardButton(text="➕", callback_data="pilus"),
        ],
        [
            InlineKeyboardButton(text="Savatchaga qo`shish📥", callback_data="buy"),

        ]
    ]

)

    await call.message.edit_reply_markup(yangi_button1)
    
@dp.callback_query_handler(text='buy',state="*")
async def savtchaga_qoshish(call:types.CallbackQuery):
    print(call.message.chat.id)
    data = await update_product_status(user_id=call.message.chat.id,product_id=kichkina_savatcha.get(call.message.chat.id))
    if data == True:
        await call.answer("Savatchaga qo`shildi",show_alert=True)
    else:
        await call.answer("Qandaydir xatolik yuz berdi")