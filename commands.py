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
        # Brief reminder for existing users
        reminder_message = (
            f"Welcome back, {user_first_name}!\n"
            "Just a quick reminder of what you can do:\n"
            "- /set_daily: Schedule a daily message to keep yourself motivated.\n"
            "- /stop_daily: Stop receiving daily messages whenever you like.\n"
            "- /feedback: Share your feedback with me anytime!\n\n"
            "Feel free to choose an option from the menu below!"
        )
        await update.message.reply_text(reminder_message)
    else:
        # Brief intro for new users
        intro_message = (
            f"Welcome {user_first_name}! I'm here to share daily inspiration and help you stay motivated, strong, and peaceful.\n\n"
            "Here's a quick guide to get started:\n"
            "- /start: Start interacting with me, and I'll greet you personally!\n"
            "- /set_daily: Schedule a daily message to inspire you at a time that works best for you.\n"
            "- /stop_daily: Stop receiving daily messages whenever you need a break.\n"
            "- /feedback: Share your thoughts and feedback with me!\n\n"
            "Now, go ahead and choose an option from the menu below to receive a motivational message!"
        )
        await update.message.reply_text(intro_message)
    
    # Show the menu after the message
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
