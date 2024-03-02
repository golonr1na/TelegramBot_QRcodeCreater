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
    Cbutton = types.KeyboardButton(texts.circleB)
    Rbutton = types.KeyboardButton(texts.regularB)
    markup.add(Cbutton, Rbutton)
    bot.send_message(message.chat.id, text=texts.greetings)
    bot.send_message(message.chat.id,text=texts.warning,reply_markup=markup)

@bot.message_handler(content_types=["text"])
def send_qr(message):
    circleTypeQR = False
    if message.text == texts.circleB:
        circleTypeQR = True
        bot.send_message(message.chat.id,text=texts.sendText)
    elif message.text == texts.regularB:
        circleTypeQR = False
        bot.send_message(message.chat.id, text=texts.sendText)
    else:
        if circleTypeQR:
            QRcodeCreate.create_circle_qr(message.text)
        else:
            QRcodeCreate.create_regular_qr(message.text)

    with open('qr-code.png','rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=texts.done)
    os.remove('qr-code.png')

bot.infinity_polling()