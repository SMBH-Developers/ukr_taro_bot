import asyncio

from aiogram import types, exceptions
from loguru import logger

from abc import ABC, abstractmethod

from ..common import bot
from ..models import db


class BaseSending(ABC):

    text: str = None
    kb: types.InlineKeyboardMarkup = None

    async def _try_to_send(self, user: int) -> bool:
        """Returns True on success sending, other way False"""
        try:
            await bot.send_message(user, text=self.text, reply_markup=self.kb, parse_mode='html')
            await asyncio.sleep(0.2)
        except (exceptions.BotBlocked, exceptions.UserDeactivated):
            logger.info(f'ID: {user}. DELETED')
            await db.delete_user(user)
        except Exception as ex:
            logger.error(f'got error: {ex}')
        else:
            return True
        return False

    def _verify(self):
        if self.text is None or self.kb is None:
            raise ValueError("Sending hasn't text or kb")

    @abstractmethod
    async def start(self):
        raise NotImplementedError
