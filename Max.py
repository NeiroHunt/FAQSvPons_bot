import logging
import asyncio
from randomfox import fox
from aiogram.types import FSInputFile
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from keyboards import (
    start_keyboard,
    main_keyboard,
    product_company_keyboard,
    ollin_professional_keyboard,
    training_videos_keyboard,
    price_keyboard,
    support_keyboard,
    fox_keyboard,
    coloring_powders_keyboard,
    technical_line_keyboard,
    hair_care_keyboard,
    hair_treatment_keyboard,
    style_styling_keyboard,
    chemical_perming_keyboard,
    xplex_care_keyboard,
    kondor_keyboard
)
import config


API_TOKEN = config.token

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды "Пуск"
@dp.message(lambda message: message.text == "/start")
async def send_start(message: types.Message):
    video_url = 'https://drive.google.com/uc?export=download&id=1neJitQWknoue6BbPbztdqaEgr_T7iuSQ'
    await message.answer_video(video=video_url)

    # Отправляем приветственное сообщение
    await message.answer(
        "Пространство SvPons приветствует тебя! Здесь ты найдешь ответы на все возможные вопросы касаемые продвижения брендов Ollin Professional и Hair Sekta.",
        reply_markup=main_keyboard
    )

# Обработчик команды "📦 Продукты компании"
@dp.message(lambda message: message.text == "📦 Продукты компании")
async def send_product_company_menu(message: types.Message):
    await message.answer("Выберите продукт компании:", reply_markup=product_company_keyboard)

# Обработчик команды "OLLIN Professional"
@dp.message(lambda message: message.text == "OLLIN Professional")
async def send_ollin_professional_menu(message: types.Message):
    await message.answer_photo(photo='https://drive.google.com/uc?export=view&id=1JfposD56-qS2srbzp8jEiVmcm5heHVdF')
    await message.answer("Выберите категорию OLLIN Professional:", reply_markup=ollin_professional_keyboard)

# Обработчик команды "Красители, порошки и оксиды"
@dp.message(lambda message: message.text == "Красители, порошки и оксиды")
async def send_coloring_powders_menu(message: types.Message):
    await message.answer("Выберите категорию красителей, порошков и оксидов:", reply_markup=coloring_powders_keyboard)

# Обработчик команды "Краситель COLOR"
@dp.message(lambda message: message.text == "Краситель COLOR")
async def send_color_dye_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1z-_3ylsIDbdc9qQlHjkZpfCQ3By7RwHb',
        'https://drive.google.com/uc?export=view&id=1EG6-tcW9z_J3jtjT5XkF44OjDr-2lbcN',
        'https://drive.google.com/uc?export=view&id=1owSYMof56WFelZtRtp0GquD0lNC2rVgN',
        'https://drive.google.com/uc?export=view&id=16OSBB52nxct9GFimR1EFQPTdDdi_VF4h',
        'https://drive.google.com/uc?export=view&id=1PRji9Q6b6ojEGIbqQm_gAUuA7EpghU2_'
    ]
    for image in images:
        await message.answer_photo(photo=image)

# Обработчик команды "Краситель PERFORMANCE"
@dp.message(lambda message: message.text == "Краситель PERFORMANCE")
async def send_performance_dye_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1OIqNGDIYfhrE-bnmOeFz5d_l3bYNlJbr',
        'https://drive.google.com/uc?export=view&id=1smZCrMGwh-J7R8gFhs2zcvbUGDbpHZH3'
    ]
    for image in images:
        await message.answer_photo(photo=image)

# Обработчик команды "Краситель N - JOY"
@dp.message(lambda message: message.text == "Краситель N - JOY")
async def send_n_joy_dye_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=11yuDSCH_D2vPpNEfISPZmSjPh8svV00E',
        'https://drive.google.com/uc?export=view&id=1m4e_zzOSMwdvkdV8xRB0n0A5s4HF9ihe'
    ]
    for image in images:
        await message.answer_photo(photo=image)

# Обработчик команды "Краситель SILK TOUCH"
@dp.message(lambda message: message.text == "Краситель SILK TOUCH")
async def send_silk_touch_dye_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1ozO3VN93ezDeJLuOITT6fgEPzfwjcP-s',
        'https://drive.google.com/uc?export=view&id=11LvqozZotr26CielQcQa0zuMM3UJZ1Vp'
    ]
    for image in images:
        await message.answer_photo(photo=image)

# Обработчик команды "Краситель MEGAPOLIS"
@dp.message(lambda message: message.text == "Краситель MEGAPOLIS")
async def send_megapolis_dye_menu(message: types.Message):
    await message.answer_photo(photo='https://drive.google.com/uc?export=view&id=1lfzwtsPT0x0zXB-kuoAa-GmNFZJtyVym')

# Обработчик команды "MATISSE COLOR"
@dp.message(lambda message: message.text == "MATISSE COLOR")
async def send_matisse_color_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1qEc_kz6jKX6f1w-VB3s3XqUa1vOdMRqS',
        'https://drive.google.com/uc?export=view&id=1RUd8n5P57dVrNiHPEAq8uFD4EI8Dwjm8'
    ]
    for image in images:
        await message.answer_photo(photo=image)

# Обработчик команды "Осветляющие порошки"
@dp.message(lambda message: message.text == "Осветляющие порошки")
async def send_bleaching_powders_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1JW4yf6yiDcgqN9Qw5nJwKkjcJI3QfSHL',
        'https://drive.google.com/uc?export=view&id=1VwF-pauAjVUDjtxKZWJlE5JEyLdpAasR',
        'https://drive.google.com/uc?export=view&id=135EWGTfzF66_xRWMMjxMEZItgBdD1iHj'
    ]
    for image in images:
        await message.answer_photo(photo=image)

# Обработчик команды "Техническая линия"
@dp.message(lambda message: message.text == "Техническая линия")
async def send_technical_line_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1Pk4lBXHgfOOiWTL1BnqLrqDmzUCP-U5B',
        'https://drive.google.com/uc?export=view&id=1AgybE0MDufFNqbwPrONxhTJ3g08lBNch',
        'https://drive.google.com/uc?export=view&id=1TG2t91pe9q6Yqp8jVsFIiz9g2QvEQaTE',
        'https://drive.google.com/uc?export=view&id=1ZkdGs9N-xqc4qeGaiCSyLS-pcBB1-z6U',
        'https://drive.google.com/uc?export=view&id=15Z_djMj5Nv-e7iilV7rZQtRANzou4Crv',
        'https://drive.google.com/uc?export=view&id=12imOmtx2kDlOTwdPEk2WVmfxuSu-pJ4v'
    ]
    for image in images:
        await message.answer_photo(photo=image)

# Обработчик команды "Уход за волосами"
@dp.message(lambda message: message.text == "Уход за волосами")
async def send_hair_care_menu(message: types.Message):
    await message.answer("Выберите категорию ухода за волосами:", reply_markup=hair_care_keyboard)

# Обработчики для подкатегорий "CARE" и "Ultimate CARE"
@dp.message(lambda message: message.text == "CARE")
async def send_care_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1xsNuxKANbEW4gLk7WLxiVNyJldcGQA6D',
        'https://drive.google.com/uc?export=view&id=110p4AovXr-hEu5TdyWbVf1xdWg9lPmOs',
        'https://drive.google.com/uc?export=view&id=1Wcxd0uKeY9nPmZTicj7iPerdwoGm4oDe',
        'https://drive.google.com/uc?export=view&id=1IzGkIAd4brnEM7q0IklHwkclcJcf-s-g',
        'https://drive.google.com/uc?export=view&id=1ju77NSJShNdA1U8Z8pjTju3e52j8tfkO',
        'https://drive.google.com/uc?export=view&id=18fPbJbHkLcu6ppn9Mt5H3fdhR0k1jvEn',
        'https://drive.google.com/uc?export=view&id=12k2ID9orKeqRwfM1xMOCTrilOzdXifCV'
    ]
    for image in images:
        await message.answer_photo(photo=image)

@dp.message(lambda message: message.text == "Ultimate CARE")
async def send_ultimate_care_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1uDQm6Y6IdThp4LZkZ9DOXYUQvLi_x9qm',
        'https://drive.google.com/uc?export=view&id=1Ol8PUpDCjSJR3SrsMMiawnTVsyKLolLp',
        'https://drive.google.com/uc?export=view&id=1OuTjYoULHp5w7is9jy02sSA4fxn2KN4c'
    ]
    for image in images:
        await message.answer_photo(photo=image)

# Обработчики для подкатегорий "BASIC LINE", "BIONIKA", "PERFECT HAIR"
@dp.message(lambda message: message.text == "BASIC LINE")
async def send_basic_line_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1pCdNVyYvW92G82JBify6Zsjdl9c_a0_j',
        'https://drive.google.com/uc?export=view&id=1eazTpfk0cQsmRmIh3APmC_b1D3iKxXRW',
        'https://drive.google.com/uc?export=view&id=1-q8-BrA0GR0qr2kZKQ5H11zLLwvE_xzD'
    ]
    for image in images:
        await message.answer_photo(photo=image)

@dp.message(lambda message: message.text == "BIONIKA")
async def send_bionika_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1Rn9xCL6zSu3olZr0xAYCht1TP-g8WwdI',
        'https://drive.google.com/uc?export=view&id=1elpguSCII5mnAJwCfg54Ktvl2PKY846Z',
        'https://drive.google.com/uc?export=view&id=1IuQdvxla7vhBPpP2t0n2INwNQpV1pokk',
        'https://drive.google.com/uc?export=view&id=11uXpHUw6jlM94GjbmcNXHVmYR9OEsPas',
        'https://drive.google.com/uc?export=view&id=1GPeHe2U_pQFuC3a3BvLn0YIIlyD724NA',
        'https://drive.google.com/uc?export=view&id=1zcLvhv2alRq2big932fpJKhaOBUYTWlb',
        'https://drive.google.com/uc?export=view&id=1Kv-N2sBZZK88K7XGITvIpZzPu5mfkOnN',
        'https://drive.google.com/uc?export=view&id=1Pjf-vshSchtNfYpCP8Zu0DnZ_YsxMq3s'
    ]
    for image in images:
        await message.answer_photo(photo=image)

@dp.message(lambda message: message.text == "PERFECT HAIR")
async def send_perfect_hair_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1Rr6e3T3mK-CVIMWEB3HaAVapsjCt5od9',
        'https://drive.google.com/uc?export=view&id=1E7ygJSubLHnCObH3tJZMuVfZcOHYnFkc',
        'https://drive.google.com/uc?export=view&id=1BOc1y2NAucAr86Is0ywv1sPteQFVMhR8',
        'https://drive.google.com/uc?export=view&id=1WJUi7_NmfVH4rgxSgqPjBZn_MT5wLb_Z',
        'https://drive.google.com/uc?export=view&id=1KcqaJa55MG4NIbIxB1qPgQljZCfM47LF',
        'https://drive.google.com/uc?export=view&id=1RIThuRrLvbE8h8CGDcYvDgUYk5uH_19T',
        'https://drive.google.com/uc?export=view&id=15iVWhHUcrexsTno1MXUIvQK8-5fgT-Ad'
    ]
    for image in images:
        await message.answer_photo(photo=image)

# Обработчики для подкатегорий "MEGAPOLIS", "Coctail BAR", "CURL & SMOOTH HAIR"
@dp.message(lambda message: message.text == "MEGAPOLIS")
async def send_megapolis_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1w7eTxcYOtvLKxRtQcIRUojGJa0wCBMNi',
        'https://drive.google.com/uc?export=view&id=1VKSutDqauVPuY7qPbv52F85xAU2zyuIw',
        'https://drive.google.com/uc?export=view&id=16018y0symWLsegTKCt0z80Uicd5yMDmp',
        'https://drive.google.com/uc?export=view&id=1ArC-70QZpELGg_kN1fDx5gkFklMUj3OS'
    ]
    for image in images:
        await message.answer_photo(photo=image)

@dp.message(lambda message: message.text == "Coctail BAR")
async def send_coctail_bar_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=14jVtb7R7m25UBlLXdvsko4TlI1BhCwyJ',
        'https://drive.google.com/uc?export=view&id=1Q86N-Vqr6QirRdGwuR6Uvub5lt0Lv6zA'
    ]
    for image in images:
        await message.answer_photo(photo=image)

@dp.message(lambda message: message.text == "CURL & SMOOTH HAIR")
async def send_curl_smooth_hair_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1-adNH335C702_WCwzSKt8yZFz4h3ydR5',
        'https://drive.google.com/uc?export=view&id=1rJwofVvnyPHH5PoO-k9N1PktjPCiXKa5'
    ]
    for image in images:
        await message.answer_photo(photo=image)

# Обработчики для подкатегорий "INTENSE Profi COLOR", "PREMIER FOR MEN", "SALON BEAUTY", "SHINE BLOND"
@dp.message(lambda message: message.text == "INTENSE Profi COLOR")
async def send_intense_profi_color_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=17kbII6TB6kRSrWjk0xQ_dALmv9uDyvbr',
        'https://drive.google.com/uc?export=view&id=1-rbdU_nwwfUXKdelvUc9RUw3qre_oB94'
    ]
    for image in images:
        await message.answer_photo(photo=image)

@dp.message(lambda message: message.text == "PREMIER FOR MEN")
async def send_premier_for_men_menu(message: types.Message):
    await message.answer_photo(photo='https://drive.google.com/uc?export=view&id=1McuNHfkK6GRe3jbPTweSlXsY5RHYZ5xa')

@dp.message(lambda message: message.text == "SALON BEAUTY")
async def send_salon_beauty_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1yQs362vVIaJRl2G4PFk9AAg_zj36GjdL',
        'https://drive.google.com/uc?export=view&id=1lklZP4Byz6WfYdUwUUz8_C7IJ1WyHb-t',
        'https://drive.google.com/uc?export=view&id=1iqbAilN5VGJ089m8JpNmF1_YwvLfFtBL'
    ]
    for image in images:
        await message.answer_photo(photo=image)

@dp.message(lambda message: message.text == "SHINE BLOND")
async def send_shine_blond_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=11OchCmqByozT07UH9DMeLB0pmO6N6M-X',
        'https://drive.google.com/uc?export=view&id=1yuxw3_5jWjOqESIL5adP9YRxhmuQ-xTT'
    ]
    for image in images:
        await message.answer_photo(photo=image)

# Обработчик команды "Уход за натуральным блондом и осветленными волосами"
@dp.message(lambda message: message.text == "Уход за натуральным блондом и осветленными волосами")
async def send_blonde_hair_care_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1P9Z-GReUVJsNHB0DTw50cc9EiVn_HPaA',
        'https://drive.google.com/uc?export=view&id=1dKrBRJFxgYP3XZUvUQosJisO6dKF4CpW'
    ]
    for image in images:
        await message.answer_photo(photo=image)

@dp.message(lambda message: message.text == "Лечение волос и кожи головы")
async def send_hair_treatment_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1o55jKisvs_vDv4ao498HBz9YA54OZFXO',
        'https://drive.google.com/uc?export=view&id=1iWQ2cpIF4ccxowEseHP2FYi_Z0ZaotHy',
        'https://drive.google.com/uc?export=view&id=1qkl6S__RJcGXF4UswxCTOzvKbg-t2_II',
        'https://drive.google.com/uc?export=view&id=1JKSlB9IT7_dHjUDEyucXuT369aYClZHZ',
        'https://drive.google.com/uc?export=view&id=1oqvpHZMdx5JNBeXW6zN0nTUn1BCFr1ie',
        'https://drive.google.com/uc?export=view&id=1zbUh8JcTPd6d4C2I4w4tjzdX5dJZo3mi',
        'https://drive.google.com/uc?export=view&id=1436fZfiatWsX4Izf_0NF0sO4-_SIofCO'
    ]
    for image in images:
        await message.answer_photo(photo=image)

@dp.message(lambda message: message.text == "STYLE Стайлинги")
async def send_style_styling_menu(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1_HsKycmT9SKQhDXEKudIKJaWXazmegYL',
        'https://drive.google.com/uc?export=view&id=1v8EOxTmffWDtttwBLbH0PPfrUFe7CC1w',
        'https://drive.google.com/uc?export=view&id=1yWZZH6sw25PvS6bepv6acWZ4JqhpUMlA',
        'https://drive.google.com/uc?export=view&id=1Ck1dx4lizBqMM_a8bqSYJ8y6CfAlN_HH',
        'https://drive.google.com/uc?export=view&id=1zRv7fOTYTdtUV3PLY4Vj_SU8QFa7mQNZ'
    ]
    for image in images:
        await message.answer_photo(photo=image)

@dp.message(lambda message: message.text == "Продукты Retail")
async def send_retail_products_images(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1fOGbeBAs5T3C2p9MVfplqJr9ud5QoLbf',
        'https://drive.google.com/uc?export=view&id=1dstWG0Kd1pLHHjE6fw0EjXVebdFFkWU0',
        'https://drive.google.com/uc?export=view&id=1kQmC2SnJ5HmlUWMw7Zgy6FpIWxTydJr-',
        'https://drive.google.com/uc?export=view&id=1VmViB7JU14rwpsT7zvd1huMCxc3A3bl0',
        'https://drive.google.com/uc?export=view&id=1LFv85zoDk3mNQbyccoTzW1rJgDt6QOwu',
        'https://drive.google.com/uc?export=view&id=1ydWRYQKgOD1tHCCVyCzxHtXRkkq_m016',
        'https://drive.google.com/uc?export=view&id=1kf_JWcxUwJ0QK8xig8VuHYnYBWgB6F_k',
        'https://drive.google.com/uc?export=view&id=1TaMMHrEJKctHbBuEH7NwbfUmOwwqxOVl'
    ]
    for image in images:
        await message.answer_photo(photo=image)

@dp.message(lambda message: message.text == "Оборудование для укладки волос")
async def send_styling_equipment_pdf(message: types.Message):
    file_path = 'E:/IMG Bot/30.Obor/Obor2024.pdf'  # Укажите точный путь к вашему локальному PDF файлу
    pdf_file = FSInputFile(file_path)  # Создаем объект FSInputFile для загрузки файла
    await message.answer_document(document=pdf_file)  # Отправляем файл пользователю

@dp.message(lambda message: message.text == "X-PLEX комплекс продуктов для восстановления и сохранения здоровья волос")
async def send_xplex_products(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=1au4H8rvlY22tWTkZlTq6Clh1KbnpzCWn',
        'https://drive.google.com/uc?export=view&id=1PI4rtwLJl8MA02f-3CZed-57e2z5B60Z'
    ]
    for image in images:
        await message.answer_photo(photo=image)

@dp.message(lambda message: message.text == "Прайс")
async def send_price_pdf(message: types.Message):
    file_path = 'E:/IMG Bot/31.Prais/прайс OLLIN Professional от 03.10.2024.pdf'  # Укажите путь к вашему локальному PDF файлу
    pdf_file = FSInputFile(file_path)  # Загружаем файл с помощью FSInputFile
    await message.answer_document(document=pdf_file)  # Отправляем файл пользователю

@dp.message(lambda message: message.text == "Каталог процедур")
async def send_procedures_catalog_link(message: types.Message):
    # Создаем клавиатуру с кнопкой
    link_button = InlineKeyboardButton(
        text="Скачать каталог процедур",
        url="https://drive.google.com/file/d/1kgsxd8bG1DBGMCDNwYS55cVfGxKZCf9T/view?usp=drive_link"
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[link_button]])

    # Отправляем сообщение с кнопкой
    await message.answer(
        "Дорогие мастера, файл весит более 50мб, поэтому ловите на него ссылку с Google диска:",
        reply_markup=keyboard
    )

@dp.message(lambda message: message.text == "Технологическое досье")
async def send_technical_dossier_link(message: types.Message):
    # Создаем клавиатуру с кнопкой
    link_button = InlineKeyboardButton(
        text="Скачать технологическое досье",
        url="https://drive.google.com/file/d/1osh1v5nFNwIV-ebtLGlN4UtXEnZhiB5l/view?usp=drive_link"
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[link_button]])

    # Отправляем сообщение с кнопкой
    await message.answer(
        "Дорогие мастера, файл весит более 50мб, поэтому ловите на него ссылку с Google диска:",
        reply_markup=keyboard
    )

@dp.message(lambda message: message.text == "Химическая завивка")
async def send_chemical_perming_image(message: types.Message):
    image_url = 'https://drive.google.com/uc?export=view&id=1Qkyz-qKYC06JlDhgklxQNA3_9TdlS8vb'
    await message.answer_photo(photo=image_url)

@dp.message(lambda message: message.text == "Краска для бровей и ресниц")
async def send_eyebrow_and_eyelash_dye_image(message: types.Message):
    image_url = 'https://drive.google.com/uc?export=view&id=16UIDEikEJwVvUw2R13his-3kBd8z7UoU'
    await message.answer_photo(photo=image_url)

@dp.message(lambda message: message.text == "KONDOR")
async def send_kondor_info(message: types.Message):
    image_url = 'https://drive.google.com/uc?export=view&id=1-ZhXn_MVODAgGKYiFyVd6sT-EWXXItPX'
    await message.answer_photo(photo=image_url)

    # Отправляем текст пользователю
    await message.answer(
        "«KONDOR» – это олицетворение настоящего мужчины: сильного, волевого, умного и бескомпромиссного, который идет к своей цели через все преграды и непременно ее добивается. Он думает не только о себе, но и о других, ведь есть честь и достоинство на все времена. Есть чувство долга и отзывчивость, прямота и искренность, есть обещания, которые дают и никогда не нарушают. Есть свобода во всех ее проявлениях и поступки, отличающие настоящих мужчин. Мужчин высокого полета, мужчин в стиле «KONDOR».",
        reply_markup=kondor_keyboard
    )

@dp.message(lambda message: message.text == "Стайлинг")
async def send_styling_image(message: types.Message):
    image_url = 'https://drive.google.com/uc?export=view&id=1u1-9WJQbrIMuoAcfkS30cYUyMrJpEx-A'
    await message.answer_photo(photo=image_url)

@dp.message(lambda message: message.text == "Бритье и уход за бородой")
async def send_shaving_beard_care_image(message: types.Message):
    image_url = 'https://drive.google.com/uc?export=view&id=1oDsqppvbauJnhiMhAxog2URGsWIJd06c'
    await message.answer_photo(photo=image_url)  # Отправляем картинку пользователю

@dp.message(lambda message: message.text == "Очищение и уход за волосами")
async def send_hair_cleansing_care_images(message: types.Message):
    images = [
        'https://drive.google.com/uc?export=view&id=10RvMPh7B9WRmjp9J81qj718QCIGZKfts',
        'https://drive.google.com/uc?export=view&id=1h4dPK1ZbMnDM-sQ6mJFNovWx3lL-68g1'
    ]
    for image in images:
        await message.answer_photo(photo=image)  # Отправляем каждую картинку пользователю

@dp.message(lambda message: message.text == "Камуфляж седины")
async def send_grey_camouflage_image(message: types.Message):
    image_url = 'https://drive.google.com/uc?export=view&id=13dj9cEH20CPfHA6o9YRZQxUPyeuYtP2u'
    await message.answer_photo(photo=image_url)  # Отправляем картинку пользователю

@dp.message(lambda message: message.text == "🎓 Обучение")
async def send_training_videos_menu(message: types.Message):
    await message.answer("Выберите обучающее видео:", reply_markup=training_videos_keyboard)

# Обработчик команды "💰 Прайсы"
@dp.message(lambda message: message.text == "💰 Прайсы")
async def send_price_menu(message: types.Message):
    await message.answer("Выберите прайс:", reply_markup=price_keyboard)

@dp.message(lambda message: message.text == "Прайс OLLIN Professional")
async def send_ollin_price_link(message: types.Message):
    # Создаем клавиатуру с кнопкой
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Скачать прайс OLLIN Professional",
                url="https://drive.google.com/file/d/1JAyjKlilaC5T2PVp2rmMdy3gqEPn0Ofh/view?usp=drive_link"  # Замените your_file_id на реальный идентификатор файла
            )
        ]
    ])

    # Отправляем сообщение с кнопкой
    await message.answer(
        "Дорогие мастера, для скачивания прайса OLLIN Professional нажмите на кнопку ниже:",
        reply_markup=keyboard
    )

@dp.message(lambda message: message.text == "Прайс Hair SEKTA")
async def send_hair_sekta_price_link(message: types.Message):
    # Создаем клавиатуру с кнопкой
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Скачать Прайс Hair SEKTA", url="https://drive.google.com/file/d/19TeozLhvtYoCJty7fqHz3xr0WnEtzXL8/view?usp=drive_link")]
    ])

    # Отправляем сообщение с кнопкой
    await message.answer(
        "Дорогие мастера, прайс Hair SEKTA доступен по следующей ссылке:",
        reply_markup=keyboard
    )
# Обработчик команды "🛠 Поддержка"
@dp.message(lambda message: message.text == "🛠 Поддержка")
async def send_support_menu(message: types.Message):
    await message.answer("Свяжитесь с поддержкой:", reply_markup=support_keyboard)

@dp.message(lambda message: message.text == "Консультация по продукции - Светлана")
async def send_product_consultation_contact(message: types.Message):
    await message.answer(
        "Для консультации по продукции воспользуйтесь следующим контактом: [Светлана](https://t.me/Ponsicsv)",
        parse_mode="Markdown"
    )

@dp.message(lambda message: message.text == "Поддержка бота - Макс")
async def send_support_contact(message: types.Message):
    await message.answer(
        "Для связи с поддержкой воспользуйтесь следующим контактом: [Поддержка](https://t.me/Policekadafi)",
        parse_mode="Markdown"
    )

# Обработчик команды "🦊 Лисичка"
@dp.message(lambda message: message.text == "🦊 Лисичка")
async def send_fox(message: types.Message):
    fox_image = await fox()
    if fox_image:
        await message.answer_photo(photo=fox_image, caption="Вот тебе случайная лисичка!")
    else:
        await message.answer("Лисичка в норке.")

# Обработчик кнопки "Назад"
@dp.message(lambda message: message.text == "Назад")
async def go_back(message: types.Message):
    # Возврат в главное меню
    await message.answer("Возврат в главное меню", reply_markup=main_keyboard)

# Основная функция запуска бота
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
