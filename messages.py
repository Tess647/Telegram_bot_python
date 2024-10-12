import random

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
        "A calm mind brings inner strength.",
        "Let go of what you cannot change."
    ]
}

# Send a random message from a specific category
async def send_random_message_in_category(update, context, category):
    message = random.choice(messages[category])
    
    # Determine the user's first name from the update
    user_first_name = update.message.from_user.first_name if update.message else update.callback_query.from_user.first_name
    
    # Send the message depending on whether it's a normal message or a callback query
    if update.message:
        await update.message.reply_text(f"{user_first_name}, {message}")
    elif update.callback_query:
        await update.callback_query.message.reply_text(f"{user_first_name}, {message}")

