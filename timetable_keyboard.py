from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

button108 = InlineKeyboardButton('108', callback_data='bus108')
button203 = InlineKeyboardButton('203', callback_data='bus203')

busses_keyboards = InlineKeyboardMarkup().row(button108).row(button203)

button_back = InlineKeyboardButton('Вернуться назад', callback_data='back')

back_keyboard = InlineKeyboardMarkup().row(button_back)
