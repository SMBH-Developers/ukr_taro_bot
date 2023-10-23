from aiogram import types


menu = types.InlineKeyboardMarkup()
menu.add(types.InlineKeyboardButton("👥 Пользователи", callback_data='admin?users'))
menu.add(types.InlineKeyboardButton("📈 Этапы", callback_data='admin?stages'))

_back_to_menu_btn = types.InlineKeyboardButton("⬅ ️В меню", callback_data='admin?back')

back_to_menu = types.InlineKeyboardMarkup()
back_to_menu.add(_back_to_menu_btn)


users_kb = types.InlineKeyboardMarkup()
users_kb.add(types.InlineKeyboardButton("📊 Выгрузка за 30 дней", callback_data="users?excel"))
users_kb.add(_back_to_menu_btn)


stages_kb = types.InlineKeyboardMarkup()
stages_kb.add(types.InlineKeyboardButton("📊 Выгрузка за 30 дней", callback_data="stages?excel"))
stages_kb.add(_back_to_menu_btn)

