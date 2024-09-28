import logging
import random
import datetime
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, JobQueue

# Logging for debugging purposes
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Organize messages into categories
messages = {
    'strength': [
        "You are stronger than you think!",
        "Keep going; you’re doing amazing.",
        "Every storm runs out of rain."
    ],
    'motivation': [
        "Believe in yourself and your abilities.",
        "Every day is a fresh start.",
        "Dream it, believe it, achieve it!"
    ],
    'peace': [
        "Peace begins with a smile.",
        "Calm mind brings inner strength.",
        "Let go of what you cannot change."
    ]
}

# Start command with personalized greeting
async def send_welcome_message(update: Update, context) -> None:
    user_first_name = update.message.from_user.first_name
    await update.message.reply_text(f"Welcome {user_first_name}! I'm here to share healing and uplifting messages with you.")

# Send menu with categories
async def send_message_menu(update: Update, context) -> None:
    keyboard = [
        [InlineKeyboardButton("Strength", callback_data='strength')],
        [InlineKeyboardButton("Motivation", callback_data='motivation')],
        [InlineKeyboardButton("Peace", callback_data='peace')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose a message category:", reply_markup=reply_markup)

# Handle button clicks to send random message from chosen category
async def handle_message_type(update: Update, context) -> None:
    query = update.callback_query
    category = query.data
    if category in messages:
        message = random.choice(messages[category])
        user_first_name = query.from_user.first_name
        await query.message.reply_text(f"{user_first_name}, {message}")
    await query.answer()

# Set up a daily message for users
async def daily_message(context):
    chat_id = context.job.chat_id
    category = random.choice(list(messages.keys()))
    message = random.choice(messages[category])
    await context.bot.send_message(chat_id, f"Here's your daily message: {message}")

# Command to set up daily messages at a fixed time (e.g., 9 AM)
async def set_daily_message(update: Update, context) -> None:
    chat_id = update.message.chat_id
    # Schedule the job for 9 AM every day
    time = datetime.time(hour=9, minute=0, second=0)
    context.job_queue.run_daily(daily_message, time=time, chat_id=chat_id)
    await update.message.reply_text("You will receive a daily message at 9 AM!")

# Command to stop daily messages
async def stop_daily_message(update: Update, context) -> None:
    context.job_queue.stop()
    await update.message.reply_text("Daily messages stopped.")

# Error handling
async def error_handler(update: Update, context) -> None:
    logging.error(msg="Exception while handling an update:", exc_info=context.error)
    try:
        await update.message.reply_text("Oops, something went wrong! Please try again later.")
    except Exception:
        pass

def main():
    """
    Handles the initial launch of the program (entry point).
    """
    token = '7615807723:AAE-i7bTiUjZ91EMoNvHoNwk8SsXm77zIkk'
    application = Application.builder().token(token).concurrent_updates(True).build()

    # Command handlers
    application.add_handler(CommandHandler("start", send_welcome_message))
    application.add_handler(CommandHandler("hello", send_welcome_message))
    
    # Message command to display the button menu
    application.add_handler(CommandHandler('message', send_message_menu))
    
    # Inline button handler
    application.add_handler(CallbackQueryHandler(handle_message_type))

    # Commands for daily messages
    application.add_handler(CommandHandler('set_daily', set_daily_message))
    application.add_handler(CommandHandler('stop_daily', stop_daily_message))

    # Error handler
    application.add_error_handler(error_handler)

    print("Telegram Bot started!", flush=True)
    application.run_polling()

if __name__ == '__main__':
    main()
