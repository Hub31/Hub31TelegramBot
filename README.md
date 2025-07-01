# Hub31 Telegram Bot — Step-by-Step

1. Go to Telegram and open @BotFather.
2. Type /newbot and follow the prompts to create a bot.
3. Copy the token and replace it in `app.py` where it says YOUR_TELEGRAM_BOT_TOKEN.
4. Deploy the bot using Render.com:
   - Create a new Web Service
   - Connect this repo or upload files
   - Use Python 3
   - Start command: gunicorn app:app
5. Set the webhook URL:
   - Use this format: https://your-app-name.onrender.com/webhook
   - Send a GET request to: https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=<YOUR_WEBHOOK>
