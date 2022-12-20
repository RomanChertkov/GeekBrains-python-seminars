"""
telegram bot. string cutter
"""
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


BOT_TOKEN = "5683302678:AAFNxgTNrvdq0luZd8sxkfxuTwQsWohvgzM"
bot = Bot(token=BOT_TOKEN)
updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher

def start(update, context):
    """start command"""
    context.bot.send_message(
        update.effective_chat.id,
        "Привет. Введи текст и я уберу все слова, в который есть \"абв\""
    )

def cut_string(update, context):
    """Cut string"""
    context.bot.send_message(
        update.effective_chat.id,
        " ".join(
            list(filter(lambda x: not 'абв' in x , update.message.text.split()))
        )
    )

start_handler  = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, cut_string)


dispatcher.add_handler(start_handler)
dispatcher.add_handler( message_handler)

updater.start_polling()
updater.idle()
