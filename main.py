import logging
import re
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = ('6065068013:AAHJvtuCsNkq0CR0QeYIi50mxj5bf2Lcydo')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Задать вопрос экспертам"))
    buttons = ["Узнать маркировки", "Коды переработки"]
    keyboard.add(*buttons)
    keyboard.add(types.KeyboardButton(text="Советы"))

    await message.answer("Привет! Я бот для работы с экологическим продуктом. "
                         "Отправьте мне свой запрос, чтобы начать работу.", reply_markup=keyboard)


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    commands = ['/start - начать работу с ботом',
                '/help - список доступных команд',
                '/question - задать вопрос экспертам',
                '/marker - узнать маркировки',
                '/code - коды переработки']
    await message.answer("\n".join(commands))


@dp.message_handler(commands=['marker'])
async def get_markers(message: types.Message):
    markers = ['Маркировка "Один"',
               'Маркировка "Два"',
               'Маркировка "Три"']
    response = "Доступные маркировки:\n" + "\n".join(markers)
    await message.answer(response)


EXPERTS = ['@patyson']


@dp.message_handler(lambda message: message.text == "Задать вопрос экспертам")
async def send_random_value(message: types.Message):
    response = f'Вы можете задать свой вопрос экспертам по экологии, написав сообщение и указав в нем имя эксперта (например, {EXPERTS[0]}), к которому вы хотите обратиться.'
    await message.answer(response)

    # проверяем, содержит ли сообщение имя эксперта
    expert_name_match = re.search(rf'{"|".join(EXPERTS)}', message.text)

    if expert_name_match:
        # если да, то отправляем сообщение эксперту
        expert_name = expert_name_match.group()
        question = message.text.replace(expert_name, "")
        response = f'Вопрос от пользователя {message.from_user.username}:\n{question}'
        await bot.send_message(expert_name, response)
        await message.answer('Ваш вопрос отправлен эксперту, ожидайте ответа.')
    else:
        # если нет, то отправляем сообщение с просьбой указать имя эксперта
        response = f'Для того чтобы задать вопрос эксперту, необходимо указать его имя в сообщении. Например, {EXPERTS[0]} Можете подсказать, как правильно разделять мусор?'
        await message.answer(response)


@dp.message_handler()
async def echo_message(message: types.Message):
    """
    Обрабатывает запросы от пользователя и отправляет ответ
    """
    if "Советы" in message.text:
        advice_list = ["1.Сортируйте мусор, чтобы его можно было переработать",
                       "2.Переходите на энергосберегающие лампы",
                       "3.Используйте общественный транспорт или ездите на велосипеде",
                       "4.Сажайте деревья и цветы на своем участке",
                       "5.Используйте многоразовые сумки для покупок"]
        await message.answer("\n".join(advice_list))
    else:
        # в остальных случаях отправляем стандартный ответ
        response = "стандартный ответ"
        await message.answer(response)

executor.start_polling(dp, skip_updates=True)
