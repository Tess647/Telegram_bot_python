# Self-Healing Telegram Bot

This is a **Self-Healing Telegram Bot** designed to uplift users' spirits by sending motivational, peaceful, and strength-filled messages. It also supports daily scheduled messages, user feedback collection, and category-based random message generation using inline buttons.

## Features

- **Personalized Welcome Message**: Users are greeted differently based on whether they are new or returning.
- **Message Categories**: Users can select from categories such as *Strength*, *Motivation*, and *Peace* to receive uplifting messages.
- **Daily Scheduled Messages**: Users can schedule daily messages at their preferred time.
- **User Feedback**: Users can provide feedback on the bot's messages.
- **Persistent Data**: MongoDB is used to store user data and feedback.
  
## Tech Stack

- **Python**: Core language for building the bot.
- **python-telegram-bot**: A wrapper for the Telegram Bot API.
- **MongoDB**: A NoSQL database to store user information and feedback.
- **python-dotenv**: For managing environment variables securely.
- **JobQueue**: For scheduling daily messages.

## Project Structure

```bash
Telegram_bot/
│
├── main.py               # Main entry point for running the bot
├── handlers.py           # Set up and define command and callback handlers
├── commands.py           # Define bot command functions
├── callbacks.py          # Define callback functions for button interactions
├── database.py           # Handle MongoDB connections and operations
├── messages.py           # Organize and manage message categories
├── utils/
│   └── error_handler.py  # Handle errors and exceptions in the bot
├── .env                  # Store environment variables (such as bot token, MongoDB URI)
└── requirements.txt      # List of dependencies
```

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/telegram-self-healing-bot.git
   cd telegram-self-healing-bot
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use: venv\Scripts\activate
   ```

3. **Install the Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add your environment variables:
   ```
   TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   MONGO_URI=your-mongodb-connection-string
   ```

5. **Run the Bot**:
   ```bash
   python main.py
   ```

## Usage

### Commands

- **`/start`**: Starts the bot and sends a personalized greeting.
- **`/set_daily`**: Allows the user to schedule a daily inspirational message at a fixed time.
- **`/stop_daily`**: Stops daily messages from being sent.
- **`/feedback`**: Prompts the user to provide feedback on the bot.

### Inline Buttons

- Users can interact with inline buttons to choose a message category:
  - *Strength 💪*
  - *Motivation ✨*
  - *Peace ☮️*
  - *Give Feedback*

### Scheduling Daily Messages

After running the `/set_daily` command, the bot will ask the user to provide a time in `HH:MM` format. Once set, the bot will send a random inspirational message from a selected category at the scheduled time every day.

### Feedback

Users can provide feedback via text after interacting with the "Give Feedback" button or running the `/feedback` command.

## Contributing

Contributions are welcome! If you'd like to add a feature or fix a bug, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request.

## Future Improvements

- Support for more message categories.
- Localization for different languages.
- Ability to let users customize their daily message content.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library for making Telegram Bot development easy.
- [MongoDB](https://www.mongodb.com/) for handling user data and feedback.
