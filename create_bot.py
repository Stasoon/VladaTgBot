from config import BOT_TOKEN
from aiogram import Bot, Dispatcher


if not BOT_TOKEN:
    exit("No token provided")


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)
