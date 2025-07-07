from flask import Flask, request
import telebot
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return 'روبات Kodex آماده‌ست!'

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return 'OK', 200

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "سلام! من ربات CRM باتیس هستم. پیام‌هات رو بفرست.")

if __name__ == '__main__':
    webhook_url = f"https://codex-4zmj.onrender.com/{BOT_TOKEN}"
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)
    app.run(host='0.0.0.0', port=10000)
