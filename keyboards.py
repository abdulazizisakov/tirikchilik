from telegram import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🔥 Mahsulotlar", web_app=WebAppInfo("https://google.com")
            ),
            KeyboardButton(text="📥Savat"),
        ],
        [KeyboardButton(text="💼 Hamkorlik"), KeyboardButton(text="ℹ️ Ma'lumot")],
        [KeyboardButton(text="🏠 Bosh menyu")],
    ]
)

info_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✍️ Izoh qoldirish")],
        [
            KeyboardButton(text="🚀 Yetkazib berish shartlari"),
            KeyboardButton(text="☎️ Kontaktlar"),
        ],
        [KeyboardButton(text="🏠 Bosh menyu")],
    ]
)


comments_keyboard = ReplyKeyboardMarkup(keyboard=[[]])
