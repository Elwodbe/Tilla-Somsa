from loader import dp
from aiogram import types
from keyboards.default.fikrlar import fikrla_py
from states.tilla_state import Xonachalar
#import state FSMCONTEXT
from aiogram.dispatcher import FSMContext

@dp.message_handler(text='✍️ Fikr bildirish')
async def fikr_uchun(message:types.Message):
    await message.answer("""✅ Tilla somsani tanlaganingiz uchun rahmat.
                            Agar Siz bizning hizmatlarimiz sifatini yaxshilashga yordam bersangiz, bundan benihoya xursand bo'lamiz.
                            Buning uchun 5 ballik tizim asosida baholang""", reply_markup=fikrla_py)
    
@dp.message_handler(text="Hammasi yoqdi ♥️")
async def hammasi_yoqdi(message: types.Message):
    await message.answer("O’z fikr va mulohazalaringizni yozma yoki audio xabar shaklida qoldiring.")
    
