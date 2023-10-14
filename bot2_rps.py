from config import api_key_rps
from random import choice
from time import sleep
import telebot

bot = telebot.TeleBot(api_key_rps)

possibilities_dict = {"r": "Rock", "p": "Paper", "s": "Scissors",
                      "rock": "Rock", "paper": "Paper", "scissors": "Scissors",
                      "1": "Rock", "2": "Paper", "3": "Scissors"}
possibilities_comp = ["r", "p", "s"]
possibilities_rock = ["rock", "r", "1"]
possibilities_paper = ["paper", "p", "2"]
possibilities_scissors = ["scissors", "s", "3"]
score_player, score_comp = 0, 0
winner_exists = False
data = {}


@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.chat.id,
                     "Welcome!!!\n" + "Score 10 before computer to win!\nEnter score to get current score\nEnter zxc to exit the game")


@bot.message_handler(commands=['reset'])
def reset(message):
    global score_player, score_comp, winner_exists
    score_player, score_comp = 0, 0
    winner_exists = False
    bot.send_message(message.chat.id, "The game was reset!")


@bot.message_handler(func=lambda message: True)
def game(message):
    global score_player, score_comp, winner_exists
    if not winner_exists:
        reply = message.text.lower()
        com_guess = choice(possibilities_comp)
        bot.send_message(message.chat.id, "---------------------------------")
        if reply in possibilities_rock:
            if com_guess in possibilities_rock:
                tie_case(reply, com_guess, message)
            elif com_guess in possibilities_paper:
                l_case(reply, com_guess, message)
            elif com_guess in possibilities_scissors:
                w_case(reply, com_guess, message)

        elif reply in possibilities_paper:
            if com_guess in possibilities_rock:
                w_case(reply, com_guess, message)
            elif com_guess in possibilities_paper:
                tie_case(reply, com_guess, message)
            elif com_guess in possibilities_scissors:
                l_case(reply, com_guess, message)


        elif reply in possibilities_scissors:
            if com_guess in possibilities_rock:
                l_case(reply, com_guess, message)
            elif com_guess in possibilities_paper:
                w_case(reply, com_guess, message)
            elif com_guess in possibilities_scissors:
                tie_case(reply, com_guess, message)

        elif reply == "zxc":
            winner_exists = True
            bot.send_message(message.chat.id, "Game is over!")

        elif reply == "score":
            bot.send_message(message.chat.id, f"Player score: {score_player}\nComputer score: {score_comp}\n")

        else:
            bot.send_message(message.chat.id, "Enter a valid choice!\n")

        if score_comp > 10 or score_player > 10:
            winner_exists = True

        bot.send_message(message.chat.id, "---------------------------------")
        bot.send_message(message.chat.id, ("You won" if (score_comp < score_player) else "Computer won") +
                         f"\nPlayer score: {score_player}\nComputer score: {score_comp}\n") if winner_exists \
            else bot.send_message(message.chat.id, "Rock? Paper? Scissors?")
    else:
        bot.send_message(message.chat.id, "Please call a reset command to reset the game")


def tie_case(r, c, message):
    bot.send_message(message.chat.id, f"Computer picked: {possibilities_dict[c]}")
    sleep(1)
    bot.send_message(message.chat.id, f"Tie! Both picked {possibilities_dict[r]}\n")
    sleep(0.5)


def w_case(r, c, message):
    global score_player
    score_player += 1
    bot.send_message(message.chat.id, f"Computer picked: {possibilities_dict[c]}")
    sleep(1)
    bot.send_message(message.chat.id, f"You won! {possibilities_dict[r]} beats {possibilities_dict[c]}\n")
    sleep(0.5)


def l_case(r, c, message):
    global score_comp
    score_comp += 1
    bot.send_message(message.chat.id, f"Computer picked: {possibilities_dict[c]}")
    sleep(1)
    bot.send_message(message.chat.id, f"You lost! {possibilities_dict[r]} looses to {possibilities_dict[c]}\n")
    sleep(0.5)


bot.infinity_polling()
