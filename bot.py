import requests
import os

BOT_TOKEN = "7058552962:AAEwAT9YwebPWDtjZMVaZXpjaX8Qhtn2evY"
CHAT_ID = "7058552962"  # یا @channelusername

TARGET_URL = "https://rollercoin.com/game"

with open("proxy.txt", "r") as f:
    proxy = f.read().strip()

proxies = {
    "http": proxy,
    "https": proxy
}

try:
    response = requests.get(TARGET_URL, proxies=proxies, timeout=15)
    text = response.text[:1000]
except Exception as e:
    text = f"❌ خطا در اتصال به سایت:\n{str(e)}"

send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": text
}

try:
    requests.post(send_url, data=payload)
except Exception as e:
    print("❌ خطا در ارسال پیام تلگرام:", e)