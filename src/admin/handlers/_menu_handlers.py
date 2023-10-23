from aiogram import types
from aiogram.dispatcher import FSMContext

from ...common import dp, ADMIN_IDS
from .._utils import kb


@dp.message_handler(lambda message: message.from_user.id in ADMIN_IDS, commands=['admin'], state='*')
async def answer_admin_menu(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Выберите:", reply_markup=kb.menu)


@dp.callback_query_handler(lambda call: call.data == 'admin?back', state='*')
async def back_to_admin_menu(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_text("Выберите:", reply_markup=kb.menu)
