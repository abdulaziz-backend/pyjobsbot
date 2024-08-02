from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👨‍💼 Xodim kerak"),
         KeyboardButton(text="👨‍💻 Ish joyi kerak")],
        [KeyboardButton(text="🧑‍🏫 Ustoz kerak")]
    ],
    resize_keyboard=True
)

remove_keyboard = ReplyKeyboardMarkup(
    keyboard=[],
    resize_keyboard=True
)
