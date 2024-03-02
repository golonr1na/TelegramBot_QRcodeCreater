import telebot
import qrcode

TOKEN = '' # Токен вашего бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я твой личный QR-генератор! "
                          "Пришли мне текст, и я с удовольствием создам для тебя красивый QR-код в формате PNG. "
                          "Давай начнем! 😊🔍🔲")

@bot.message_handler(content_types=["text"])
def send_qr(message):
#Создение qr кода
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=16,
        border=4,
    )
    qr.add_data(message.text)
    qr.make(fit=True)
# Преобразование в png
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('photo.png')
    img = open('photo.png','rb')

    bot.send_photo(message.chat.id, img, caption='Вот твой уникальный QR-код! '
                                                 'Теперь ты можешь использовать его для быстрого доступа к информации или передачи данных. '
                                                 'Надеюсь, он будет полезен для тебя!😉📲🔍')
    img.close()

bot.infinity_polling()
