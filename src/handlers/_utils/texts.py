from aiogram.utils import markdown
from pathlib import Path

from ...constants import DATA_DIR


welcome = "Добро пожаловать, в таро бот Анны Пьерс.\n\nАнна - эксперт в сфере таро и основатель онлайн-школы. Более 16 тыс личных раскладов\n\nТут вы сможете познакомиться с историей карт таро, узнать для чего они нужны и когда появились. Раз в 24 часа вы сможете получить карту дня и личные рекомендации.\n\nБонус - бесплатно карта вашего общего состояния.\n\n👇Для продолжения, нажмите на любую из кнопок снизу"

choose_taro_card = "🔮Ваша задача внимательно посмотреть на карты и выбрать одну из 6 закрытых карт таро"

# Вывод при выборе карт:
CARDS_DIR = DATA_DIR / "cards_photos"
_cards_end_of_all = f'Для расшифровки значения и вашего общего состояния напишите {markdown.hbold("Анне в личные сообщения — https://t.me/taro_anna_pie название карты, чтобы получить расшифровку карты и полезные")} рекомендации🙌\n\n{markdown.hbold("❗️Количество бесплатных мест ограничено")}'
taro_cards = [
        {'photo': CARDS_DIR / "taro_card_0.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Жрица")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_1.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Башня")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_2.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Солнце")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_3.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Сила")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_4.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Луна")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_5.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Колесо Фортуны")}\n\n{_cards_end_of_all}'}
    ]
