"""
таски:
1) найти библиотеку котоорая рабтает с видео MoviePy например  pydub opencv moviepy, бот будет на стоит попробовать на 
python telegram bot https://docs.python-telegram-bot.org/en/v21.1.1/index.html либо попробую снова на aiogram. Вообще можно рассмотреть вариант написать две версии
2) Видео скачивается по ссылке на ютубе(мб в дальнейшем по прямой ссылке тоже)
3) Сделать раздедение видео на аудио и видео
4) Далее аудио дорога переводистя на язык который был указан при начале работы в боте
функции бота 
    1. Видео в аудио
    2. Видео в аудио с переводом
        Будут кнопки с языком

        
В голову пришла идея написать это в виде микросервиса, будет сервис который будет отвечать за статические файлы их отдачу и загрузку.
И рядом будет клиент телеграм бот
хочется сделать два сервиса 

1 для статики
2 для запросов 
но как это реализовать пока не сильно понятно

https://fastapi.tiangolo.com/ru/tutorial/static-files/
https://habr.com/ru/articles/710376/

"""

from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters
from handlers import start, get_mp3_file, get_mp3_file_with_translate, get_video, GET_VIDEO, cancel_url_getting
import os
from exceptions import StartingAppError
from handlers_declaration import HandlersDeclaration

import logging


from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
logger = logging.basicConfig(level=logging.DEBUG, filename="bot_log.log")

def get_app(TOKEN: str):
    app = ApplicationBuilder().token(TOKEN).build()
    
    handlers = HandlersDeclaration()
    application = handlers.handlers_declaration(app)
    
    return application


if __name__ == '__main__':
    try:
        app = get_app(TOKEN)
        logging.info("App are created")
        logging.info("Starting...")
        app.run_polling()
    except:
        raise StartingAppError