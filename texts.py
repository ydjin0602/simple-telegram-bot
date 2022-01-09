from enum import Enum

from aiogram import types


class ThemesButtonsTexts(Enum):
    OFTEN_WAKE_UP = 'Ты часто просыпаешься ночью по несколько раз.'
    SLEEP_PARALYSIS = 'Тебя беспокоит сонный паралич.'
    NIGHTMARES = 'Тебя мучают ночные кошмары.'
    CANT_SLEEP = 'Просыпаешься и долго не можешь уснуть снова.'
    SLEEPINESS = 'Присутствует сонливость в течение дня.'
    FALL_ASLEEP_FOR_A_LONG_TIME = 'Когда ложишься спать, ' \
                                  'долго засыпаешь и не можешь уснуть.'

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

    nightmares_start = 'pass_nightmares_start'
    nightmares_first_problem = 'pass_nightmares_first_problem'
    nightmares_second_problem = 'pass_nightmares_second_problem'
    nightmares_look_second_problem = 'pass_nightmares_look_second_problem'
    nightmares_look_first_problem = 'pass_nightmares_look_first_problem'
    nightmares_finish = 'pass_nightmares_finish'

    anything_else = 'Могу ли я еще чем то помочь?'
    finish = 'pass_finish'
