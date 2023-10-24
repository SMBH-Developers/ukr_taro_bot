import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from pathlib import Path

from ..constants import DATA_DIR
from ..common import dp
from ..models import db
from ._utils import kb, texts, states


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message):
    await db.registrate_if_not_exists(message.from_user.id)
    await db.update_stage(message.from_user.id, 'stage_1')
    await message.answer(texts.welcome, reply_markup=kb.start)


@dp.message_handler(lambda message: message.text == "🌙Таро розклад загальний стан", state='*')
async def start_choosing_cards(message: types.Message, state: FSMContext):
    await db.update_stage(message.from_user.id, 'stage_2')
    f = types.InputFile(DATA_DIR / 'taro_cards.jpg')
    await message.answer_photo(f, caption=texts.choose_taro_card, reply_markup=kb.choosing_taro_card)


@dp.message_handler(lambda message: message.text in kb.taro_cards_title, state='*')
async def choose_card(message: types.Message, state: FSMContext):
    await message.answer('🪄Обробляю інформацію...', reply_markup=types.ReplyKeyboardRemove())
    choose = int(message.text.split()[-1]) - 1
    asyncio.create_task(send_late_taro_analyze(message, choose))


def get_taro_card(user_choice: int):
    if len(texts.taro_cards) - 1 < user_choice:
        user_choice = -1
    photo: Path = texts.taro_cards[user_choice]['photo']
    text: str = texts.taro_cards[user_choice]['text']
    return photo, text


async def send_late_taro_analyze(message: types.Message, user_choose: int):
    await asyncio.sleep(4.5)
    if len(texts.taro_cards) - 1 < user_choose:
        user_choose = -1
    photo, text = get_taro_card(user_choose)
    await db.update_stage(message.from_user.id, 'stage_3')
    file = types.InputFile(photo)
    await message.answer_photo(file, caption=text, reply_markup=kb.to_autoanswer, parse_mode='html')
