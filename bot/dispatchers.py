from aiogram import types


async def start(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


async def echo(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=1)
    btns_text = (
        'Yes!', 'No!', "I don't know",
        "Who am i?",
        "Where am i?",
        "Who is there?",
    )
    keyboard_markup.add(*(types.KeyboardButton(text) for text in btns_text))

    await message.answer(message.text, reply_markup=keyboard_markup)
