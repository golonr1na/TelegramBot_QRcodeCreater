import telebot
from telebot import types
import config
import QRcodeCreate
import texts
import os

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Содание кнопок на клавиатуре
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cbutton = types.KeyboardButton(texts.circleB)
    rbutton = types.KeyboardButton(texts.regularB)
    markup.add(cbutton, rbutton)
    # Приветственные сообщения
    bot.send_message(message.chat.id, text=texts.greetings, reply_markup=markup)
    bot.send_message(message.chat.id, text=texts.warning)


@bot.message_handler(content_types=["text"])
def send_qr(message):
    # Проверка сообщений от пользователя
    if message.text == texts.circleB:
        QRcodeCreate.typeiscircle = True
        bot.send_message(message.chat.id, text=texts.selectedC)
        bot.send_message(message.chat.id, text=texts.sendText)
    elif message.text == texts.regularB:
        QRcodeCreate.typeiscircle = False
        bot.send_message(message.chat.id, text=texts.selectedR)
        bot.send_message(message.chat.id, text=texts.sendText)

    else: # Любой текст не являющийся выбором типа преобразуется в qr-код
        QRcodeCreate.create_qr(message.text)

        # Конструкция with открывает файл и после выполнения своего блока кода закрывает файл
        with open('qr-code.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo=photo, caption=texts.done)
        os.remove('qr-code.png') #удаление фото qr-кода


bot.infinity_polling()
