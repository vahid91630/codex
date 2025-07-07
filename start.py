from aiogram import types
from database.models import add_user

async def start_handler(message: types.Message):
    user = message.from_user
    await add_user(user.id, user.full_name, user.username)
    await message.reply(f"سلام {user.full_name}!
آیدی عددی شما: {user.id}")
