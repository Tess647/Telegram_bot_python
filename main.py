import os
import logging
from telegram.ext import Application
from flask import Flask, request
from dotenv import load_dotenv
from handlers import setup_handlers
from utils.error_handler import error_handler
from telegram import Update

# Load environment variables
load_dotenv()

# Get the bot token from environment variables
token = os.getenv('TELEGRAM_BOT_TOKEN')
webhook_url = os.getenv('WEBHOOK_URL')  # Add this to your .env file with your Heroku app URL

# Logging for debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Initialize Flask app for handling webhooks
app = Flask(__name__)

# Define the application for the bot
application = Application.builder().token(token).concurrent_updates(True).build()

# Set up handlers
setup_handlers(application)

# Error handler
application.add_error_handler(error_handler)

@app.route(f'/{token}', methods=['POST'])
async def webhook():
    """Handle incoming webhook updates."""
    update = Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return "OK"

async def set_webhook():
    """Set the webhook for the bot."""
    await application.bot.set_webhook(webhook_url + f'/{token}')

def main():
    print("Telegram Bot started with Webhook!", flush=True)
    
    # Set the webhook
    import asyncio
    asyncio.run(set_webhook())
    
    # Run the Flask app (web server) on Heroku's provided port
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    main()
