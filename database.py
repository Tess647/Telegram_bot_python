import datetime
from pymongo import MongoClient
import os
import logging

# Get MongoDB connection string from environment
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client['telegram_bot_db']
users_collection = db['users']

# Check or add user
def check_or_add_user(user_id, user_first_name):
    try:
        user = users_collection.find_one({"user_id": user_id})
        if user is None:
            users_collection.insert_one({"user_id": user_id, "first_name": user_first_name})
            return False
        return True
    except Exception as e:
        logging.error(f"Error in check_or_add_user: {e}")
        return False

# Store user feedback
def store_user_feedback(user_id, feedback_type, message):
    feedback_collection = db['feedback']
    try:
        feedback_collection.insert_one({
            'user_id': user_id,
            'feedback_type': feedback_type,
            'message': message,
            'timestamp': datetime.datetime.now()
        })
    except Exception as e:
        logging.error(f"Error storing feedback: {e}")
