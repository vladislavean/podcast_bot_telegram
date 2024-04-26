
from telegram.ext import (ConversationHandler, 
                          CommandHandler, 
                          filters, 
                          MessageHandler,
                          ApplicationBuilder)
from podcast_translation_bot.handlers import (start, 
                            get_mp3_file, 
                            get_mp3_file_with_translate, 
                            get_video, 
                            GET_VIDEO, 
                            cancle_url_getting)

class HandlersDeclaration:
    @staticmethod
    def mp3_conversation_hander() -> ConversationHandler: 
        conv_handler_mp3 = ConversationHandler(
            entry_points=[CommandHandler('get_mp3', get_mp3_file)],
            states= {
                GET_VIDEO: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_video), CommandHandler('cancle', cancle_url_getting)],
            },
            fallbacks=[CommandHandler('cancle_getting', cancle_url_getting)]
        )
        return conv_handler_mp3
   
    @staticmethod
    def handlers_declaration(app: ApplicationBuilder) -> ApplicationBuilder:
            app.add_handler(CommandHandler('start', start))
            app.add_handler(HandlersDeclaration.mp3_conversation_hander())
            return app

     
