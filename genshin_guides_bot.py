from config import TOKEN

from aiogram import Dispatcher, executor, types, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

import genshin_buttons

import text_guides

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

video_guides = {'Гайд на фарм артефактов': 'https://www.youtube.com/watch?v=ghbFFpQ_-XI',
                'Чжун Ли⏳': 'часть 1: https://www.youtube.com/watch?v=725ikw9karY \n'
                            'часть 2: https://www.youtube.com/watch?v=vbIqtzt-wk8',
                'Кадзуха🌪': 'https://www.youtube.com/watch?v=HSgp20-AuyM',
                'Райден⚡': 'гайд на персонажа: https://www.youtube.com/watch?v=LF0LiiNBcWk \n'
                           'гайд на Raiden National: https://www.youtube.com/watch?v=oLkyhzdfENU',
                'Аяка❄': 'https://www.youtube.com/watch?v=FBGEOw3NGOQ',
                'Ху Тао👻': 'https://www.youtube.com/watch?v=X2mJItYYFEI',
                'Гань Юй🏹': 'https://www.youtube.com/watch?v=I_fFvrjyjJw',
                'Беннет🔥': 'https://www.youtube.com/watch?v=AvfHFcz4vUo',
                'Сян Лин🥩': 'https://www.youtube.com/watch?v=9k5v1ZfVewU',
                'Сяо👹': 'гайд: https://www.youtube.com/watch?v=U_ow8r_vuzs&t=2s \n'
                        'дополнение: https://www.youtube.com/watch?v=s7KunA5UbMg'}


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
        await message.answer(text_guides.farm_guide, reply_markup=genshin_buttons.in_start)


@dp.message_handler(state='guides')
async def send_guide(message: types.Message, state: FSMContext):
    name = message.text
    if message.text == 'Чжун Ли⏳':
        await message.answer(text_guides.zhongli)
        await message.answer_photo('https://yvid.ru/wp-content/uploads/2020/12/Vozvyshenie-Chzhun-Li.jpg',
                                   reply_markup=genshin_buttons.back)
    elif message.text == 'Кадзуха🌪':
        await message.answer(text_guides.kazuha)
        await message.answer_photo('https://avatars.dzeninfra.ru/get-zen_doc/3964212/pub_60bb3'
                                   '2a5bbd5974178426208_60db6c63e09a980274445814/scale_1200',
                                   reply_markup=genshin_buttons.back)
    elif message.text == 'Райден⚡':
        await message.answer(text_guides.raiden)
        await message.answer_photo('https://yvid.ru/wp-content/uploads/2020/12/Vozvyshenie-Segun-Rajden.jpg',
                                   reply_markup=genshin_buttons.back)
    elif message.text == 'Аяка❄':
        await message.answer(text_guides.ayaka)
        await message.answer_photo('https://avatars.dzeninfra.ru/get-zen_doc/108399/pub_60f1942d'
                                   'cf9db26ddaa80079_60f890cb0c14cd3ca97173a6/scale_1200',
                                   reply_markup=genshin_buttons.back)
    elif message.text == 'Ху Тао👻':
        await message.answer(text_guides.hutao)
        await message.answer_photo('https://genshin.ru/wp-content/uploads/2023/02/prokachka_hu_tao.jpg',
                                   reply_markup=genshin_buttons.back)
    elif message.text == 'Гань Юй🏹':
        await message.answer(text_guides.ganyu)
        await message.answer_photo('https://avatars.dzeninfra.ru/get-zen_doc/4935831/pub_5ffcbcf5aeef3c7829ff1'
                                   'd1f_60deced3526c5a7dabffa516/scale_1200',
                                   reply_markup=genshin_buttons.back)
    elif message.text == 'Сян Лин🥩':
        await message.answer(text_guides.xiangling)
        await message.answer_photo('https://avatars.dzeninfra.ru/get-zen_doc/168601/pub_6001eb08d0d4386c9fd167c0_6130a'
                                   'e03ef7362581490eef2/scale_1200',
                                   reply_markup=genshin_buttons.back)
    elif message.text == 'Беннет🔥':
        await message.answer(text_guides.bennett)
        await message.answer_photo('https://genshindb.ru/wp-content/uploads/2021/04/bennet-res.jpg',
                                   reply_markup=genshin_buttons.back)
    elif message.text == 'Сяо👹':
        await message.answer(text_guides.xiao)
        await message.answer_photo('https://genshinhelper.ru/wp-content/uploads/2021/07/%D0%9C%D0%B0%D1%82%D0%B5%D1%8'
                                   '0%D0%B8%D0%B0%D0%BB%D1%8B-%D0%B4%D0%BB%D1%8F-%D0%B2%D0%BE%D0%B7%D0%B2%D1%8B%D1%'
                                   '88%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D1%8F%D0%BE.jpg',
                                   reply_markup=genshin_buttons.back)
    await state.update_data({"name": name})
    await state.set_state('get_back')


@dp.message_handler(state='get_back')
async def backward(message: types.Message, state: FSMContext):
    if message.text == 'Хочу более подробный гайд💬':
        name = (await state.get_data())['name']
        await message.answer(video_guides[name])
    elif message.text == 'В начало↩':
        await state.set_state('*')
        await start_handler(message, state)
    elif message.text == 'Выбрать гайд на другого персонажа🆕':
        await state.set_state('choose_option')
        await choose_option(message, state, True)
    elif message.text == 'Описание сленга👅':
        await message.answer(text_guides.slang)


executor.start_polling(dp, skip_updates=True)
