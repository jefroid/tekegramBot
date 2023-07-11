from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

guides_button = KeyboardButton('Гайды')

in_start_button = KeyboardButton('В начало')
in_character_guides_button = KeyboardButton('Выбрать гайд на другого персонажа')

zhongli_button = KeyboardButton('Чжун Ли')

options = ReplyKeyboardMarkup(resize_keyboard=True).insert(guides_button)
character = ReplyKeyboardMarkup(resize_keyboard=True).insert(zhongli_button)
back = ReplyKeyboardMarkup(resize_keyboard=True).insert(in_start_button).add(in_character_guides_button)
