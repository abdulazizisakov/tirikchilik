from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, ParseMode
from telegram.ext import CallbackContext

from messages import welcome_message, partnership, comments
from keyboards import main_keyboard, info_keyboard, comments_keyboard


def start(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text=welcome_message.format(name=update.effective_user.first_name),
        reply_markup=main_keyboard,
    )


def send_cart(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text="<b> Sizning savatingiz bo'sh </b>",
        parse_mode=ParseMode.HTML,
    )


def send_partnership(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(chat_id=update.message.chat.id, text=partnership)


def send_info(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id,
        text="Kerakli bo'limni tanlang ⬇️",
        reply_markup=info_keyboard,
    )


def send_comments(update: Update, context: CallbackContext) -> None:
    bot = context.bot

    bot.send_message(
        chat_id=update.message.chat.id, text=comments, reply_markup=comments_keyboard
    )
