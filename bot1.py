import telebot
import config
import time
import random

bot = telebot.TeleBot(config.api_key)
bot1 = telebot.TeleBot(config.api_key_aeg)
data = {}
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Welcome!!!")


@bot.message_handler(func=lambda message: False)
def get_time(message):
    print(time.ctime(time.time()))
    bot.send_message(message.chat.id, time.ctime(time.time()))


@bot.message_handler(func=lambda message: False)
def ran_num(message):
    for i in range(int(message.text)):
        bot.send_message(message.chat.id, random.randint(1, 10))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "/get_time" or message.text.lower() == "time":
        get_time(message)
        return
    if message.text.isdigit():
        ran_num(message)
        return
    print(message.text)
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()
