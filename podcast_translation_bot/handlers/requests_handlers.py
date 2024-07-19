from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, CallbackContext, filters
from podcast_translation_bot.utils import Video, VideoDownloader
import os
from dotenv import load_dotenv

load_dotenv()

PATH = os.getenv("PATH")
GET_VIDEO = range(1)


async def get_mp3_file(
        update: Update,
        context: CallbackContext
):
    await update.message.reply_text(text="Вставьте ссылку на ютуб видео: ")
    return GET_VIDEO


async def get_video(
        update: Update,
        context: CallbackContext
):
    url_message = update.message.text
    video = Video(url_message)
    title = video.get_video_title
    VideoDownloader.download_video(video)
    await update.message.reply_document(document=f'{os.getcwd()}/../static/{title}.mp3')
    return ConversationHandler.END


async def cancel_url_getting(
        update: Update,
        context: CallbackContext
):
    await update.message.reply_text("Возвращайтесь, когда захотите!")
    return ConversationHandler.END


async def get_mp3_file_with_translate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text="Вот твой файл: Тут должен быть файл он будет через send_audio")
