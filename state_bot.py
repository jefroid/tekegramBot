import asyncio

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from config import TOKEN

from aiogram import Bot, Dispatcher, executor, types

from keyboards import choose_chat_type_keyboard


bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

users_id = []
pairPlenty = set()
pairs = {}


@dp.message_handler(commands=['start'], state='*')
async def start_handler(message: types.Message, state: FSMContext):
    await message.answer("Привет, как тебя зовут?")
    await state.set_state("name")


@dp.message_handler(state='name')
async def name_handler(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({"name": name})
    await state.set_state("age")
    await message.answer(f"{name}, введи свой возраст")


@dp.message_handler(state='age')
async def age_handler(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(f"{user_data['name']}, "
                         "если хочешь присоединиться к групповому чату жми 'групповой чат', "
                         "если хотите присоединиться к анонимному чату один на один нажми 'чат 1 на 1'", reply_markup=
                         choose_chat_type_keyboard)
    await state.set_state("choosing")


@dp.message_handler(state='choosing')
async def choose_chat(message: types.Message, state: FSMContext):
    if message.text.lower() == 'групповой чат':
        await state.set_state("groupChatting")
        if message.from_user.id not in users_id:
            users_id.append(message.from_user.id)
        await message.answer("Добро пожаловать в групповой чат")
        await group_chat(message, state)
    elif message.text.lower() == 'чат 1 на 1':
        await state.set_state("soloChatting")
        await message.answer("Ищем собеседника для чата один на один...")
        await solo_chat(message, state)


@dp.message_handler(state='groupChatting')
async def group_chat(message: types.Message, state: FSMContext):
    sent = []
    user_data = await state.get_data()
    for i in range(len(users_id)):
        if message.from_user.id != users_id[i] and message.from_user.id not in pairPlenty and str(message.from_user.id) not in pairs.values():
            sent.append(bot.send_message(users_id[i], f"{user_data['name']} говорит: {message.text}"))
    await asyncio.gather(*sent)


@dp.message_handler(state='soloChatting')
async def solo_chat(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    pairPlenty.add(user_id)
    if len(pairPlenty) >= 2:
        pairPlenty.remove(user_id)
        another_user = pairPlenty.pop()
        pairs[user_id] = another_user
        pairs[another_user] = user_id
        await state.set_state("inChatting")
        another_user_state = dp.current_state(chat=pairs[user_id],
                                              user=pairs[user_id])
        await another_user_state.set_state('inChatting')

        await bot.send_message(chat_id=user_id, text='Вы начали общаться')
        await bot.send_message(chat_id=pairs[user_id], text='Вы начали общаться')


@dp.message_handler(state='inChatting')
async def in_chat(message: types.Message, state: FSMContext):
    await bot.send_message(pairs[message.from_user.id], message.text)


executor.start_polling(dp, skip_updates=True)
