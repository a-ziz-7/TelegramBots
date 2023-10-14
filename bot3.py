import telebot
from config import api_key_aeg, api_key

bot = telebot.TeleBot(api_key_aeg)
bot2 = telebot.TeleBot(api_key)

@bot.message_handler(func=lambda message: True)
def ran_num(message):
    bot2.send_message(1001864551, message.from_user.id)

bot.polling()