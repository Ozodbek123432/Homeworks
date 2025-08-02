from pyexpat.errors import messages
from telebot import TeleBot

token = "8027965474:AAGab8Wq-nNjdwnfbUWUajGlV2s57pwFzD0"
bot = TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    print("kod ishladi")
    chat_id = message.chat.id
    user_name = message.from_user.id
    print(user_name)
    bot.send_message(chat_id, "salom bu kod  ishladi")
@bot.message_next_handler(messages)
def next_handler(message,chat_id):
    if message.text == "salom":
        bot.send_message(chat_id, "tekshruv")

bot.polling(non_stop=True)