from loader import dp
from aiogram import types
from keyboards.default.somsalar import menyu_somsa
from states.tilla_state import Xonachalar
#import state FSMCONTEXT
from aiogram.dispatcher import FSMContext
from utils.db_api.database import search_somsa


@dp.message_handler(text='🍽 Menyu')
async def menyu_uchun(message:types.Message):
    await message.answer("Somsalardan birini tanlang",reply_markup=menyu_somsa)
    await Xonachalar.choise_somsa.set()


@dp.message_handler(state=Xonachalar.choise_somsa)
async def tanlangan_somsa(message: types.Message,state :FSMContext):
    somsa_nomi = message.text
    qandaydir = await search_somsa(somsa_nomi=somsa_nomi)
    await message.answer_photo(photo=open(f'images/{qandaydir[-1]}','rb'),caption=f"""
<b>{qandaydir[1]}</b>
💸<b>Narx</b>:<code>{qandaydir[2]}</code>
""")
    print(qandaydir)
