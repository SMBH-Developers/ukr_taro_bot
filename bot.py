import asyncio

from aiogram import executor

from src.common import dp
from src.amqp import amqp_queue_task
from src.auto_sendings import Sending2Hours, Sending24Hours
from src.handlers import _handlers
from src.admin.handlers import _menu_handlers, _users_handlers, _stages_handlers


async def on_startup(_):
    asyncio.create_task(amqp_queue_task())
    asyncio.create_task(Sending2Hours().start())
    asyncio.create_task(Sending24Hours().start())


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
