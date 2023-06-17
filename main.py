from aiogram import executor, Dispatcher
from create_bot import dp
from keep_alive import keep_alive
from handlers import register_handlers


async def on_startup(dp: Dispatcher):
    print('Бот запущен')
    register_handlers(dp)


def start_bot():
    try:
        executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
    except Exception as e:
        print('Ошибка при запуске: ', e)


if __name__ == '__main__':
    keep_alive()
    start_bot()

