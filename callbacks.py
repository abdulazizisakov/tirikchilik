from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text="Salom xush kelibsiz.",
    )
