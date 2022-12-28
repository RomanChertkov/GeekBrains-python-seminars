"""
telegram bot. string cutter
"""
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


BOT_TOKEN = "5683302678:AAFNxgTNrvdq0luZd8sxkfxuTwQsWohvgzM"
bot = Bot(token=BOT_TOKEN)
updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher

def logger(update, result = ""):
    """ bot command logger"""
    with open("bot_log.txt", "a", encoding="UTF-8") as log:
        log.write( f"{update.effective_chat.id}, {update.message.text}, {result}\n")


def start(update, context):
    """start command"""
   
    logger(update)
    context.bot.send_message(
        update.effective_chat.id,
        "Синтаксис: комманда число1 число 2\n"+
        "/sum - сумма\n/diff - разность\n/mult- умножение\n/div - деление\n"+
        "/help"
    )

def sum_command(update, context):
    """sum command"""
    message = update.message.text.split()
    if not len(message) == 3:
        return context.bot.send_message(
                    update.effective_chat.id,
                    "Ошибка! Введите комманду и два числа."
        )
    result = round(float(message[1]) + float(message[2]),2)
    logger(update, result)
    context.bot.send_message(
        update.effective_chat.id,
        f"{message[1]} + {message[2]}  = {result}"
    )


def diff_command(update, context):
    """diff command"""
    message = update.message.text.split()
    if not len(message) == 3:
        return context.bot.send_message(
                    update.effective_chat.id,
                    "Ошибка! Введите комманду и два числа."
        )
    result = round(float(message[1]) - float(message[2]),2)
    logger(update, result)
    context.bot.send_message(
        update.effective_chat.id,
        f"{message[1]} - {message[2]}  ={result}"
    )

def mult_command(update, context):
    """mult command"""
    message = update.message.text.split()
    if not len(message) == 3:
        return context.bot.send_message(
                    update.effective_chat.id,
                    "Ошибка! Введите комманду и два числа."
        )
    result = round(float(message[1]) * float(message[2]),2)
    logger(update, result)
    context.bot.send_message(
        update.effective_chat.id,
        f"{message[1]} * {message[2]}  ={result}"
    )

def div_command(update, context):
    """div command"""
    message = update.message.text.split()
    if not len(message) == 3:
        return context.bot.send_message(
                    update.effective_chat.id,
                    "Ошибка! Введите комманду и два числа."
        )
    result = round(float(message[1]) / float(message[2]),2)
    logger(update, result)
    context.bot.send_message(
        update.effective_chat.id,
        f"{message[1]} / {message[2]}  ={result}"
    )

start_handler  = CommandHandler('start', start)
help_handler  = CommandHandler('help', start)
sum_handler  = CommandHandler('sum', sum_command)
diff_handler  = CommandHandler('diff', diff_command)
mult_handler  = CommandHandler('mult', mult_command)
div_handler = CommandHandler('div', div_command)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(sum_handler)
dispatcher.add_handler(diff_handler)
dispatcher.add_handler(mult_handler)
dispatcher.add_handler(div_handler)


updater.start_polling()
updater.idle()
