from fastapi import FastAPI, Request
import httpx

app = FastAPI()

BOT_TOKEN = "7847661218:AAEIHUcwg2gb7jF8zdK75w2Xk_exIewWAPU"
WEBHOOK_URL = "https://codex-4zmj.onrender.com"
ADMIN_ID = 6065428372  # Telegram numeric ID for @vahid91640
MANAGER_CHANNEL = "-1002096928375"  # Telegram channel ID

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.on_event("startup")
async def set_webhook():
    url = f"{API_URL}/setWebhook"
    async with httpx.AsyncClient() as client:
        await client.post(url, json={"url": WEBHOOK_URL})

@app.post("/")
async def handle_update(request: Request):
    data = await request.json()
    message = data.get("message", {}).get("text")
    chat_id = data.get("message", {}).get("chat", {}).get("id")
    user_id = data.get("message", {}).get("from", {}).get("id")
    if message and chat_id:
        if user_id != ADMIN_ID:
            reply = "شما اجازه استفاده از این ربات را ندارید."
        else:
            reply = f"مدیر عزیز، شما فرمودید: {message}"
            await send_to_channel(f"دستور مدیر: {message}")
        async with httpx.AsyncClient() as client:
            await client.post(f"{API_URL}/sendMessage", data={"chat_id": chat_id, "text": reply})
    return {"ok": True}

async def send_to_channel(text):
    async with httpx.AsyncClient() as client:
        await client.post(f"{API_URL}/sendMessage", data={"chat_id": MANAGER_CHANNEL, "text": text})
