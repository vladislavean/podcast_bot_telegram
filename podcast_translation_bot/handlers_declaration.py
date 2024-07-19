
from telegram.ext import (CommandHandler,
                          ApplicationBuilder)

from handlers import (start,
                      conversation_handler)


class HandlersDeclaration:
    @staticmethod
    def handlers_declaration(
                            app: ApplicationBuilder
                             ) -> ApplicationBuilder:
            app.add_handler(CommandHandler('start', start))
            app.add_handler(conversation_handler.mp3_conversation_handler())
            return app

     

