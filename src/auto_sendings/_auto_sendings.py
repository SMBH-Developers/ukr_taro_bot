from aiogram import types
from aiogram.utils import markdown

from sqlalchemy import Update, TIMESTAMP
from sqlalchemy import func, cast
from sqlalchemy.sql.expression import select, update

from loguru import logger
from datetime import datetime, timedelta
from ._base import BaseSending
from ..models import async_session, User

# For future

__all__ = ["Sending2Hours", "Sending24Hours"]


class Sending2Hours(BaseSending):
    is_active = True
    text = f'🙌Дорогі мої, я поспішаю повідомити про те, що залишилося всього 6 безкоштовних місць на розклад карт таро\n\n💌Не упустіть свій шанс і напишіть: «карта долі» в особисті повідомлення — @tarolog_anna_pier 👈\n\n📝За допомогою безкоштовного розкладу на таро ми зможемо виявити актуальні життєві проблеми, з якими ви зіткнетеся в цьому місяці, і знайти правильний шлях для їх вирішення'
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("🌟Змінити життя", url='https://t.me/tarolog_anna_pier '))

    to_log: str = '2h_sending'

    def requirements(self):
        return ((User.registration_date + timedelta(hours=2)) < datetime.now(),
                User.got_2h_autosending.is_(None), User.stage != 'stage_4', User.status == 'alive')

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
    text = f'Добрий день, зараз не самий  простий час для нас усіх, це період труднощів на шляху, не упустіть можливість зробити індивідуальний розклад таро та отримати особисті рекомендації від ведучого таролога України (див. куди ставимо)\n\nУ розкладі Ви дізнаєтеся про те, як можна вирішити поточні життєві проблеми і уникнути подальших невдач в майбутньому місяці.\n\nДля отримання необхідно написати «карту успіху» в особистих повідомленнях — @tarolog_anna_pier 👈\n\n🔮Кількість безкоштовних місць обмежено!'
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("🔆Безкоштовний таророзклад", url='https://t.me/tarolog_anna_pier '))
    to_log: str = '24h_sending'

    def requirements(self):
        return ((User.got_2h_autosending + timedelta(hours=22)) < datetime.now(),
                User.got_24h_autosending.is_(None), User.stage != 'stage_4', User.status == 'alive')

    def _update_query_on_success(self, user: int) -> Update:
        return update(User).where(User.id == user).values(got_24h_autosending=func.now())

    async def start(self):
        try:
            if self._verify():
                await super().start()
        except ValueError as ex:
            logger.info(f'Sending24Hours {ex.args}')
