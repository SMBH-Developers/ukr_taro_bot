import json

from itertools import islice
from aiogram import types


def _get_titles_from_kb(kb: types.ReplyKeyboardMarkup):
    json_kb = json.loads(kb.as_json())['keyboard']
    titles = []
    for row in json_kb:
        for btn in row:
            titles.append(btn['text'])
    return titles


def _chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())


def __init_choosing_taro_card():
    for tuple_of_indexes in _chunk(range(1, 7), 2):  # Карта Таро
        btns = [types.KeyboardButton(f'Карта Таро {index}') for index in tuple_of_indexes]
        choosing_taro_card.add(*btns)


start = types.ReplyKeyboardMarkup(resize_keyboard=True)
start.add(types.KeyboardButton('🌙Таро расклад общее состояние'))


# Клавиатура при выборе таро карты
choosing_taro_card = types.ReplyKeyboardMarkup(resize_keyboard=True)
__init_choosing_taro_card()
taro_cards_title = _get_titles_from_kb(choosing_taro_card)


to_autoanswer = types.InlineKeyboardMarkup()
to_autoanswer.add(types.InlineKeyboardButton('🔮 Получить расклад', url='https://t.me/taro_anna_pie'))
