import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from randomfox import fox
from keyboards import (
    start_keyboard,
    main_keyboard,
    line_keyboard,
    product_lines_keyboard,
    amigo_keyboard,
    anti_yellow_keyboard,
    basic_line_keyboard,
    bionika_keyboard,
    care_keyboard,
    repair_structure_keyboard,
    volume_keyboard,
    anti_dandruff_keyboard,
    double_hydration_keyboard,
    color_protection_keyboard,
    daily_use_keyboard,
    balance_keyboard,  # Добавьте этот импорт
    nourishment_keyboard,  # Если вам нужны и другие клавиатуры для BIONIKA
    repair_keyboard,
    density_keyboard,
    hydration_keyboard,
    color_brightness_keyboard,
    training_videos_keyboard,
    care_ultimate_keyboard,
    anti_hair_loss_keyboard,
    hyaluronic_line_keyboard,
    ceramide_line_keyboard,
    acai_line_keyboard,
    coctail_bar_keyboard,
    curl_smooth_hair_keyboard
)

# Обновляем клавиатуру и обработчики для CURL & SMOOTH HAIR (Для кудряшек)
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import config


API_TOKEN = config.token

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды "/start"
@dp.message(lambda message: message.text == "/start")
async def send_start(message: types.Message):
    await message.answer(
        "Пространство SvPons приветствует тебя! Здесь ты найдешь ответы на все возможные вопросы касаемые продвижения брендов Ollin Professional и Hair Sekta.",
        reply_markup=main_keyboard
    )

# Обработчик команды /line
@dp.message(Command("line"))
async def send_line_menu(message: types.Message):
    await message.answer("Выберите категорию:", reply_markup=line_keyboard)

# Обработчик команды /help
@dp.message(Command("help"))
async def open_chat_with_support(message: types.Message):
    await message.answer("Свяжитесь с поддержкой: @Ponsicsv", reply_markup=main_keyboard)


# Обработчик команды /user
@dp.message(Command("user"))
async def send_user(message: types.Message):
    user_name = message.from_user.first_name if message.from_user.first_name else message.from_user.username
    img_fox = fox()  # Получаем случайное изображение лисы
    if not user_name:
        user_name = message.from_user.id

    # Отправляем приветственное сообщение
    await message.answer(f"{user_name}, Привет, я рад что ты смотришь этот бот!", reply_markup=main_keyboard)

    # Отправляем случайное изображение лисы
    if img_fox:
        await message.answer_photo(photo=img_fox, caption="А вот тебе случайная лисичка!")
    else:
        await message.answer("Не удалось получить изображение лисы.")


# Обработчик для линейки "AMIGO"
@dp.message(lambda message: message.text == "AMIGO")
async def send_amigo_categories(message: types.Message):
    await message.answer("Выберите товар из линейки AMIGO:", reply_markup=amigo_keyboard)

# Обработчик для линейки "ANTI-YELLOW"
@dp.message(lambda message: message.text == "ANTI-YELLOW")
async def send_anti_yellow_categories(message: types.Message):
    await message.answer("Выберите товар из линейки ANTI-YELLOW:", reply_markup=anti_yellow_keyboard)

# Обработчик для линейки "BASIC LINE"
@dp.message(lambda message: message.text == "BASIC LINE")
async def send_basic_line_categories(message: types.Message):
    await message.answer("Выберите товар из линейки BASIC LINE:", reply_markup=basic_line_keyboard)

@dp.message(lambda message: message.text == "BIONIKA")
async def send_bionika_categories(message: types.Message):
    await message.answer("Выберите подкатегорию BIONIKA:", reply_markup=bionika_keyboard)

# Обработчик для подкатегории "Баланс от Корней до кончиков"
@dp.message(lambda message: message.text == "Баланс от Корней до кончиков")
async def send_balance_subcategories(message: types.Message):
    await message.answer("Выберите продукт из категории 'Баланс от Корней до кончиков':", reply_markup=balance_keyboard)

# Обработчик для подкатегории "Восстановление и Реконструкция волос"
@dp.message(lambda message: message.text == "Восстановление и Реконструкция волос")
async def send_repair_subcategories(message: types.Message):
    await message.answer("Выберите продукт из категории 'Восстановление и Реконструкция волос':", reply_markup=repair_keyboard)

# Обработчик для подкатегории "Питание и блеск волос"
@dp.message(lambda message: message.text == "Питание и блеск волос")
async def send_nourishment_subcategories(message: types.Message):
    await message.answer("Выберите продукт из категории 'Питание и блеск волос':", reply_markup=nourishment_keyboard)

# Обработчик для подкатегории "Плотность волос"
@dp.message(lambda message: message.text == "Плотность волос")
async def send_density_subcategories(message: types.Message):
    await message.answer("Выберите продукт из категории 'Плотность волос':", reply_markup=density_keyboard)

# Обработчик для подкатегории "Экстра-увлажнение волос"
@dp.message(lambda message: message.text == "Экстра-увлажнение волос")
async def send_hydration_subcategories(message: types.Message):
    await message.answer("Выберите продукт из категории 'Экстра-увлажнение волос':", reply_markup=hydration_keyboard)

# Обработчик для подкатегории "Яркость цвета волос"
@dp.message(lambda message: message.text == "Яркость цвета волос")
async def send_color_brightness_subcategories(message: types.Message):
    await message.answer("Выберите продукт из категории 'Яркость цвета волос':", reply_markup=color_brightness_keyboard)

# Обработчик для подкатегории "Против выпадения волос"
@dp.message(lambda message: message.text == "Против выпадения волос")
async def send_hair_loss_subcategories(message: types.Message):
    await message.answer("Выберите продукт из категории 'Против выпадения волос':", reply_markup=hair_loss_keyboard)

# Обработчик для линейки "CARE"
@dp.message(lambda message: message.text == "CARE")
async def send_care_categories(message: types.Message):
    await message.answer("Выберите категорию из линейки CARE:", reply_markup=care_keyboard)

# Обработчик для подкатегории "Восстановление структуры волос" в линейке "CARE"
@dp.message(lambda message: message.text == "Восстановление структуры волос")
async def send_repair_structure(message: types.Message):
    await message.answer("Выберите продукт из категории 'Восстановление структуры волос':", reply_markup=repair_structure_keyboard)

# Обработчик для подкатегории "Придание объёма" в линейке "CARE"
@dp.message(lambda message: message.text == "Придание объёма")
async def send_volume(message: types.Message):
    await message.answer("Выберите продукт из категории 'Придание объёма':", reply_markup=volume_keyboard)

# Обработчик для подкатегории "Против выпадения волос" в линейке "CARE"
@dp.message(lambda message: message.text == "Против выпадения волос")
async def send_anti_hair_loss(message: types.Message):
    await message.answer("Выберите продукт из категории 'Против выпадения волос':", reply_markup=anti_hair_loss_keyboard)

# Обработчик для подкатегории "Против перхоти" в линейке "CARE"
@dp.message(lambda message: message.text == "Против перхоти")
async def send_anti_dandruff(message: types.Message):
    await message.answer("Выберите продукт из категории 'Против перхоти':", reply_markup=anti_dandruff_keyboard)

# Обработчик для подкатегории "Двойное увлажнение" в линейке "CARE"
@dp.message(lambda message: message.text == "Двойное увлажнение")
async def send_double_hydration(message: types.Message):
    await message.answer("Выберите продукт из категории 'Двойное увлажнение':", reply_markup=double_hydration_keyboard)

# Обработчик для подкатегории "Сохранение цвета и блеска окрашенных волос" в линейке "CARE"
@dp.message(lambda message: message.text == "Сохранение цвета и блеска окрашенных волос")
async def send_color_protection(message: types.Message):
    await message.answer("Выберите продукт из категории 'Сохранение цвета и блеска окрашенных волос':", reply_markup=color_protection_keyboard)

# Обработчик для подкатегории "Для ежедневного применения" в линейке "CARE"
@dp.message(lambda message: message.text == "Для ежедневного применения")
async def send_daily_use(message: types.Message):
    await message.answer("Выберите продукт из категории 'Для ежедневного применения':", reply_markup=daily_use_keyboard)

# Обработчик для линейки "CARE ULTIMATE"
@dp.message(lambda message: message.text == "CARE ULTIMATE")
async def send_care_ultimate_categories(message: types.Message):
    await message.answer("Выберите категорию из линейки CARE ULTIMATE:", reply_markup=care_ultimate_keyboard)

# Обработчик для "Линии с гиалуроновой кислотой увлажняющая"
@dp.message(lambda message: message.text == "Линия с гиалуроновой кислотой увлажняющая")
async def send_hyaluronic_line(message: types.Message):
    await message.answer("Выберите продукт из линии с гиалуроновой кислотой:", reply_markup=hyaluronic_line_keyboard)

# Обработчик для "Линии с церамидами восстанавливающая"
@dp.message(lambda message: message.text == "Линия с церамидами восстанавливающая")
async def send_ceramide_line(message: types.Message):
    await message.answer("Выберите продукт из линии с церамидами:", reply_markup=ceramide_line_keyboard)

# Обработчик для "Линии с экстрактом ягод асаи для окрашенных волос"
@dp.message(lambda message: message.text == "Линия с экстрактом ягод асаи для окрашенных волос")
async def send_acai_line(message: types.Message):
    await message.answer("Выберите продукт из линии с экстрактом ягод асаи:", reply_markup=acai_line_keyboard)

# Обработчик для линейки "Coctail BAR"
@dp.message(lambda message: message.text == "Coctail BAR")
async def send_coctail_bar_categories(message: types.Message):
    await message.answer("Выберите продукт из линейки Coctail BAR:", reply_markup=coctail_bar_keyboard)

# Обработчик для линейки "CURL & SMOOTH HAIR (Для кудряшек)"
@dp.message(lambda message: message.text == "CURL & SMOOTH HAIR (Для кудряшек)")
async def send_curl_smooth_hair_categories(message: types.Message):
    await message.answer("Выберите категорию из CURL & SMOOTH HAIR (Для кудряшек):", reply_markup=curl_smooth_hair_keyboard)

# Обработчик для "Химическая завивка"
@dp.message(lambda message: message.text == "Химическая завивка")
async def send_chemical_curl_products(message: types.Message):
    await message.answer("Выберите продукт из категории 'Химическая завивка':", reply_markup=chemical_curl_keyboard)

# Обработчик для "Домашний уход"
@dp.message(lambda message: message.text == "Домашний уход")
async def send_home_care_products(message: types.Message):
    await message.answer("Выберите продукт из категории 'Домашний уход':", reply_markup=home_care_keyboard)

# Обработчик кнопки "Назад"
@dp.message(lambda message: message.text == "Назад")
async def go_back(message: types.Message):
    # Проверяем, откуда пользователь нажал кнопку "Назад"
    if message.reply_markup == line_keyboard:
        # Если пользователь в меню "Линейки товаров" или "Обучающие видео", то возвращаем в главное меню
        await message.answer("Возврат в главное меню", reply_markup=main_keyboard)
    elif message.reply_markup in [product_lines_keyboard, training_videos_keyboard]:
        # Если пользователь находится в категориях "Линейки товаров" или "Обучающие видео", возвращаем на уровень выше
        await message.answer("Возврат к выбору категории:", reply_markup=line_keyboard)
    else:
        # По умолчанию возвращаем в главное меню
        await message.answer("Возврат в главное меню", reply_markup=main_keyboard)


# Обработчик для подкатегории "Линейки товаров"
@dp.message(lambda message: message.text == "Линейки товаров")
async def send_product_lines(message: types.Message):
    await message.answer("Выберите линейку товаров:", reply_markup=product_lines_keyboard)

# Обработчик для подкатегории "Обучающие видео"
@dp.message(lambda message: message.text == "Обучающие видео")
async def send_training_videos(message: types.Message):
    await message.answer("Выберите обучающее видео:", reply_markup=training_videos_keyboard)

# Основная функция запуска бота
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
