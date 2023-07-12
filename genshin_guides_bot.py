from config import TOKEN

from aiogram import Dispatcher, executor, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

import genshin_buttons

import text_guides

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Добро пожаловать в бота с гайдами по игре Genshin Impact! Выбери одну из опций',
                         reply_markup=genshin_buttons.options)
    await state.set_state('choose_option')


@dp.message_handler(state='choose_option')
async def choose_option(message: types.Message, state: FSMContext, is_back: bool = False):
    if message.text == 'Гайды' or is_back == True:
        await state.set_state('guides')
        await message.answer('Выбери на какого персонажа хочешь получить гайд',
                             reply_markup=genshin_buttons.character)


@dp.message_handler(state='guides')
async def send_guide(message: types.Message, state: FSMContext):
    if message.text == 'Чжун Ли':
        await message.answer(text_guides.zhongli)
        await message.answer_photo('https://yvid.ru/wp-content/uploads/2020/12/Vozvyshenie-Chzhun-Li.jpg',
                                   reply_markup=genshin_buttons.back)
        await state.set_state('get_back')


@dp.message_handler(state='get_back')
async def backward(message: types.Message, state: FSMContext):
    if message.text == 'В начало':
        await state.set_state('*')
        await start_handler(message, state)
    elif message.text == 'Выбрать гайд на другого персонажа':
        await state.set_state('choose_option')
        await choose_option(message, state, True)


executor.start_polling(dp, skip_updates=True)
