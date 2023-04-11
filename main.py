import logging
import requests
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from kb import Main_keyboard, Color_keyboard, Digit_keyboard
from aiogram.dispatcher import Dispatcher

API_TOKEN = "6232142718:AAGtjHPrJJPfAWGztHk-RzwKiTeMWHH4xFc"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Я бот для работы с экологическим продуктом. "
        "Отправьте мне свой запрос, чтобы начать работу.",
        reply_markup=Main_keyboard,
    )
    await message.delete()


@dp.message_handler(lambda message: message.text == "⬅️ Вернуться в главное меню")
async def back_menu(message: types.Message):
    await message.answer("Назад в главное меню", reply_markup=Main_keyboard)
    await message.delete()


color_map = {"🟦": "Бумага", "🟩": "Стекло", "🟧": "Пластик", "🟨": "Металл"}


@dp.message_handler(lambda message: message.text == "♻️ Узнать цветовой маркер отходов")
async def Marker(message: types.Message):
    await message.answer("Выберите цвет урны", reply_markup=Color_keyboard)
    await message.delete()


@dp.message_handler(lambda message: message.text in color_map.keys())
async def handle_color(message: types.Message):
    color = color_map[message.text]
    await message.answer(color)
    await message.delete()


@dp.message_handler(lambda message: message.text == "💡 Советы")
async def Marker(message: types.Message):
    advice_list = [
        "1.Сортируйте мусор, чтобы его можно было переработать",
        "2.Переходите на энергосберегающие лампы",
        "3.Используйте общественный транспорт или ездите на велосипеде",
        "4.Сажайте деревья и цветы на своем участке",
        "5.Используйте многоразовые сумки для покупок",
    ]
    await message.answer("\n".join(advice_list))
    await message.delete()


@dp.message_handler(lambda message: message.text == "❔ Задать вопрос экспертам")
async def send_random_value(message: types.Message):
    response = f'Вы можете задать свой вопрос экспертам по экологии, указав команду и написав в нем ваш вопрос. К примеру: " /q Можете подсказать, как правильно разделять мусор?"'
    await message.answer(response)
    await message.delete()


@dp.message_handler(commands=["q"])
async def send_q_expert(message: types.Message):
    question = message.text.split(maxsplit=1)
    response = f"Вопрос от пользователя {message.from_user.full_name} : {question}"
    await bot.send_message("@ecologisticsexpert", response)
    await message.answer("Ваш вопрос отправлен эксперту, ожидайте ответа.")


digit_map = {
    "1️⃣": "1",
    "2️⃣": "2",
    "3️⃣": "3",
    "4️⃣": "4",
    "5️⃣": "5",
    "6️⃣": "6",
    "7️⃣": "7",
}


@dp.message_handler(lambda message: message.text == "🔢 Коды переработки")
async def send_random_value(message: types.Message):
    await message.answer(
        "♻️ Для обеспечения утилизации одноразовых предметов была разработана система маркировки для всех видов пластика и идентификационные коды. "
        "Маркировка пластика состоит из 3-х стрелок в форме треугольника, внутри которых находится число, обозначающая тип пластика.",
        reply_markup=Digit_keyboard,
    )
    await message.delete()


@dp.message_handler(lambda message: message.text in digit_map.keys())
async def handle_digit(message: types.Message):
    digit = digit_map[message.text]
    await message.answer(digit)
    await message.delete()


API_QA = "7e9f1b481689e9bb85a2119fe75ec481119a9ced"


def get_air_quality(city):
    # API endpoint URL
    url = f"https://api.waqi.info/feed/{city}/?token={API_QA}"
    # Make a request to the API
    response = requests.get(url)
    # Get the JSON response
    data = response.json()
    # Check if the request was successful
    if response.status_code == 200:
        # Get the AQI (air quality index)
        aqi = data["data"]["aqi"]
        # Get the pollutant with the highest concentration
        dominant_pollutant = data["data"]["dominentpol"]
        # Construct a message based on the AQI value
        if aqi <= 50:
            message = f"The air quality in {city} is good (AQI {aqi}). Enjoy your day!"
        elif aqi <= 100:
            message = f"The air quality in {city} is moderate (AQI {aqi}). It's still safe to be outside."
        elif aqi <= 150:
            message = f"The air quality in {city} is unhealthy for sensitive groups (AQI {aqi}). Limit outdoor activities."
        elif aqi <= 200:
            message = f"The air quality in {city} is unhealthy (AQI {aqi}). Consider staying indoors."
        elif aqi <= 300:
            message = f"The air quality in {city} is very unhealthy (AQI {aqi}). Stay indoors and avoid all outdoor activities."
        else:
            message = f"The air quality in {city} is hazardous (AQI {aqi}). Please stay indoors."
        # Add information about the dominant pollutant to the message
        message += f"\n\nThe dominant pollutant is {dominant_pollutant}."
    else:
        message = f"Sorry, we could not retrieve air quality data for {city}."
    return message


@dp.message_handler(lambda message: message.text == "Узнать качества воздуха")
async def msg_air_quality(message: types.Message):
    response_message = (
        "Укажите город на латинице для проверки качества воздуха.\n" "Например: Astana"
    )
    await message.answer(response_message)


@dp.message_handler(commands=["air"])
async def cmd_air_quality(message: types.Message):
    if len(message.text.split()) > 1:
        city = message.text.split(maxsplit=1)[1]
        response_message = get_air_quality(city)
        await message.answer(response_message)
    else:
        response_message = (
            "Укажите город на латинице для проверки качества воздуха.\nНапример: Astana"
        )
        await message.answer(response_message)


API_Yan = "408bfa84-ab2e-4934-8e21-e2cc719dc1c7"


@dp.message_handler(commands=["nearest"])
async def handle_nearest_command(message: types.Message):
    location = message.location
    if location is None:
        await message.reply("Please share your location to use this command")
        return

    latitude = location.latitude
    longitude = location.longitude

    async with aiohttp.ClientSession() as session:
        url = f"https://search-maps.yandex.ru/v1/?apikey={API_Yan}&type=biz&text=прием макулатуры&ll={longitude},{latitude}"
        async with session.get(url) as resp:
            response_json = await resp.json()

            points = response_json["features"]
            if len(points) == 0:
                await message.reply("There are no recycling points nearby")
            else:
                result = ""
                for point in points:
                    name = point["properties"]["name"]
                    address = point["properties"]["address"]
                    distance = int(point["properties"]["Distance"])
                    result += f"{name} ({distance} meters)\n{address}\n"

                await message.reply(result)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

# @dp.message_handler(lambda message: message.text == "Узнать маркировки")
# async def Marker(message: types.Message):
#     response = f''
#     await message.answer(response)
