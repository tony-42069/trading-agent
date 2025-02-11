"""
Simple Telegram bot for crypto trading alerts.
"""
import os
import logging
from datetime import datetime
import telebot
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get bot token from environment
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN found in .env file")

# Initialize bot
bot = telebot.TeleBot(TOKEN)

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    """Handle /start command."""
    welcome_text = f"""
👋 Hi {message.from_user.first_name}!

Welcome to TraderTony Bot. I'm here to help you monitor crypto trading activities.

Available commands:
/start - Show this welcome message
/help - Show available commands
/status - Check bot status
"""
    bot.reply_to(message, welcome_text)
    logger.info(f"User {message.from_user.id} started the bot")

@bot.message_handler(commands=['help'])
def help_command(message):
    """Handle /help command."""
    help_text = """
Available Commands:
/start - Start the bot
/help - Show this help message
/status - Check bot status

More features coming soon!
"""
    bot.reply_to(message, help_text)
    logger.info(f"User {message.from_user.id} requested help")

@bot.message_handler(commands=['status'])
def status(message):
    """Handle /status command."""
    status_text = f"""
Bot Status:
✅ Bot Online
✅ Commands Active

System Info:
• Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    bot.reply_to(message, status_text)
    logger.info(f"User {message.from_user.id} checked status")

def main():
    """Start the bot."""
    try:
        logger.info("Starting bot...")
        bot.infinity_polling()
    except Exception as e:
        logger.error(f"Bot error: {e}")
        raise

if __name__ == '__main__':
    main()
