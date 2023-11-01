import re
import asyncio
import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from pathlib import Path

from ..constants import DATA_DIR
from ..common import dp
from ..models import db
from ._utils import kb, texts, states


class UserStates(StatesGroup):
    ask_date = State()
    ask_city = State()


codes = list(range(124561, 463281))


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message, state: FSMContext):
    await db.registrate_if_not_exists(message.from_user.id)
    await db.update_stage(message.from_user.id, 'stage_1')
    await message.answer(texts.welcome, reply_markup=kb.start)


@dp.message_handler(lambda message: message.text == "🌙Хочу прогноз", state='*')
async def start_choosing_cards(message: types.Message, state: FSMContext):
    await db.update_stage(message.from_user.id, 'stage_2')
    await message.answer(texts.ask_date)
    await state.set_state(UserStates.ask_date.state)


@dp.message_handler(state=UserStates.ask_date)
async def get_user_date(message: types.Message, state: FSMContext):
    if re.fullmatch(r'\d{1,2}\.\d{1,2}\.\d{4}', message.text):
        day, month, year = message.text.split('.')
        if 0 < int(day) < 32 and 0 < int(month) < 13 and int(year) < 2023:
            await db.update_stage(message.from_user.id, 'stage_3')
            await message.answer(texts.ask_city)
            await state.set_state(UserStates.ask_city.state)
        else:
            await message.answer('Некорректная дата.\n🙏Для получения прогноза, пожалуйста, напишите дату рождения в форме дд.мм.гггг')
    else:
        await message.answer('Неверный формат.\n🙏Для получения прогноза, пожалуйста, напишите дату рождения в форме дд.мм.гггг')


@dp.message_handler(state=UserStates.ask_city)
async def choose_card(message: types.Message, state: FSMContext):
    await message.answer(texts.byte_message.substitute(random.choice(codes)), reply_markup=kb.to_autoanswer)