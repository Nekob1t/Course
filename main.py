import telebot
import requests
import json

bot = telebot.TeleBot('6128729724:AAFBUpqRFdLd8n0FNyk4svre4QEBULpgnIM')
API = 'f3a9f080d7e599dfda7739b791422f79'


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, я твоя карманная метеостанция! Напиши название города")


@bot.message_handler(content_types=["text"])
def weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        speed = data["wind"]["speed"]
        bot.reply_to(message, f"Вот, что мне удалось найти по данному городу: температура {temp} °C, ощущается как {feels} °C, влажность {humidity}%, скорость ветра {speed} м/с")
    else:
        bot.reply_to(message, "Город указан не верно")


bot.polling(none_stop=True)