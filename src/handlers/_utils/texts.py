from aiogram.utils import markdown
from pathlib import Path

from ...constants import DATA_DIR


welcome = "Ласкаво просимо, в робот створений Анною П'єрс.\n\nАнна - експерт у сфері таро та засновник онлайн-школи. Понад 16 тис особистих розкладів\n\nЯкщо Ви тут – це не випадковість. Значить, Вас щось турбує і карти допоможуть у цьому розібратися.\n\nНу що, почнемо.\n\n👇Для продовження, натисніть кнопку знизу"

choose_taro_card = "🔮Ваша задача уважно подивіться на карти та виберіть одну з 6 закритих карт таро"

# Вывод при выборе карт:
CARDS_DIR = DATA_DIR / "cards_photos"
_cards_end_of_all = f'Для розшифрування значення та вашого загального стану запам’ятайте назву чі номер карти, та перейдя далі, не забудьте написати її.'
taro_cards = [
        {'photo': CARDS_DIR / "taro_card_0.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Жриця")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_1.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Башта")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_2.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Сонце")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_3.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Сила")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_4.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Місяць")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_5.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Колесо Фортуни")}\n\n{_cards_end_of_all}'}
    ]
