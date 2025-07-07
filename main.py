import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7847661218:AAFjJ8DOpzoj0-fRGQJ1PSkCCsAB9qS8GNQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.username != "vahid91640":
        return
    await update.message.reply_text("سلام مدیر عزیز! ربات در خدمت شماست.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()