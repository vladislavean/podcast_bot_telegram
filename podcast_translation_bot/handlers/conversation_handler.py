from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, filters

from podcast_translation_bot.handlers.requests_handlers import (get_mp3_file,
                                                                get_video,
                                                                GET_VIDEO,
                                                                cancel_url_getting)


def mp3_conversation_handler() -> ConversationHandler:
    conv_handler_mp3 = ConversationHandler(
        entry_points=[CommandHandler('get_mp3', get_mp3_file)],
        states={
            GET_VIDEO: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_video),
                        CommandHandler('cancel', cancel_url_getting)],
        },
        fallbacks=[CommandHandler('cancel_getting', cancel_url_getting)]
    )
    return conv_handler_mp3
