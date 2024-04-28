
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
                            cancel_url_getting)

class HandlersDeclaration:
    @staticmethod
    def mp3_conversation_hander() -> ConversationHandler: 
        conv_handler_mp3 = ConversationHandler(
            entry_points=[CommandHandler('get_mp3', get_mp3_file)],
            states= {
                GET_VIDEO: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_video), CommandHandler('cancel', cancel_url_getting)],
            },
            fallbacks=[CommandHandler('cancel_getting', cancel_url_getting)]
        )
        return conv_handler_mp3
   
    def handlers_declaration(self, app: ApplicationBuilder) -> ApplicationBuilder:
            app.add_handler(CommandHandler('start', start))
            app.add_handler(self.mp3_conversation_hander())
            return app

     

