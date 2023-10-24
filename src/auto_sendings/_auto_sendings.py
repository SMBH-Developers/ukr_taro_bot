from aiogram import types
from aiogram.utils import markdown

from sqlalchemy import func
from sqlalchemy.sql.expression import select, update

from loguru import logger

from ._base import BaseSending
from ..models import async_session, User

# For future

__all__ = ["Sending2Hours", "Sending24Hours"]


class Sending2Hours(BaseSending):
    is_active = False
    text = None
    kb = None
    requirements = None
    to_log = None
    update_on_success = None

    async def start(self):
        try:
            if self._verify():
                await super().start()
        except ValueError as ex:
            logger.info(f'Sending2Hours {ex.args}')


class Sending24Hours(BaseSending):
    is_active = False
    text = None
    kb = None
    requirements = None
    to_log = None
    update_on_success = None

    async def start(self):
        try:
            if self._verify():
                await super().start()
        except ValueError as ex:
            logger.info(f'Sending24Hours {ex.args}')
