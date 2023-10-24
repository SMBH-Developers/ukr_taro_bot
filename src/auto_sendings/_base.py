import asyncio

from aiogram import types, exceptions

from sqlalchemy import select
from sqlalchemy import ColumnElement, Update

from loguru import logger

from ..common import bot
from ..models import db, async_session, User


class BaseSending:

    is_active: bool = False
    text: str = None
    kb: types.InlineKeyboardMarkup = None
    to_log: str = None

    def _update_query_on_success(self, user: int) -> Update:
        raise NotImplementedError

    def requirements(self) -> tuple[ColumnElement]:
        raise NotImplementedError

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
        if self.text is None or self.kb is None or self.requirements is None or self.to_log is None:
            raise ValueError("Sending hasn't text or kb")
        return True

    async def start(self):
        self._verify()
        while True:
            async with async_session() as session:
                users = (await session.execute(select(User.id).where(*self.requirements()))).scalars().all()

            for user in users:
                if await self._try_to_send(user):
                    logger.success(f'{self.to_log} {user=}')
                    async with async_session() as session:
                        await session.execute(self._update_query_on_success(user))
                        await session.commit()
            await asyncio.sleep(5)
