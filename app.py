import logging
import os

from aiogram import Bot, Dispatcher, executor

from bot.dispatchers import echo

API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(echo)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
