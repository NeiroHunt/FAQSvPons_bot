from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Клавиатура с единственной кнопкой "Пуск"
start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Пуск")]
    ],
    resize_keyboard=True
)

# Клавиатура после команды "Пуск"
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📦 Продукты компании"), KeyboardButton(text="🎓 Обучение")],
        [KeyboardButton(text="💰 Прайсы"), KeyboardButton(text="🛠 Поддержка")],
        [KeyboardButton(text="🦊 Лисичка")]
    ],
    resize_keyboard=True
)

# Клавиатура для команды "Продукты компании"
product_company_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="OLLIN Professional"), KeyboardButton(text="Hair SEKTA")],
        [KeyboardButton(text="KONDOR"), KeyboardButton(text="Расходники")],
        [KeyboardButton(text="Другие продукты компании")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

ollin_professional_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Красители, порошки и оксиды"), KeyboardButton(text="Техническая линия")],
        [KeyboardButton(text="Уход за волосами"), KeyboardButton(text="Лечение волос и кожи головы")],
        [KeyboardButton(text="STYLE Стайлинги"), KeyboardButton(text="Химическая завивка")],
        [KeyboardButton(text="Краска для бровей и ресниц"), KeyboardButton(text="Продукты Retail")],
        [KeyboardButton(text="Оборудование для укладки волос")],
        [KeyboardButton(text="X-PLEX комплекс продуктов для восстановления и сохранения здоровья волос")],
        [KeyboardButton(text="Прайс"), KeyboardButton(text="Каталог процедур")],
        [KeyboardButton(text="Технологическое досье")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Клавиатура для обучающих видео
training_videos_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Видео 1")],
        [KeyboardButton(text="Видео 2")],
        [KeyboardButton(text="Видео 3")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Клавиатура для прайсов
price_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Прайс OLLIN Professional"), KeyboardButton(text="Прайс Hair SEKTA")],
        [KeyboardButton(text="Прайс Kondor"), KeyboardButton(text="Прайс Расходники")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Клавиатура для поддержки
support_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Поддержка бота - Макс"), KeyboardButton(text="Консультация по продукции - Светлана")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Клавиатура для случайной лисички
fox_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Получить лисичку")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Клавиатура для подкатегорий "Красители, порошки и оксиды"
coloring_powders_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Краситель COLOR"), KeyboardButton(text="Краситель PERFORMANCE")],
        [KeyboardButton(text="Краситель N - JOY"), KeyboardButton(text="Краситель SILK TOUCH")],
        [KeyboardButton(text="Краситель MEGAPOLIS"), KeyboardButton(text="MATISSE COLOR")],
        [KeyboardButton(text="Осветляющие порошки")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Клавиатура для подкатегорий "Техническая линия"
technical_line_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Service Line"), KeyboardButton(text="Химическая завивка")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Клавиатура для команды "Уход за волосами"
hair_care_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="CARE"), KeyboardButton(text="Ultimate CARE")],
        [KeyboardButton(text="BASIC LINE"), KeyboardButton(text="BIONIKA")],
        [KeyboardButton(text="PERFECT HAIR"), KeyboardButton(text="MEGAPOLIS")],
        [KeyboardButton(text="Coctail BAR"), KeyboardButton(text="CURL & SMOOTH HAIR")],
        [KeyboardButton(text="INTENSE Profi COLOR"), KeyboardButton(text="PREMIER FOR MEN")],
        [KeyboardButton(text="SALON BEAUTY"), KeyboardButton(text="SHINE BLOND")],
        [KeyboardButton(text="Уход за натуральным блондом и осветленными волосами")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Клавиатура для лечения волос и кожи головы
hair_treatment_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Anti Hair Loss"), KeyboardButton(text="Anti Dandruff")],
        [KeyboardButton(text="Double Hydration"), KeyboardButton(text="Color Protection")],
        [KeyboardButton(text="Daily Use"), KeyboardButton(text="Balance")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Клавиатура для стайлингов STYLE
style_styling_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Лак для волос"), KeyboardButton(text="Мусс для укладки")],
        [KeyboardButton(text="Гель для укладки"), KeyboardButton(text="Воск для укладки")],
        [KeyboardButton(text="Спрей для объема"), KeyboardButton(text="Термозащита")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Клавиатура для категории "Химическая завивка"
chemical_perming_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Средство для химической завивки"), KeyboardButton(text="Нейтрализатор")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Клавиатура для X-PLEX комплекса
xplex_care_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Шампунь X-PLEX"), KeyboardButton(text="Кондиционер X-PLEX")],
        [KeyboardButton(text="Маска X-PLEX")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)

# Клавиатура для команды "KONDOR"
kondor_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Стайлинг"), KeyboardButton(text="Бритье и уход за бородой")],
            [KeyboardButton(text="Очищение и уход за волосами"), KeyboardButton(text="Камуфляж седины")],
        [KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)