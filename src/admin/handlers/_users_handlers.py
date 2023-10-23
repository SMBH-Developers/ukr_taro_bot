from aiogram import types
from aiogram.dispatcher import FSMContext

from ...common import dp
from .. import db
from .._utils import kb
from .._utils.excel import UsersExcelStat


@dp.callback_query_handler(lambda call: call.data == 'admin?users', state='*')
async def get_users_menu(call: types.CallbackQuery):
    all_users, yesterday_users, today_users = await db.get_users_stat()
    text = f'Пользователей всего: {all_users}\n' \
           f'Пользователей за вчера: {yesterday_users}\n' \
           f'Пользователей за сегодня: {today_users}'
    await call.message.edit_text(text, reply_markup=kb.users_kb)


@dp.callback_query_handler(lambda call: call.data == 'users?excel', state='*')
async def get_users_excel(call: types.CallbackQuery):
    stat = await db.get_users_excel()
    excel_path = UsersExcelStat().create(stat)
    f = types.InputFile(excel_path)
    await call.message.answer_document(f)
    await call.message.answer("Готово!", reply_markup=kb.back_to_menu)
