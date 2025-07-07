import aiosqlite
from config import DB_NAME

async def add_user(user_id, full_name, username, is_admin=0):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            INSERT OR IGNORE INTO users (user_id, full_name, username, is_admin)
            VALUES (?, ?, ?, ?)
        """, (user_id, full_name, username, is_admin))
        await db.commit()
