import settings

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)

from settings import TOKEN
from callbacks import start


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # command handlers
    dispatcher.add_handler(
        handler=CommandHandler(command=["start", "boshlash"], callback=start)
    )

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
