from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, filters
from commands import send_welcome_message, set_daily_message, stop_daily_message, feedback_prompt
from callbacks import handle_message_type, handle_feedback

def setup_handlers(application):
    # Command handlers
    application.add_handler(CommandHandler("start", send_welcome_message))
    application.add_handler(CommandHandler("hello", send_welcome_message))
    application.add_handler(CommandHandler('set_daily', set_daily_message))
    application.add_handler(CommandHandler('stop_daily', stop_daily_message))
    application.add_handler(CommandHandler('feedback', feedback_prompt))
    
    # Inline button handler
    application.add_handler(CallbackQueryHandler(handle_message_type))

    # Feedback message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_feedback))
