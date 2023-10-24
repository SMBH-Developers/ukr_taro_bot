from aiogram import types
from aiogram.dispatcher import FSMContext

from ...common import dp
from .. import db
from .._utils import kb
from .._utils.excel import StagesExcelStat


@dp.callback_query_handler(lambda call: call.data == 'admin?stages', state='*')
async def get_stages_menu(call: types.CallbackQuery):
    def _ls_stages_to_str(ls_):
        return '\n'.join([f'{stage} - {count}' for stage, count in ls_])

    stages = [_ls_stages_to_str(stages_ls) for stages_ls in await db.get_stages_stat()]
    all_stages, yesterday_stages, today_stages = stages

    text = f'Всего:\n{all_stages}\n---\n' \
           f'За вчера:\n{yesterday_stages}\n---\n' \
           f'За сегодня:\n{today_stages}'

    await call.message.edit_text(text, reply_markup=kb.stages_kb)


@dp.callback_query_handler(lambda call: call.data == 'stages?excel', state='*')
async def get_users_excel(call: types.CallbackQuery):
    stat = await db.get_stages_excel()
    excel_path = StagesExcelStat().create(stat)
    f = types.InputFile(excel_path)
    await call.message.answer_document(f)
    await call.message.answer("Готово!", reply_markup=kb.back_to_menu)
