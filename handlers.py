import string
from aiogram import types, Dispatcher
from misc.jokes import get_random_joke, get_joke_about_women


async def answer_start(msg: types.Message):
    await msg.answer('Здоров, заебал')


async def reply_joke(msg: types.Message):
    joke = await get_random_joke()
    await msg.reply(joke)


async def reply_women_joke(msg: types.Message):
    joke = await get_joke_about_women()
    await msg.answer(joke, parse_mode='html')


async def answer_to_yes_word(msg: types.Message):
    if len(msg.text) == 2 and 'да' in msg.text.lower():
        await msg.reply('Пизда')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(answer_start, commands=['start'])
    dp.register_message_handler(reply_joke, commands=['joke'])
    dp.register_message_handler(reply_women_joke, commands=['womjoke'])
    dp.register_message_handler(answer_to_yes_word, content_types=['text'])

