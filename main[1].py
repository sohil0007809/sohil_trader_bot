import asyncio
import logging
import requests
from telegram import Bot
from telegram.constants import ParseMode
from telegram.error import TelegramError

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

bot = Bot(token=BOT_TOKEN)

API_URL = "https://draw.ar-lottery01.com/WinGo/WinGo_30S/GetHistoryIssuePage.json?ts=1751728621041"

logging.basicConfig(level=logging.INFO)

async def send_prediction():
    try:
        response = requests.get(API_URL)
        data = response.json()
        last_result = data["data"][0]["winNumber"]
        message = f"🎯 Prediction Result: <b>{last_result}</b>"
        await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=ParseMode.HTML)
    except TelegramError as e:
        logging.error(f"Telegram error: {e}")
    except Exception as e:
        logging.error(f"Error: {e}")

async def main():
    while True:
        await send_prediction()
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
