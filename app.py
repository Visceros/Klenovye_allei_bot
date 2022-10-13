import logging
import ssl

from aiogram import Dispatcher, Bot
from aiogram.types import InputFile
from aiogram.utils import executor
from aiogram.utils.executor import start_webhook

from config import Config
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from controller import MainController


async def on_startup(app):
    config = Config()
    bot = Bot(token=config.bot_token)
    await bot.set_webhook(config.webhook_url,
                          certificate=InputFile(config.webhook_cert_file) if config.webhook_cert_file != "" else None)


def main():
    logging.basicConfig(level=logging.INFO)

    config = Config()
    storage = MongoStorage(uri=config.mongo_url, db_name=config.fsm_mongo_database)

    bot = Bot(token=config.bot_token)
    dp = Dispatcher(bot, storage=storage)

    MainController(bot=bot, presentation_copy_chat=config.presentation_copy_chat,
                   presentation_copy_message=config.presentation_copy_message, tour_link=config.tour_link,
                   reply_chat=config.reply_chat, photo_copy_chat=config.photo_copy_chat,
                   support_chat_link=config.support_chat_link,
                   photo_copy_message=config.photo_copy_message).register(dp)

    if config.webhook_enabled:
        ssl_context = None
        if config.webhook_cert_file != "":
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            ssl_context.load_cert_chain(config.webhook_cert_file, config.webhook_private_key_file)
        start_webhook(
            webhook_path="/",
            dispatcher=dp,
            skip_updates=False,
            host=config.webhook_app_host,
            port=config.webhook_app_port,
            ssl_context=ssl_context,
            on_startup=on_startup
        )
    else:
        executor.start_polling(dp, skip_updates=False)


if __name__ == '__main__':
    main()
