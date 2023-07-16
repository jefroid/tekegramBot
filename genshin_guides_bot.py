from config import TOKEN

from aiogram import Dispatcher, executor, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

import genshin_buttons

import guides

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer('Добро пожаловать в бота с гайдами по игре Genshin Impact! Выбери одну из опций',
                         reply_markup=genshin_buttons.options)
    await state.set_state('choose_option')


@dp.message_handler(state='choose_option')
async def choose_option(message: types.Message, state: FSMContext, is_back: bool = False):
    if message.text == 'Гайды на персонажей' or is_back is True:
        await state.set_state('guides')
        await message.answer('Выбери на какого персонажа хочешь получить гайд',
                             reply_markup=genshin_buttons.character)
    elif message.text == 'Гайд на фарм артефактов':
        name = 'Гайд на фарм артефактов'
        await state.update_data({"name": name})
        await state.set_state('get_back')
        await message.answer(guides.farm_guide, reply_markup=genshin_buttons.in_start)


@dp.message_handler(state='guides')
async def send_guide(message: types.Message, state: FSMContext):
    name = message.text
    await message.answer(guides.text_guides_dict[name])
    await message.answer_photo(guides.character_resources[name],
                               reply_markup=genshin_buttons.back)
    await state.update_data({"name": name})
    await state.set_state('get_back')


@dp.message_handler(state='get_back')
async def backward(message: types.Message, state: FSMContext):
    if message.text == 'Хочу более подробный гайд💬':
        name = (await state.get_data())['name']
        await message.answer(guides.video_guides[name])
    elif message.text == 'В начало↩':
        await state.set_state('*')
        await start_handler(message, state)
    elif message.text == 'Выбрать гайд на другого персонажа🆕':
        await state.set_state('choose_option')
        await choose_option(message, state, True)
    elif message.text == 'Описание сленга👅':
        await message.answer(guides.slang)


executor.start_polling(dp, skip_updates=True)
