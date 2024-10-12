import random
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from database import check_or_add_user
from messages import messages, send_random_message_in_category

# Start command
async def send_welcome_message(update, context):
    user_id = update.message.from_user.id
    user_first_name = update.message.from_user.first_name

    # Check if user exists
    if check_or_add_user(user_id, user_first_name):
        # Greet returning user
        await update.message.reply_text(f"Welcome back, {user_first_name}! How have you been?")
    else:
        # Greet new user
        await update.message.reply_text(f"Welcome {user_first_name}! I'm here to inspire you every day.")

        # Option 1: Send only one random message from a category
        category = random.choice(list(messages.keys()))  # Select a random category
        await send_random_message_in_category(update, context, category)
    
    # Show the message category selection menu
    await send_message_menu(update, context)

# Send menu with categories
async def send_message_menu(update, context):
    keyboard = [
        [InlineKeyboardButton("Strength 💪", callback_data='strength')],
        [InlineKeyboardButton("Motivation ✨", callback_data='motivation')],
        [InlineKeyboardButton("Peace ☮️", callback_data='peace')],
        [InlineKeyboardButton("Give Feedback", callback_data='feedback')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("What do you need today?", reply_markup=reply_markup)

# Set up daily messages
async def set_daily_message(update, context):
    chat_id = update.message.chat_id
    await update.message.reply_text("At what time would you like to receive your daily message? (HH:MM in 24-hour format)")

# Stop daily messages
async def stop_daily_message(update, context):
    current_jobs = context.job_queue.get_jobs_by_name(str(update.message.chat_id))
    for job in current_jobs:
        job.schedule_removal()
    await update.message.reply_text("Daily messages stopped.")

# Feedback prompt
async def feedback_prompt(update, context):
    await update.message.reply_text("What did you think of today's message? Did it help?")
