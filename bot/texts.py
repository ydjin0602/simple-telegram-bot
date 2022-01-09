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
