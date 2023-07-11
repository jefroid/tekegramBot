from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

click_button = InlineKeyboardButton('CLICK!!!', callback_data='click')

double_click_button = InlineKeyboardButton('DOUBLE CLICK!!!!', callback_data='double_click')

click_keyboard = InlineKeyboardMarkup().row(click_button)
double_click_keyboard = InlineKeyboardMarkup().row(click_button).add(double_click_button)
