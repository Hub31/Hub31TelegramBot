
from flask import Flask, request
import requests

import os
BOT_TOKEN = os.environ.get('8012170017:AAHrZTw4tTJmZPJ818TFDV9ArnAqDGqOS38')
TELEGRAM_API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'

def send_message(chat_id, text):
    requests.post(TELEGRAM_API_URL, json={'chat_id': chat_id, 'text': text})

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    chat_id = data['message']['chat']['id']
    msg_text = data['message'].get('text', '')

    if msg_text.lower() in ['/start', 'hi', 'hello']:
        send_message(chat_id, "👑 Welcome to Hub31 AI Agent!\nWhat do you want to build today?\n1️⃣ Brand Kit\n2️⃣ AI Agent\n3️⃣ Both")
    elif '1' in msg_text:
        send_message(chat_id, "🔥 Great! Tell me your idea in one sentence.")
    elif '2' in msg_text:
        send_message(chat_id, "🤖 Cool! What part of your business do you want to automate?")
    elif '3' in msg_text:
        send_message(chat_id, "💥 Boss moves! Share your idea in one sentence and your WhatsApp number.")
    elif '+' in msg_text and msg_text.startswith('+254'):
        send_message(chat_id, "✅ Got your number! We'll reach out soon.\nMeanwhile: https://hub31.xyz")
    else:
        send_message(chat_id, "✨ Got it! Anything else you’d like to add?")

    return {'ok': True}
