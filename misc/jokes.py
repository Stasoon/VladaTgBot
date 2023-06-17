from bs4 import BeautifulSoup
import random
import requests
import asyncio
from create_bot import bot
from config import need_to_send_jokes, seconds_btw_telling_jokes, chat_ids


async def get_random_joke():
    anectots_on_one_page_count = 10
    joke_number = random.randint(0, 5_000)
    page_number = joke_number // anectots_on_one_page_count

    main_url = 'https://веселун.рф/anekdoty/good/'
    url = main_url + f'{page_number}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    data = soup.findAll('p', attrs={'itemprop': 'articleBody'})

    return data[joke_number % anectots_on_one_page_count]\
        .text.replace('  ', '\n').replace(' -', '\n-').replace(':-', ':\n-') \
        .replace('?-', '?\n-').replace('. —', '.\n-').replace('.-', '.\n-').replace('?—', '?\n—')


async def get_joke_about_women():
    main_url = "https://anekdotbar.ru/pro-zhenschin/page/"
    joke_number = random.randint(1, 500)
    page_number = joke_number // 20

    url = main_url + f'{page_number}'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    data = soup.findAll('div', attrs={'class': 'tecst'})

    return data[joke_number % 20].text


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


