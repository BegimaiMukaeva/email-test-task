import requests

TOKEN = "TELEGRAM_BOT_TOKEN"
CHAT_ID = 123456789

with open("message.txt", "r", encoding="utf-8") as f:
    text = f.read()

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": text
})

print("Message sent, status:", response.status_code)
