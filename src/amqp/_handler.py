import asyncio
import aio_pika
import logging
import os

from typing import Callable
from aio_pika import logger as aio_pika_logger
from loguru import logger

from ._schemas import UpdateStageQuery
from ..common import settings
from ..models import db

aio_pika_logger.setLevel(logging.ERROR)


async def update_stage(message: aio_pika.abc.AbstractIncomingMessage):
    with logger.catch(level='EXCEPTION'):
        async with message.process():
            query = UpdateStageQuery.from_json(message.body.decode())
            await db.update_stage(query.user_id, query.new_stage)


async def amqp_queue_task() -> None:
    url = os.getenv('KARINA_BOTS_AMQP_URL')
    if not url:
        raise ValueError("No variable $KARINA_BOTS_AMQP_URL")

    connection = await aio_pika.connect(url)

    queue_name = f"update_stage_$_{settings.uniq_title}"
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=25)
    queue = await channel.declare_queue(queue_name, durable=True)
    # await queue.purge()

    await queue.consume(update_stage)

    try:
        # Wait until terminate
        while True:
            await asyncio.sleep(5)
    finally:
        await connection.close()
