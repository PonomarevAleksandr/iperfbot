from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_format_keyboard():
    """
    Создаёт клавиатуру для выбора формата вывода.
    """
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1. График 📈"), KeyboardButton(text="2. Текст 📃")],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
