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
    await msg.reply(joke, parse_mode='html')


async def answer_to_chmonya_sticker(msg: types.Message):
    if msg.sticker.file_id == "CAACAgIAAxkBAAEB3YRkjhtZBHBls6jk-cTqkgzEDVp7QQAC_QAD8pmQOUZ64WPHa_1aLwQ":
        await msg.answer_chat_action(action="upload_photo")
        await msg.answer_photo(photo="AgACAgIAAxkBAAEB3YhkjhwdFZiNYYzm3X-9ni4eahOYnwAC0M8xGyezcEi8NmmtK4vJywEAAwIAA20AAy8E")


async def answer_to_yes_word(msg: types.Message):
    if len(msg.text) == 2 and 'да' in msg.text.lower():
        await msg.reply('Пизда')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(answer_start, commands=['start'])
    dp.register_message_handler(reply_joke, commands=['joke'])
    dp.register_message_handler(reply_women_joke, commands=['womjoke'])
    dp.register_message_handler(answer_to_chmonya_sticker, content_types=['sticker'])
    dp.register_message_handler(answer_to_yes_word, content_types=['text'])

