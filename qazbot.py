import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from kb import Main_keyboard, Color_keyboard, Digit_keyboard
from aiogram.dispatcher import Dispatcher

API_TOKEN = "6232142718:AAGtjHPrJJPfAWGztHk-RzwKiTeMWHH4xFc"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def qazbot_main(bot, chat_id):
    @dp.message_handler(commands=["start"])
    async def send_welcome(message: types.Message):
        await message.answer(
            "Сәлем" "Отправьте мне свой запрос, чтобы начать работу.",
            reply_markup=Main_keyboard,
        )
        await message.delete()

    @dp.message_handler(lambda message: message.text == "🔄 Вернуться в главное меню")
    async def back_menu(message: types.Message):
        await message.answer("Назад в главное меню", reply_markup=Main_keyboard)
        await message.delete()

    color_map = {
        "🟦": {"name": "Стекло", "image": "color_img/2.jpeg"},
        "🟩": {"name": "Органика", "image": "color_img/6.jpeg"},
        "🟥": {"name": "Пластик", "image": "color_img/5.jpeg"},
        "🟨": {"name": "Бумага", "image": "color_img/4.jpeg"},
        "🟪": {"name": "Металл", "image": "color_img/1.jpeg"},
        "⬜": {"name": "Батарейки", "image": "color_img/3.jpeg"},
    }

    @dp.message_handler(
        lambda message: message.text == "♻️ Узнать цветовой маркер отходов"
    )
    async def Marker(message: types.Message):
        await message.answer("Выберите цвет урны", reply_markup=Color_keyboard)
        await message.delete()

    @dp.message_handler(lambda message: message.text in color_map.keys())
    async def handle_color(message: types.Message):
        chat_id = message.chat.id

        color = color_map[message.text]
        image_path = color["image"]
        name = color["name"]
        await bot.send_photo(chat_id=chat_id, photo=open(image_path, "rb"))
        await bot.send_message(chat_id=chat_id, text=name)
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
        response = f"Вопрос от пользователя {f'@{message.from_user.username}' or message.from_user.id}: {question}"
        await bot.send_message("@ecologisticsexpert", response)
        await message.answer("Ваш вопрос отправлен эксперту, ожидайте ответа.")

    digit_map = {
        "1️⃣": {
            "description": "Полиэтилен терефталата (PET) - широко используется в производстве бутылок для напитков, упаковок для продуктов питания, контейнеров для косметических средств и прочих товаров. Также может использоваться для производства волокон для одежды и домашнего текстиля. ",
            "image": "digit_img/1.jpeg",
        },
        "2️⃣": {
            "description": "Полиэтилен высокой плотности (ПВХ) - широко используется в производстве пластиковых бутылок для молока, воды, сока, а также в упаковке косметических средств, бытовой химии и прочих товаров.",
            "image": "digit_img/2.jpeg",
        },
        "3️⃣": {
            "description": "Поливинилхлорид (PVC) - используется в производстве оконных профилей, труб, кабельных изделий, пленок для упаковки, сумок, обуви, мебели, стеновых панелей, каркасов для зонтиков и прочих товаров.",
            "image": "digit_img/3.jpeg",
        },
        "4️⃣": {
            "description": "Полипропилен низкой плотности (ПНД) - используется в производстве пищевых пленок, мешков для мусора, пакетов для упаковки продуктов, пакетов для хранения одежды, игрушек и т.д.",
            "image": "digit_img/4.jpeg",
        },
        "5️⃣": {
            "description": "Полипропилен (PP) - широко используется в производстве упаковочных материалов, в том числе контейнеров, пищевых коробок, пакетов, крышек, крышек для бутылок, косметических бутылок, автомобильных деталей и т.д.",
            "image": "digit_img/5.jpeg",
        },
        "6️⃣": {
            "description": "Полистирол (PS) - часто используется в производстве различных пластиковых изделий, включая пищевые контейнеры, стаканы, крышки для стаканов, игрушки, упаковки, изделия для медицины, бытовые принадлежности и т.д.",
            "image": "digit_img/6.jpeg",
        },
        "7️⃣": {
            "description": "Акрилонитрил-бутадиен-стирол (ABS) - применяется в производстве автомобильных деталей, электроники, бытовых приборов, игрушек, мебели, бутылок и прочих изделий.",
            "image": "digit_img/7.jpeg",
        },
    }

    @dp.message_handler(lambda message: message.text == "🔢 Коды переработки")
    async def send_random_value(message: types.Message):
        text = (
            "♻️ Для обеспечения утилизации одноразовых предметов была разработана система маркировки для всех видов пластика и идентификационные коды. "
            "Маркировка пластика состоит из 3-х стрелок в форме треугольника, внутри которых находится число, обозначающая тип пластика."
        )
        await message.answer(text, reply_markup=Digit_keyboard)
        await message.delete()

    @dp.message_handler(lambda message: message.text in digit_map.keys())
    async def handle_digit(message: types.Message):
        chat_id = message.chat.id

        digit = digit_map[message.text]
        image_path = digit["image"]
        description = digit["description"]
        await bot.send_photo(chat_id=chat_id, photo=open(image_path, "rb"))
        await bot.send_message(chat_id=chat_id, text=description)
        await message.delete()

    API_QA = "7e9f1b481689e9bb85a2119fe75ec481119a9ced"

    def get_air_quality(city):
        url = f"https://api.waqi.info/feed/{city}/?token={API_QA}"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            aqi = data["data"]["aqi"]
            dominant_pollutant = data["data"]["dominentpol"]
            if aqi <= 50:
                message = f"Качество воздуха в городе {city} хорошее (AQI {aqi}). Наслаждайтесь своим днем!"
            elif aqi <= 100:
                message = f"Качество воздуха в городе {city} умеренное (AQI {aqi}). По-прежнему безопасно находиться на улице."
            elif aqi <= 150:
                message = f"Качество воздуха в городе {city} небезопасное для групп людей с чувствительностью (AQI {aqi}). Ограничьте время, проведенное на улице."
            elif aqi <= 200:
                message = f"Качество воздуха в городе {city} небезопасное (AQI {aqi}). Рассмотрите возможность оставаться в помещении."
            elif aqi <= 300:
                message = f"Качество воздуха в городе {city} очень небезопасное (AQI {aqi}). Оставайтесь в помещении и избегайте любых уличных активностей."
            else:
                message = f"Качество воздуха в городе {city} опасное (AQI {aqi}). Пожалуйста, оставайтесь в помещении."
                message += (
                    f"\n\nДоминирующим загрязнителем является {dominant_pollutant}."
                )
        else:
            message = f"К сожалению, мы не смогли получить данные о качестве воздуха для города {city}."
        return message

    @dp.message_handler(lambda message: message.text == "Узнать качества воздуха")
    async def msg_air_quality(message: types.Message):
        response_message = (
            "Ведите команду и укажите город на латинице для проверки качества воздуха.\n"
            "Например: /air Astana"
        )
        await message.answer(response_message)

    @dp.message_handler(commands=["air"])
    async def cmd_air_quality(message: types.Message):
        if len(message.text.split()) > 1:
            city = message.text.split(maxsplit=1)[1]
            response_message = get_air_quality(city)
            await message.answer(response_message)
        else:
            response_message = "Неверна ведена команда или наименование города, напишите правильном порядке. \nНапример: /air Astana"
            await message.answer(response_message)

    @dp.message_handler(commands=["all"])
    async def send_to_all(message: types.Message):
        if message.chat.type == "private":
            await message.answer("Команда доступна только в групповом чате или канале.")
            return

        events_message = message.text.split(maxsplit=1)[1]
        chat = await bot.get_chat(chat_id=message.chat.id)
        async for member in bot.iter_chat_members(chat_id=chat.id):
            if member.status == "member":
                try:
                    await bot.send_message(chat_id=member.user.id, text=events_message)
                except:
                    pass
        await message.answer("Рассылка выполнена.")

    executor.start_polling(dp, skip_updates=True)
