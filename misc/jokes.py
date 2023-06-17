from bs4 import BeautifulSoup
import random
import requests
import asyncio
from create_bot import bot
from config import need_to_send_jokes, seconds_btw_telling_jokes, chat_ids


async def get_random_joke():
    main_url = 'https://веселун.рф/anekdoty/good/'
    joke_number = random.randint(1, 1001) - 1
    page_number = joke_number // 10

    url = main_url + f'{page_number}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    data = soup.findAll('p', attrs={'itemprop': 'articleBody'})

    return data[joke_number % 10].text.replace('  ', '\n').replace(' -', '\n-').replace(':-', ':\n-') \
        .replace('?-', '?\n-').replace('. —', '.\n-').replace('.-', '.\n-').replace('?—', '?\n—')


async def send_jokes_by_interval():
    await asyncio.sleep(50)
    while True:
        if not need_to_send_jokes or len(chat_ids) == 0:
            await asyncio.sleep(seconds_btw_telling_jokes)
            continue

        joke = await get_random_joke()
        for chat_id in chat_ids:
            await bot.send_message(chat_id=chat_id, text=joke)
            await asyncio.sleep(0.2)
        await asyncio.sleep(seconds_btw_telling_jokes)

