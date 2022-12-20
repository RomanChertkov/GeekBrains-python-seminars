"""
telegram bot. sweet game
"""
import random
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


BOT_TOKEN = "5683302678:AAFNxgTNrvdq0luZd8sxkfxuTwQsWohvgzM"
bot = Bot(token=BOT_TOKEN)
updater = Updater(token=BOT_TOKEN)
dispatcher = updater.dispatcher

total_candies = 120
error_messages =[
    "А ряха не треснет? Максимум 28 конфет 😁",
    "Побереги здоровье. 28 - это уже перебор, а у тебе перебор перебора",
    "Похоже у тебя что-то должно слипнуться.Пожалей врачей. Верни всё обратно. ",
    "И тут тоже руки загребуки 😭😭😭. Не более 28 конфет в одни руки. Тут тебе не ozon"
]

def start(update, context):
    """start command"""
    context.bot.send_message(
        update.effective_chat.id,
        "Привет. Давай сыграем в игру 😁\nБери конфеты, но не более 28"
    )

def restart(update, context):
    """start command"""
    global total_candies
    total_candies = 120
    context.bot.send_message(
        update.effective_chat.id,
        "Давай снова сыграем в игру 😁\nБери конфеты, но не более 28"
    )

def take_candies(update, context):
    """Cut string"""
    global total_candies
    human_move = int(update.message.text)

    if human_move >28:
        context.bot.send_message(
            update.effective_chat.id,
            error_messages[random.randint(0,3)]
        )
        return

    if total_candies - human_move == 0:
        context.bot.send_message(
            update.effective_chat.id,
            "Ты забрал все конфеты и победил🥳. В твоих руках победа и жир на жопе 😁"
        )
        return
    if total_candies < human_move:
        context.bot.send_message(
            update.effective_chat.id,
            "К сожалению, конфетных кредитов пока нет 😭 А было бы здорово 😁"
        )
        return

    total_candies-= human_move
    context.bot.send_message(
        update.effective_chat.id,
        f"конфет осталось:{total_candies}"
    )

    random_val = random.randint(1,28)

    if total_candies <= 28:
        total_candies = 0
        context.bot.send_message(
            update.effective_chat.id,
            "Я  забираю оставшиеся конфеты и изящно обжираюсь в гордом одиночестве 😋"
        )
        context.bot.send_message(
            update.effective_chat.id,
            "Введи /restart для перезапуска игры"
        )
        return

    total_candies-= random_val
    context.bot.send_message(
        update.effective_chat.id,
        f"Я беру {random_val}\nконфет осталось:{total_candies}"
    )

start_handler  = CommandHandler('start', start)
restart_handler  = CommandHandler('restart', restart)
message_handler = MessageHandler(Filters.text, take_candies)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(restart_handler)
dispatcher.add_handler( message_handler)

updater.start_polling()
updater.idle()
