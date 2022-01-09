import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, Command
from aiogram.dispatcher.filters.state import StatesGroup, State

from bot.texts import Texts, YesNoButtons, ThemesButtonsTexts

API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class MainStates(StatesGroup):
    start = State()
    themes = State()
    finish = State()


@dp.message_handler(Command('start'), state=[None, MainStates.finish])
async def start(message: types.Message):
    await MainStates.start.set()
    await message.answer(Texts.start, reply_markup=YesNoButtons.buttons())


@dp.message_handler(Text(equals=YesNoButtons.NO.value, ignore_case=True),
                    state=MainStates.start)
async def start_no(message: types.Message, state: FSMContext):
    await message.answer(Texts.happy_for_you)
    await MainStates.finish.set()


@dp.message_handler(Text(equals=YesNoButtons.YES.value, ignore_case=True),
                    state=MainStates.start)
async def start_yes(message: types.Message, state: FSMContext):
    await MainStates.next()
    await message.answer(Texts.themes, reply_markup=ThemesButtonsTexts.buttons())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
