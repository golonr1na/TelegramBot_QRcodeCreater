import telebot
from telebot import types
import config
import QRcodeCreate
import texts
import os

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cbutton = types.KeyboardButton(texts.circleB)
    rbutton = types.KeyboardButton(texts.regularB)
    markup.add(cbutton, rbutton)
    bot.send_message(message.chat.id, text=texts.greetings, reply_markup=markup)
    bot.send_message(message.chat.id, text=texts.warning)


@bot.message_handler(content_types=["text"])
def send_qr(message):
    if message.text == texts.circleB:
        QRcodeCreate.typeiscircle = True
        bot.send_message(message.chat.id, text=texts.selectedC)
        bot.send_message(message.chat.id, text=texts.sendText)
    elif message.text == texts.regularB:
        QRcodeCreate.typeiscircle = False
        bot.send_message(message.chat.id, text=texts.selectedR)
        bot.send_message(message.chat.id, text=texts.sendText)
    else:
        #print(message.text, " - from {0.first_name} {0.last_name}".format(message.from_user))
        QRcodeCreate.create_qr(message.text)

        with open('qr-code.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo=photo, caption=texts.done)
        os.remove('qr-code.png')


bot.infinity_polling()
