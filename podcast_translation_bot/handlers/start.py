from telegram import Update
from telegram.ext import ContextTypes


async def start(
            update: Update,
            context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.effective_user.send_message(
        f'Привет, {update.effective_user.first_name}. Это бот для перевода видео в подкаст.')
