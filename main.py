from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from handlers.start import start_handler
from database.db import init_db

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await start_handler(message)

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(f"پیام شما ذخیره شد:\n{message.text}")

if __name__ == '__main__':
    import asyncio
    asyncio.run(init_db())
    executor.start_polling(dp)
