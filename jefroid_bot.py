from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types

import requests
import asyncio

url = 'https://api.thecatapi.com/v1/images/search'


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

users_id = []

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    """Ловец (обработчик сообщений)"""
    await message.answer('Добро пожаловать в тестового бота')
    if message.from_user['id'] not in users_id:
        users_id.append(message.from_user['id'])


@dp.message_handler(commands=['send_cat'])
async def send_cat(message: types.Message):
    """Отправдение кота"""

    response = requests.get(url).json()
    Url = response[0]['url']

    await message.answer_photo(Url)


@dp.message_handler()
async def reply(message: types.Message):
    sendable = []
    for i in range(len(users_id)):
        if message.from_id != users_id[i]:
            sendable.append(bot.send_message(users_id[i], message['text']))
    await asyncio.gather(*sendable)


executor.start_polling(dp, skip_updates=True)
