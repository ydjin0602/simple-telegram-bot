from enum import Enum

from aiogram import types


class ThemesButtonsTexts(Enum):
    OFTEN_WAKE_UP = 'Ты часто просыпаешься ночью по несколько раз.'
    SLEEP_PARALYSIS = 'Тебя беспокоит сонный паралич.'
    NIGHTMARES = 'Тебя мучают ночные кошмары.'
    CANT_SLEEP = 'Просыпаешься и долго не можешь уснуть снова.'
    SLEEPINESS = 'Присутствует сонливость в течение дня.'
    CANT_FALL_ASLEEP = 'Когда ложишься спать, долго засыпаешь и не можешь уснуть.'

    @staticmethod
    def buttons():
        keyboard_markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
        keyboard_markup.add(*(button.value for button in ThemesButtonsTexts))
        return keyboard_markup


class NightmaresButtonsTexts(Enum):
    FIRST_PROBLEM = 'Что делать чтобы кошмары не снились или снились реже?'
    SECOND_PROBLEM = 'Как уснуть снова после кошмара?'

    @staticmethod
    def buttons():
        keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        keyboard_markup.add(*(button.value for button in NightmaresButtonsTexts))
        return keyboard_markup


class SleepinessButtonsTexts(Enum):
    FIRST_ADVICE = 'Профилактика сонливости в дневное время.'
    SECOND_ADVICE = 'Как временно устранить сонливость днем на данный момент.'

    @staticmethod
    def buttons():
        keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        keyboard_markup.add(*(button.value for button in SleepinessButtonsTexts))
        return keyboard_markup


class YesNoButtons(Enum):
    YES = 'Да'
    NO = 'Нет'

    @staticmethod
    def buttons():
        keyboard_markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        keyboard_markup.add(*(button.value for button in YesNoButtons))
        return keyboard_markup


class Texts:
    start = 'Привет. Если ты меня нашел, возможно ' \
            'у тебя есть какие то проблемы со сном.'
    happy_for_you = 'Рад за тебя.'
    themes = 'Хорошо, тогда выбери одну из проблем, которая тебе подходит:'

    often_wake_up_first_assumption = 'pass_often_wake_up_first'
    often_wake_up_first_assumption_yes = 'pass_often_wake_up_first_yes'
    often_wake_up_second_assumption = 'pass_often_wake_up_second'
    often_wake_up_second_assumption_yes = 'pass_often_wake_up_second_yes'
    often_wake_up_third_assumption = 'pass_often_wake_up_third'
    often_wake_up_third_assumption_yes = 'pass_often_wake_up_third_yes'
    often_wake_up_third_assumption_no = 'pass_often_wake_up_third_no'

    cant_fall_asleep_first_advice = 'pass_cant_fall_asleep_first_advice'
    cant_fall_asleep_first_advice_yes = 'pass_cant_fall_asleep_first_advice_yes'
    cant_fall_asleep_second_advice = 'pass_cant_fall_asleep_second_advice'
    cant_fall_asleep_second_advice_yes = 'pass_cant_fall_asleep_second_advice_yes'
    cant_fall_asleep_third_advice = 'pass_cant_fall_asleep_third_advice'
    cant_fall_asleep_third_advice_yes = 'pass_cant_fall_asleep_third_advice_yes'
    cant_fall_asleep_fourth_advice = 'pass_cant_fall_asleep_fourth_advice'
    cant_fall_asleep_fourth_advice_yes = 'pass_cant_fall_asleep_fourth_advice_yes'
    cant_fall_asleep_fifth_advice = 'pass_cant_fall_asleep_fifth_advice'
    cant_fall_asleep_fifth_advice_yes = 'pass_cant_fall_asleep_fifth_advice_yes'
    cant_fall_asleep_fifth_advice_no = 'pass_cant_fall_asleep_fifth_advice_no'
    cant_fall_asleep_early_finish = 'Рад, что был тебе полезен'
    cant_fall_asleep_finish = 'Советую обратиться к сомнологу, он точно ' \
                              'подскажет тебе, как решить твою проблему.'

    is_useful = 'pass_is_useful'
    more_info = 'pass_more_info'

    nightmares_start = 'pass_nightmares_start'
    nightmares_first_problem = 'pass_nightmares_first_problem'
    nightmares_second_problem = 'pass_nightmares_second_problem'
    nightmares_look_second_problem = 'pass_nightmares_look_second_problem'
    nightmares_look_first_problem = 'pass_nightmares_look_first_problem'
    nightmares_finish = 'pass_nightmares_finish'

    sleep_paralysis_advices = 'pass_sleep_paralysis_advices'

    cant_sleep_advices = 'pass_cant_sleep_advices'

    sleepiness_start = 'pass_sleepiness_start'
    sleepiness_first_advice = 'pass_sleepiness_first_problem'
    sleepiness_second_advice = 'pass_sleepiness_second_problem'
    sleepiness_look_second_advice = 'pass_sleepiness_look_second_problem'
    sleepiness_look_first_advice = 'pass_sleepiness_look_first_problem'
    sleepiness_finish = 'pass_sleepiness_finish'

    anything_else = 'Могу ли я еще чем то помочь?'
    finish = 'pass_finish'
