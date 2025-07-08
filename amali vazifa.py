# from telebot import TeleBot, types
# import random
# bot = TeleBot(token="8027965474:AAGab8Wq-nNjdwnfbUWUajGlV2s57pwFzD0")
#
# @bot.message_handler(commands=["start"])
# def start(msg: types.Message):
#     bot.send_message(msg.chat.id, "So‘z kiriting:")
#     bot.register_next_step_handler(msg, oquchi)
#
# def oquchi(message):
#     fd = message.text
#     bot.send_message(message.chat.id, "oyin oynashni holaysizmi ha/yoq")
#     if message.text == "ha":
#         bot.send_message(message.chat.id, "holganson tanlang agar oyangan sozingiz meni sonimbilan 1 hil bolsa siz yutasiz")
#         raqam = message.
#         print(raqam)
#         rando = random.randint(1,10)
#         bot.register_next_step_handler(message, find_the_number, raqam, rando)
#         print(rando)
#
#     if message.text == "yuq":
#         bot.register_next_step_handler(qk, start)
#
# def find_the_number(qk: types.Message, raqam, rando):
#     if rando == raqam:
#         bot.send_message(qk.chat.id, "Siz topdingiz.")
#         bot.register_next_step_handler(qk, start)
#
#     else:
#         bot.send_message(qk.chat.id, "noto‘g‘ri")
#         oquchi(qk)
#
# bot.polling()
