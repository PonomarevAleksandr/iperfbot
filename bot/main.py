"""Bot configuration"""
import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from src.handlers import router as main_router
from src.utils.config import settings



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    """
    Bot, middlewares, session configuration
    :return: None
    """
    session = AiohttpSession()
    bot = Bot(
        token=settings.BOT_TOKEN,
        session=session,
        default=DefaultBotProperties(parse_mode="HTML")
    )

    dp = Dispatcher()

    dp.include_router(main_router)

    try:
        await dp.start_polling(bot)
    except ValueError as e:
        logger.error("ValueError occurred: %s", e)
    except KeyError as e:
        logger.error("KeyError occurred: %s", e)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
