import telebot
from keyboard import is_pressed
from random import randint
from socket import gethostbyname, gethostname
from time import sleep
from json import load, dump
import asyncio

#http://t.me/Alex_Zaliznuak_bot
#https://habr.com/ru/post/448310/
global IP

IP = "https://127.0.0.1:5000/"

bot = telebot.TeleBot('1638375655:AAFxI5GQ6JTkjBRsV4tuVW3OxXWf5GaI2Ag')
commands = [
    "/help - write all commands",
    "/invite - send bot`s invite url",   
    "/random a b - random num(a-b) default 1-6",
]

with open("settings.json", "r") as f:
    chats_id = load(f)["ChatsID"]
    print(chats_id)

keyboard_ossements = telebot.types.ReplyKeyboardMarkup(True)
keyboard_ossements.row('/url')

@bot.message_handler(commands=['help'])
def help_command(message):
    send = ""
    for command in commands:
        send += str(command) + "\n"*2
    bot.send_message(message.chat.id, send)

@bot.message_handler(commands=['invite','invite_code','invite_url'])
def invite(message):
    bot.send_message(message.chat.id, 'http://t.me/Alex_Zaliznuak_bot')

@bot.message_handler(commands=['init'])
def init_id(message):
    with open("settings.json", "r") as f:
        data = load(f)
    # bot.send_message(message.chat.id, f"Succesfull", reply_markup = None)
    if message.chat.id not in data["ChatsID"]:
        with open("settings.json", "w") as f:
            data["ChatsID"] += [message.chat.id]
            dump(data, f, indent = 4)
        bot.send_message(message.chat.id, f"init was succesfull", reply_markup = None)
    else:
        bot.send_message(message.chat.id, f"You was init", reply_markup = None)

@bot.message_handler(commands=['random'])
def game_random(message):
    args = tuple(message.text.split(" ")[1:3])
    send = (args[0], args[1]) if len(args) == 2 else (1, 6) 
    send = randint(int(send[0]), int(send[1]))
    bot.send_message(message.chat.id, f"Число: {send}", reply_markup = None)

@bot.message_handler(commands=['url', "Получить ссылку"])
def game_random(message):
    global IP
    IP = "http://" + gethostbyname(gethostname()) + ":5000/"
    for id_ in chats_id:
        bot.send_message(id_, IP, reply_markup = keyboard_ossements)

def main():
    IP = gethostbyname(gethostname())
    while not is_pressed("Esc"):
        bot.send_message(1513636690, IP)
        bot.polling(none_stop = True)

if __name__ == "__main__":
    main()