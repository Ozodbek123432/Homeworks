from telebot import TeleBot, types
import random
bot = TeleBot(token="8027965474:AAGab8Wq-nNjdwnfbUWUajGlV2s57pwFzD0")

@bot.message_handler(commands=['start'])
def start(xabar: types.Message):
    bot.send_message(xabar.from_user.id, "salom bu bot tayr")
    m = bot.send_message(xabar.from_user.id, "Raqam kiriting")
    bot.register_next_step_handler(xabar, t)

def t(xabar: types.Message):
    raqam = random.randint(1, 100)
    print(raqam)
    if xabar.from_user.id == raqam:
        bot.send_message(xabar.from_user.id, "To'g'ri topdingiz")
    elif xabar.from_user.id < raqam:
        bot.send_message(xabar.from_user.id, "son Kichik")
    elif xabar.from_user.id > raqam:
        bot.send_message(xabar.from_user.id, "son Katta")

    bot.register_next_step_handler(xabar, t)

bot.polling()