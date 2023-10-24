from aiogram import types
from aiogram.utils import markdown

from sqlalchemy import Update, TIMESTAMP
from sqlalchemy import func, cast
from sqlalchemy.sql.expression import select, update

from loguru import logger

from ._base import BaseSending
from ..models import async_session, User

# For future

__all__ = ["Sending2Hours", "Sending24Hours"]


class Sending2Hours(BaseSending):
    is_active = True
    text = f"🙌Дорогие мои, я спешу сообщить о том, что осталось всего {markdown.hbold('6 бесплатных мест на расклад карт таро')}\n\n💌Не упустите свой шанс и напишите: «карта судьбы» в личные сообщения — @taro_anna_pie...👈\n\n📝С помощью бесплатного  расклада на таро мы сможем выявить актуальные жизненные проблемы с которыми столкнетесь в этом месяце и найти правильные пути для их решения"
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("🌟 Изменить жизнь", url='https://t.me/taro_anna_pie '))
    requirements = (func.trunc(func.date_part('hour', cast(func.now(), TIMESTAMP), cast(User.registration_date, TIMESTAMP))) >= 2,
                    User.got_2h_autosending.is_(None), User.stage != 'stage_4')
    to_log: str = '2h_sending'

    def _update_query_on_success(self, user: int) -> Update:
        return update(User).where(User.id == user).values(got_2h_autosending=func.now())

    async def start(self):
        try:
            if self._verify():
                return await super().start()
        except ValueError as ex:
            logger.info(f'Sending2Hours {ex.args}')


class Sending24Hours(BaseSending):
    is_active = True
    text = f'Добрый день, сейчас не самое простое время для нас всех, это период трудностей на пути, не упустите возможность сделать индивидуальный расклад таро и получить личные рекомендации от ведущего таролога СНГ/Украины (смотря куда ставим)\n\nВ  раскладе  Вы узнаете о том, как можно решить текущие жизненные проблемы и избежать дальнейших неудач  грядущем месяце.\n\nДля получения необходимо написать «карта удачи» в личные сообщения  — @taro_anna_pie 👈\n\n{markdown.hbold("🔮Количество бесплатных мест ограничено!")}'
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("🔆Бесплатный таро расклад", url='https://t.me/taro_anna_pie '))
    requirements = (func.trunc(func.date_part('hour', func.now(), User.got_2h_autosending)) >= 22,
                    User.got_24h_autosending.is_(None), User.stage != 'stage_4')
    to_log: str = '24h_sending'

    def _update_query_on_success(self, user: int) -> Update:
        return update(User).where(User.id == user).values(got_24h_autosending=func.now())

    async def start(self):
        try:
            if self._verify():
                await super().start()
        except ValueError as ex:
            logger.info(f'Sending24Hours {ex.args}')
