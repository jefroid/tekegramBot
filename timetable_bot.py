from config import TOKEN

from aiogram import Dispatcher, executor, types, Bot
from aiogram.types import Message

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import timetable_keyboard

bot = Bot(TOKEN)
dp = Dispatcher(bot)

main_menu = {'text': 'Узнать расписание автобуса', 'reply_markup': timetable_keyboard.busses_keyboards}


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer(**main_menu)


@dp.callback_query_handler(lambda c: c.data == 'bus108', state='*')
async def process_bus_108(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.edit_reply_markup(timetable_keyboard.back_keyboard)


@dp.callback_query_handler(lambda c: c.data == 'bus203', state='*')
async def process_bus_203(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.edit_text('Автобус 106 сейчас не работает',
                                           reply_markup=timetable_keyboard.back_keyboard)


@dp.callback_query_handler(lambda c: c.data == 'back', state='*')
async def process_back(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await callback_query.message.edit_text(**main_menu)

executor.start_polling(dp, skip_updates=True)
