import telebot
from flask import Flask, request
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام! زه چمتو یم 😊")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([
        telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    ])
    return "OK", 200

@server.route("/")
def index():
    return "Bot is running!"

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
