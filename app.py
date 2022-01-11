import logging
import os
import re
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

from texts import Texts, YesNoButtons, ThemesButtonsTexts, NightmaresButtonsTexts, \
    SleepinessButtonsTexts

TIME_RE = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)$')

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


class CantFallAsleepStates(StatesGroup):
    first_advice = State()
    is_useful_first = State()
    second_advice = State()
    is_useful_second = State()
    third_advice = State()
    is_useful_third = State()
    fourth_advice = State()
    is_useful_fourth = State()
    fifth_advice = State()
    finish = State()


class SleepinessStates(StatesGroup):
    start = State()
    first_advice = State()
    second_advice = State()
    finish = State()


class SleepAnalysisStates(StatesGroup):
    input_first_time = State()
    input_second_time = State()
    third_step = State()
    finish = State()


class SleepParalysisStates(StatesGroup):
    finish = State()


class CantSleepStates(StatesGroup):
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
        SleepAnalysisStates.finish,
        OftenWakeUpStates.finish,
        NightmaresStates.finish,
        SleepParalysisStates.finish,
        CantSleepStates.finish,
        SleepinessStates.finish,
        CantFallAsleepStates.finish,
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
        NightmaresStates.finish,
        SleepParalysisStates.finish,
        CantSleepStates.finish,
        SleepinessStates.finish,
        CantFallAsleepStates.finish,
        SleepAnalysisStates.finish
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
    state=[NightmaresStates.first_problem, NightmaresStates.second_problem]
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
    Text(equals=ThemesButtonsTexts.SLEEP_PARALYSIS.value, ignore_case=True),
    state=MainStates.themes
)
async def sleep_paralysis_advices(message: types.Message, state: FSMContext):
    await SleepParalysisStates.finish.set()
    await message.answer(Texts.sleep_paralysis_advices)
    await message.answer(Texts.anything_else, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=ThemesButtonsTexts.CANT_SLEEP.value, ignore_case=True),
    state=MainStates.themes
)
async def cant_sleep_advices(message: types.Message, state: FSMContext):
    await CantSleepStates.finish.set()
    await message.answer(Texts.cant_sleep_advices)
    await message.answer(Texts.anything_else, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=ThemesButtonsTexts.SLEEPINESS.value, ignore_case=True),
    state=MainStates.themes
)
async def sleepiness_start(message: types.Message, state: FSMContext):
    await SleepinessStates.start.set()
    await message.answer(Texts.sleepiness_start,
                         reply_markup=SleepinessButtonsTexts.buttons())


@dp.message_handler(
    Text(equals=SleepinessButtonsTexts.FIRST_ADVICE.value, ignore_case=True),
    state=SleepinessStates.start
)
@dp.message_handler(
    Text(equals=YesNoButtons.YES.value, ignore_case=True),
    state=SleepinessStates.second_advice
)
async def sleepiness_first_advice(message: types.Message, state: FSMContext):
    await SleepinessStates.first_advice.set()
    await message.answer(Texts.sleepiness_first_advice)
    await message.answer(Texts.sleepiness_look_second_advice,
                         reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=SleepinessButtonsTexts.SECOND_ADVICE.value, ignore_case=True),
    state=SleepinessStates.start
)
@dp.message_handler(
    Text(equals=YesNoButtons.YES.value, ignore_case=True),
    state=SleepinessStates.first_advice
)
async def sleepiness_second_advice(message: types.Message, state: FSMContext):
    await SleepinessStates.second_advice.set()
    await message.answer(Texts.sleepiness_second_advice)
    await message.answer(Texts.sleepiness_look_first_advice,
                         reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.NO.value, ignore_case=True),
    state=[
        SleepinessStates.first_advice,
        SleepinessStates.second_advice
    ]
)
async def sleepiness_finish(message: types.Message, state: FSMContext):
    await SleepinessStates.finish.set()
    await message.answer(Texts.sleepiness_finish)
    await message.answer(Texts.anything_else, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=ThemesButtonsTexts.CANT_FALL_ASLEEP.value, ignore_case=True),
    state=MainStates.themes
)
async def cant_fall_asleep_first_advice(message: types.Message, state: FSMContext):
    await CantFallAsleepStates.first_advice.set()
    await message.answer(Texts.cant_fall_asleep_first_advice)
    await message.answer(Texts.is_useful, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.NO.value, ignore_case=True),
    state=[
        CantFallAsleepStates.is_useful_first,
        CantFallAsleepStates.is_useful_second,
        CantFallAsleepStates.is_useful_third,
        CantFallAsleepStates.is_useful_fourth,
        CantFallAsleepStates.fifth_advice
    ]
)
async def cant_fall_asleep_early_finish(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == 'CantFallAsleepStates:fifth_advice':
        await message.answer(Texts.cant_fall_asleep_finish)
    else:
        await message.answer(Texts.cant_fall_asleep_early_finish)
    await CantFallAsleepStates.finish.set()
    await message.answer(Texts.anything_else, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.YES.value, ignore_case=True),
    state=[
        CantFallAsleepStates.first_advice,
        CantFallAsleepStates.second_advice,
        CantFallAsleepStates.third_advice,
        CantFallAsleepStates.fourth_advice,
        CantFallAsleepStates.fifth_advice,
    ]
)
async def cant_fall_asleep_is_useful(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == 'CantFallAsleepStates:fifth_advice':
        await CantFallAsleepStates.next()
        await message.answer(Texts.cant_fall_asleep_early_finish)
        await message.answer(Texts.anything_else, reply_markup=YesNoButtons.buttons())
    else:
        await CantFallAsleepStates.next()
        await message.answer(Texts.more_info, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.NO.value, ignore_case=True),
    state=CantFallAsleepStates.first_advice
)
@dp.message_handler(
    Text(equals=YesNoButtons.YES.value, ignore_case=True),
    state=CantFallAsleepStates.is_useful_first
)
async def cant_asleep_second_advice(message: types.Message, state: FSMContext):
    await CantFallAsleepStates.second_advice.set()
    await message.answer(Texts.cant_fall_asleep_second_advice)
    await message.answer(Texts.is_useful, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.NO.value, ignore_case=True),
    state=CantFallAsleepStates.second_advice
)
@dp.message_handler(
    Text(equals=YesNoButtons.YES.value, ignore_case=True),
    state=CantFallAsleepStates.is_useful_second
)
async def cant_asleep_third_advice(message: types.Message, state: FSMContext):
    await CantFallAsleepStates.third_advice.set()
    await message.answer(Texts.cant_fall_asleep_third_advice)
    await message.answer(Texts.is_useful, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.NO.value, ignore_case=True),
    state=CantFallAsleepStates.third_advice
)
@dp.message_handler(
    Text(equals=YesNoButtons.YES.value, ignore_case=True),
    state=CantFallAsleepStates.is_useful_third
)
async def cant_asleep_fourth_advice(message: types.Message, state: FSMContext):
    await CantFallAsleepStates.fourth_advice.set()
    await message.answer(Texts.cant_fall_asleep_fourth_advice)
    await message.answer(Texts.is_useful, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.NO.value, ignore_case=True),
    state=CantFallAsleepStates.fourth_advice
)
@dp.message_handler(
    Text(equals=YesNoButtons.YES.value, ignore_case=True),
    state=CantFallAsleepStates.is_useful_fourth
)
async def cant_asleep_fifth_advice(message: types.Message, state: FSMContext):
    await CantFallAsleepStates.fifth_advice.set()
    await message.answer(Texts.cant_fall_asleep_fifth_advice)
    await message.answer(Texts.is_useful, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(equals=YesNoButtons.YES.value, ignore_case=True),
    state=MainStates.start
)
async def sleep_analysis_first_date(message: types.Message, state: FSMContext):
    await SleepAnalysisStates.input_first_time.set()
    await message.answer(Texts.sleep_analysis_first_time)


@dp.message_handler(
    state=SleepAnalysisStates.input_first_time
)
async def sleep_analysis_second_date(message: types.Message, state: FSMContext):
    if not TIME_RE.match(message.text):
        await message.answer(Texts.sleep_analysis_time_error)
    else:
        await SleepAnalysisStates.next()
        await state.set_data(message.text)
        await message.answer(Texts.sleep_analysis_second_time)


@dp.message_handler(
    state=SleepAnalysisStates.input_second_time
)
async def sleep_analysis_finish(message: types.Message, state: FSMContext):
    first_time = await state.get_data()
    if not TIME_RE.match(message.text):
        await message.answer(Texts.sleep_analysis_time_error)
    else:
        first_time_object = datetime.strptime(str(first_time), '%H:%M')
        second_time_object = datetime.strptime(message.text, '%H:%M')
        result = second_time_object - first_time_object  # в объекте почему то нет часа
        if result.seconds < 25200:
            await MainStates.themes.set()
            await message.answer(Texts.sleep_analysis_bad_result,
                                 reply_markup=ThemesButtonsTexts.buttons())
        elif 25200 <= result.seconds <= 32400:
            await MainStates.themes.set()
            await message.answer(Texts.sleep_analysis_ok_result)
            await message.answer(Texts.themes,
                                 reply_markup=ThemesButtonsTexts.buttons())
        else:
            await SleepAnalysisStates.next()
            await message.answer(Texts.sleep_analysis_grate_result,
                                 reply_markup=YesNoButtons.buttons())


@dp.message_handler(state=SleepAnalysisStates.third_step)
async def sleep_analysis_finish(message: types.Message, state: FSMContext):
    if message.text.lower() == YesNoButtons.YES.value.lower():
        await SleepAnalysisStates.next()
        await message.answer(Texts.sleep_analysis_finish_yes)
        await message.answer(Texts.anything_else, reply_markup=YesNoButtons.buttons())
    if message.text.lower() == YesNoButtons.NO.value.lower():
        await SleepAnalysisStates.next()
        await message.answer(Texts.sleep_analysis_finish_no)
        await message.answer(Texts.anything_else, reply_markup=YesNoButtons.buttons())


@dp.message_handler(
    Text(ThemesButtonsTexts.NOTHING.value, ignore_case=True),
    state=MainStates.themes
)
async def nothing_finish(message: types.Message, state: FSMContext):
    await MainStates.finish.set()
    await message.answer(Texts.nothing_finish)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
