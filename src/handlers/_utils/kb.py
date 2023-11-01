import json

from itertools import islice
from aiogram import types


def _get_titles_from_kb(kb: types.ReplyKeyboardMarkup):
    json_kb = json.loads(kb.as_json())['keyboard']
    titles = []
    for row in json_kb:
        for btn in row:
            titles.append(btn['text'])
    return titles


start = types.ReplyKeyboardMarkup(resize_keyboard=True)
start.add(types.KeyboardButton('🌙Хочу прогноз'))


to_autoanswer = types.InlineKeyboardMarkup()
to_autoanswer.add(types.InlineKeyboardButton('🔮 Получить прогноз', url='https://t.me/nastavnik_dire'))
