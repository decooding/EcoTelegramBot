from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["♻️ Узнать цветовой маркер отходов", "🔢 Коды переработки"]
Main_keyboard.add(*buttons)
Main_keyboard.add(KeyboardButton(text="❔ Задать вопрос экспертам")).add(KeyboardButton(text="Узнать качества воздуха"))
Main_keyboard.add(KeyboardButton(text="📍 Узнать ближайшие пункты приема вторсырья"))
Main_keyboard.add(KeyboardButton(text="💡 Советы")).add(KeyboardButton(text="💡 Советы"))
Color_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["🟦", "🟩", "🟥", "🟨", "🟪", "⬜"]
Color_keyboard.add(*buttons).add(KeyboardButton(text="🔄 Вернуться в главное меню"))

Digit_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣"]
Digit_keyboard.add(*buttons).add(KeyboardButton(text="🔄 Вернуться в главное меню"))
