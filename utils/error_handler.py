import logging

async def error_handler(update, context):
    logging.error(msg="Exception while handling an update:", exc_info=context.error)
    try:
        await update.message.reply_text("Oops, something went wrong! Please try again later.")
    except Exception:
        pass
