from aiogram.utils import markdown
from pathlib import Path

from ...constants import DATA_DIR


welcome = "Ласкаво просимо до робот Анни П'єрс.\n\nАнна - експерт у сфері таро та засновник онлайн-школи. Понад 16 тис особистих розкладів\n\nТут ви можете познайомитися з історією карт таро, дізнатися для чого вони потрібні і коли з'явилися. Раз на 24 години ви зможете отримати картку дня та особисті рекомендації.\n\nБонус – безкоштовно карта вашого загального стану.\n\n👇Для продовження, натисніть на будь-яку з кнопок знизу"

choose_taro_card = "🔮Ваша задача уважно подивіться на карти та виберіть одну з 6 закритих карт таро"

# Вывод при выборе карт:
CARDS_DIR = DATA_DIR / "cards_photos"
_cards_end_of_all = f'Для розшифрування значення та вашого загального стану напишіть {markdown.hbold("мені в особисті повідомлення - https://t.me/tarolog_anna_pier назва карти, і я особисто розшифрую карту і дам корисні")} рекомендації🙌\n\n{markdown.hbold("❗️Колічество безкоштовних місць обмежено")}'
taro_cards = [
        {'photo': CARDS_DIR / "taro_card_0.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Жриця")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_1.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Башта")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_2.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Сонце")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_3.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Сила")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_4.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Місяць")}\n\n{_cards_end_of_all}'},
        {'photo': CARDS_DIR / "taro_card_5.jpg", 'text': f'Ваша карта — {markdown.hbold("Аркан Колесо Фортуни")}\n\n{_cards_end_of_all}'}
    ]
