import os
import logging
from telegram import Bot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
INVITE_LINK = os.environ.get("INVITE_LINK")
TARGET_USER_ID = os.environ.get("TARGET_USER_ID")  # new input

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if not BOT_TOKEN or not INVITE_LINK or not TARGET_USER_ID:
    logger.error("BOT_TOKEN, INVITE_LINK, or TARGET_USER_ID not set.")
    exit(1)

try:
    user_id = int(TARGET_USER_ID)
except ValueError:
    logger.error("TARGET_USER_ID must be an integer")
    exit(1)

bot = Bot(token=BOT_TOKEN)

try:
    bot.send_message(chat_id=user_id, text=f"Hello! Join our group here:\n{INVITE_LINK}")
    logger.info(f"✅ Invite sent to user {user_id}")
except Exception as e:
    logger.error(f"❌ Failed to send invite: {e}")
