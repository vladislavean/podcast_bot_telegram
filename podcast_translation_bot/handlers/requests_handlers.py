from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler, CallbackContext, filters
from podcast_translation_bot.functions import Video

GET_VIDEO = range(1)

async def get_mp3_file(update: Update, context: CallbackContext):
    await update.message.reply_text(text="Вставьте ссылку на ютуб видео: ")
    return GET_VIDEO


async def get_video(update: Update, context: CallbackContext):
    url_message = update.message.text
    # че то мне не нравится этот участок кода ваще/////
    video = Video(url_message)
    title = video.get_video_title()
    video.download_video()
    await update.message.reply_document(document=f'/Users/vladislavananev/Desktop/project/podcast-translation-bot/static/{title}.mp3')
    return ConversationHandler.END

async def cancle_url_getting(update: Update, context: CallbackContext):
    await update.message.reply_text("Возвращайтесь, когда захотите!")
    return ConversationHandler.END

async def get_mp3_file_with_translate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text="Вот твой файл: Тут должен быть файл он будет через send_audio")