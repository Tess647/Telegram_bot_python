import random
from messages import messages, send_random_message_in_category
from database import store_user_feedback

# Handle button clicks
async def handle_message_type(update, context):
    query = update.callback_query
    category = query.data

    if category == 'feedback':
        await query.message.reply_text("Please type your feedback. How can I improve?")
        return

    if category in messages:
        await send_random_message_in_category(query, context, category)

    await query.answer()

# Handle user feedback
async def handle_feedback(update, context):
    user_id = update.message.from_user.id
    feedback = update.message.text

    store_user_feedback(user_id, "user_feedback", feedback)
    await update.message.reply_text("Thank you for your feedback!")
import random
from messages import messages
from database import store_user_feedback

# Handle button clicks
async def handle_message_type(update, context):
    query = update.callback_query
    category = query.data

    if category == 'feedback':
        await query.message.reply_text("Please type your feedback. How can I improve?")
        return

    if category in messages:
        await send_random_message_in_category(query, context, category)

    await query.answer()

# Handle user feedback
async def handle_feedback(update, context):
    user_id = update.message.from_user.id
    feedback = update.message.text

    store_user_feedback(user_id, "user_feedback", feedback)
    await update.message.reply_text("Thank you for your feedback!")
import random
from messages import messages
from database import store_user_feedback

# Handle button clicks
async def handle_message_type(update, context):
    query = update.callback_query
    category = query.data

    if category == 'feedback':
        await query.message.reply_text("Please type your feedback. How can I improve?")
        return

    if category in messages:
        await send_random_message_in_category(query, context, category)

    await query.answer()

# Handle user feedback
async def handle_feedback(update, context):
    user_id = update.message.from_user.id
    feedback = update.message.text

    store_user_feedback(user_id, "user_feedback", feedback)
    await update.message.reply_text("Thank you for your feedback!")
