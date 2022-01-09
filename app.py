import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

from texts import Texts, YesNoButtons, ThemesButtonsTexts, NightmaresButtonsTexts

API_TOKEN = os.getenv('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class MainStates(StatesGroup):
    start = State()
    themes = State()
    finish = State()


class OftenWakeUpStates(StatesGroup):
    first_assumption = State()
    second_assumption = State()
    third_assumption = State()
    finish = State()


class NightmaresStates(StatesGroup):
    start = State()
    first_problem = State()
    second_problem = State()
    finish = State()


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message):
    await MainStates.start.set()
    await message.answer(Texts.start, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.NO.value, ignore_case=True),
    state=MainStates.start
)
async def start_no(message: types.Message, state: FSMContext):
    await message.answer(Texts.happy_for_you)
    await MainStates.finish.set()


@dp.message_handler(
    Text(equals=YesNoButtons.YES.value, ignore_case=True),
    state=[
        MainStates.start,
        OftenWakeUpStates.finish,
        NightmaresStates.finish
    ]
)
async def start_yes(message: types.Message, state: FSMContext):
    await MainStates.themes.set()
    await message.answer(Texts.themes, reply_markup=ThemesButtonsTexts.buttons())


@dp.message_handler(
    Text(equals=ThemesButtonsTexts.OFTEN_WAKE_UP.value, ignore_case=True),
    state=MainStates.themes
)
async def often_wake_up_first_assumption(message: types.Message, state: FSMContext):
    await OftenWakeUpStates.first_assumption.set()
    await message.answer(Texts.often_wake_up_first_assumption,
                         reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.YES.value, ignore_case=True),
    state=OftenWakeUpStates.first_assumption
)
async def often_wake_up_first_assumption_yes(message: types.Message, state: FSMContext):
    await OftenWakeUpStates.finish.set()
    await message.answer(Texts.often_wake_up_first_assumption_yes)
    await message.answer(Texts.anything_else, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.NO.value, ignore_case=True),
    state=OftenWakeUpStates.first_assumption
)
async def often_wake_up_first_assumption_no(message: types.Message, state: FSMContext):
    await OftenWakeUpStates.next()
    await message.answer(Texts.often_wake_up_second_assumption,
                         reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.YES.value, ignore_case=True),
    state=OftenWakeUpStates.second_assumption
)
async def often_wake_up_second_assumption_yes(message: types.Message,
                                              state: FSMContext):
    await OftenWakeUpStates.finish.set()
    await message.answer(Texts.often_wake_up_second_assumption_yes)
    await message.answer(Texts.anything_else, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.NO.value, ignore_case=True),
    state=OftenWakeUpStates.second_assumption
)
async def often_wake_up_second_assumption_no(message: types.Message, state: FSMContext):
    await OftenWakeUpStates.next()
    await message.answer(Texts.often_wake_up_third_assumption,
                         reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.YES.value, ignore_case=True),
    state=OftenWakeUpStates.third_assumption
)
async def often_wake_up_third_assumption_yes(message: types.Message, state: FSMContext):
    await OftenWakeUpStates.next()
    await message.answer(Texts.often_wake_up_third_assumption_yes)
    await message.answer(Texts.anything_else, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.NO.value, ignore_case=True),
    state=OftenWakeUpStates.third_assumption
)
async def often_wake_up_third_assumption_no(message: types.Message, state: FSMContext):
    await OftenWakeUpStates.next()
    await message.answer(Texts.often_wake_up_third_assumption_no)
    await message.answer(Texts.anything_else, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.NO.value, ignore_case=True),
    state=[
        OftenWakeUpStates.finish,
        NightmaresStates.finish
    ]
)
async def finish(message: types.Message, state: FSMContext):
    await MainStates.finish.set()
    await message.answer(Texts.finish)


@dp.message_handler(
    Text(equals=ThemesButtonsTexts.NIGHTMARES.value, ignore_case=True),
    state=MainStates.themes
)
async def nightmares_start(message: types.Message, state: FSMContext):
    await NightmaresStates.start.set()
    await message.answer(Texts.nightmares_start,
                         reply_markup=NightmaresButtonsTexts.buttons())


@dp.message_handler(
    Text(equals=NightmaresButtonsTexts.FIRST_PROBLEM.value, ignore_case=True),
    state=NightmaresStates.start
)
@dp.message_handler(
    Text(equals=YesNoButtons.YES.value, ignore_case=True),
    state=NightmaresStates.second_problem
)
async def nightmares_first_problem(message: types.Message, state: FSMContext):
    await NightmaresStates.first_problem.set()
    await message.answer(Texts.nightmares_first_problem)
    await message.answer(Texts.nightmares_look_second_problem,
                         reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.NO.value, ignore_case=True),
    state=NightmaresStates.first_problem
)
async def nightmares_first_problem_no(message: types.Message, state: FSMContext):
    await NightmaresStates.finish.set()
    await message.answer(Texts.nightmares_finish)
    await message.answer(Texts.anything_else, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=NightmaresButtonsTexts.SECOND_PROBLEM.value, ignore_case=True),
    state=NightmaresStates.start
)
@dp.message_handler(
    Text(equals=YesNoButtons.YES.value, ignore_case=True),
    state=NightmaresStates.first_problem
)
async def nightmares_second_problem(message: types.Message, state: FSMContext):
    await NightmaresStates.second_problem.set()
    await message.answer(Texts.nightmares_second_problem)
    await message.answer(Texts.nightmares_look_first_problem,
                         reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.NO.value, ignore_case=True),
    state=NightmaresStates.second_problem
)
async def nightmares_second_problem_no(message: types.Message, state: FSMContext):
    await NightmaresStates.finish.set()
    await message.answer(Texts.nightmares_finish)
    await message.answer(Texts.anything_else, reply_markup=YesNoButtons.buttons())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
