from dotenv import load_dotenv
import os

load_dotenv('.env')

chat_ids = ['']

seconds_btw_telling_jokes = 3600
need_to_send_jokes = True


try:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
except Exception as e:
    print('Ошибка чтения переменных окружения:', e)





