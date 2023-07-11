from config import TOKEN

from aiogram import Dispatcher, executor, types, Bot

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from cliker_buttons import click_keyboard, double_click_keyboard

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: types.Message, state: FSMContext):
    n = 0
    await state.update_data({'n': n})
    await message.answer("Добро пожаловать в бота-кликера, жми на кнопку что-бы начать!", reply_markup=click_keyboard)


@dp.callback_query_handler(lambda c, b: c.data == 'click' or b.data == 'double_click', state='*')
async def click_click(callback_query: types.CallbackQuery, state: FSMContext):
    n = await state.get_data()['n']
    await callback_query.answer()
    if n <= 50:
        n += 1
        await callback_query.message.edit_text(f'Всего кликов: {n}', reply_markup=click_keyboard)
        await state.update_data({'n': n})
    else:
        if callback_query.data == 'click':
            n += 1
            await callback_query.message.edit_text(f'Всего кликов: {n}', reply_markup=double_click_keyboard)
            await state.update_data({'n': n})
        elif callback_query.data == 'double_click':
            n += 2
            await callback_query.message.edit_text(f'Всего кликов: {n}', reply_markup=double_click_keyboard)
            await state.update_data({'n': n})

executor.start_polling(dp, skip_updates=True)
