import os
import logging
from telegram.ext import Application
from dotenv import load_dotenv
from handlers import setup_handlers
from utils.error_handler import error_handler

# Load environment variables
load_dotenv()

# Get the bot token from environment variables
token = os.getenv('TELEGRAM_BOT_TOKEN')

# Logging for debugging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main():
    application = Application.builder().token(token).concurrent_updates(True).build()

    # Set up handlers
    setup_handlers(application)

    # Error handler
    application.add_error_handler(error_handler)

    print("Telegram Bot started!", flush=True)
    application.run_polling()

if __name__ == '__main__':
    main()
