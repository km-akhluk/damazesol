import os
import requests
import time
from telegram import Bot

TELEGRAM_TOKEN = os.environ.get("8087494289:AAFUUrnS8Rk7ysxTIlWCqCJTkJGXjORkyBo")
CHAT_ID = os.environ.get("1002733061886")
bot = Bot(token=TELEGRAM_TOKEN)

def check_dexscreener():
    url = "https://api.dexscreener.com/latest/dex/pairs/solana"
    data = requests.get(url).json()

    for pair in data["pairs"]:
        price_change = float(pair["priceChange"]["m5"])
        volume = float(pair["volume"]["h1"])
        
        if price_change > 10 and volume > 150000:
            token = pair["baseToken"]["symbol"]
            msg = f"🚨 Pump Alert: {token}\nPrice Change (5m): {price_change}%\nVolume (1h): ${volume:,}"
            bot.send_message(chat_id=CHAT_ID, text=msg)

while True:
    check_dexscreener()
    time.sleep(300)  # every 5 minutes
