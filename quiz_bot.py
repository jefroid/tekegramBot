from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from keyboards import question1, question2, question3, start

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

right_answers = 0


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: types.Message, state: FSMContext):
    global right_answers
    right_answers = 0
    await message.answer('Добро пожаловать, если хотите пройти викторину нажмите "старт"', reply_markup=start)
    await state.set_state('question1')


@dp.message_handler(state='question1')
async def first_question(message: types.Message, state: FSMContext):
    global right_answers
    right_answers = 0
    await message.answer('Первый вопрос: Сколько колес у собаки?', reply_markup=question1)
    await state.set_state('question2')


@dp.message_handler(state='question2')
async def first_question(message: types.Message, state: FSMContext):
    global right_answers
    if message.text == '5':
        right_answers += 1
    await message.answer('Второй вопрос: Чья услуга никома не нужна?', reply_markup=question2)
    await state.set_state('question3')


@dp.message_handler(state='question3')
async def first_question(message: types.Message, state: FSMContext):
    global right_answers
    if message.text == 'Медвежья':
        right_answers += 1
    await message.answer('Третий вопрос: Самый лучший гайдер по Геншин Импакту?', reply_markup=question3)
    await state.set_state('results')


@dp.message_handler(state='results')
async def first_question(message: types.Message, state: FSMContext):
    global right_answers
    if message.text == 'GL1n':
        right_answers += 1
    await state.set_state('*')
    await message.answer(f'У тебя {right_answers} правильных ответ')


executor.start_polling(dp, skip_updates=True)
