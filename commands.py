from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from database import check_or_add_user
import re

# Utility to generate welcome message
def get_welcome_message(user_first_name, is_new_user):
    if is_new_user:
        return (f"Welcome {user_first_name}! I'm here to share daily inspiration and help you stay motivated, strong, and peaceful.\n\n"
                "- /start: Start interacting with me!\n"
                "- /set_daily: Schedule daily messages at a time that works for you.\n"
                "- /stop_daily: Stop receiving messages.\n"
                "- /feedback: Share your feedback anytime!\n"
                "Choose an option from the menu below to receive a message.")
    else:
        return (f"Welcome back, {user_first_name}!\n"
                "Just a reminder:\n"
                "- /set_daily: Schedule daily messages.\n"
                "- /stop_daily: Stop messages.\n"
                "- /feedback: Share feedback.\n"
                "Choose an option from the menu below.")

# Start command
async def send_welcome_message(update, context):
    user_id = update.message.from_user.id
    user_first_name = update.message.from_user.first_name

    is_new_user = not check_or_add_user(user_id, user_first_name)
    welcome_message = get_welcome_message(user_first_name, is_new_user)

    await update.message.reply_text(welcome_message)
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

# Set up daily messages with time validation
async def set_daily_message(update, context):
    time_format = re.compile(r'^\d{2}:\d{2}$')
    chat_id = update.message.chat_id
    user_time = update.message.text.strip()

    if time_format.match(user_time):
        await update.message.reply_text(f"Your daily message is set for {user_time}.")
    else:
        await update.message.reply_text("Please provide time in HH:MM format (24-hour clock).")

# Stop daily messages
async def stop_daily_message(update, context):
    current_jobs = context.job_queue.get_jobs_by_name(str(update.message.chat_id))
    for job in current_jobs:
        job.schedule_removal()
    await update.message.reply_text("Daily messages stopped.")

# Feedback prompt
async def feedback_prompt(update, context):
    await update.message.reply_text("What did you think of today's message? Did it help?")
