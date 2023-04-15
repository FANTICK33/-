import telebot
import requests
import json

bot = telebot.TeleBot("5734323883:AAG2ySfHjAFy1EFz7_WWIlCIQmGlFCPsn5I")
API = '169b2d96e81576b76cf0dbe17e35661e'

# Привествие


@bot.message_handler(commands=['start'])
def profile(message):
    bot.send_message(
        message.chat.id, 'Привет, рад тебя видеть! Напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    temp = data["main"]["temp"]
    bot.reply_to(message, f'Сейчас погода: {temp}')

    image = 'Тепло.png' if temp > 5.0 else 'Холодно.png'
    file = open('./Telegram-Bot/Weather/' + image, 'rb')
    bot.send_photo(message.chat.id, file)


bot.infinity_polling()
