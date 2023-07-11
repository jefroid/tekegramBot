from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

b1 = KeyboardButton('чат 1 на 1')
b2 = KeyboardButton('групповой чат')
start_button = KeyboardButton('старт')
question1_button1 = KeyboardButton('5')
question1_button2 = KeyboardButton('4')
question2_button1 = KeyboardButton('Медвежья')
question2_button2 = KeyboardButton('Кошачья')
question3_button1 = KeyboardButton('jefroid')
question3_button2 = KeyboardButton('GL1n')


question1 = ReplyKeyboardMarkup(resize_keyboard=True).insert(question1_button1).insert(question1_button2)
question2 = ReplyKeyboardMarkup(resize_keyboard=True).insert(question2_button1).insert(question2_button2)
question3 = ReplyKeyboardMarkup(resize_keyboard=True).insert(question3_button1).insert(question3_button2)
start = ReplyKeyboardMarkup(resize_keyboard=True).insert(start_button)
choose_chat_type_keyboard = ReplyKeyboardMarkup(resize_keyboard=True).insert(b1).insert(b2)
