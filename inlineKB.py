from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def create_inline_keyboard_section_1():
    buttons = [
        InlineKeyboardButton("Примеры видео уроков", callback_data="section_21"),
        InlineKeyboardButton("Полезная рассылка", callback_data="section_22"),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data="section_23")
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_21():
    buttons = [
        InlineKeyboardButton("Высшая математика", callback_data="section_31"),
        InlineKeyboardButton("Физика", callback_data="section_32"),
        InlineKeyboardButton("Программирование", callback_data="section_33"),
        InlineKeyboardButton("Линал & Ангем", callback_data="section_441"),
        InlineKeyboardButton("Тервер & Матстат", callback_data="section_451"),
        InlineKeyboardButton("Матфиз", callback_data="section_561"),
        InlineKeyboardButton("Химия & органич. химия", callback_data="section_37"),
        InlineKeyboardButton("Физхим", callback_data="section_38"),
        InlineKeyboardButton("Экономическое направление", callback_data='section_39'),
        InlineKeyboardButton("Назад", callback_data='section_1')
    ]
    return InlineKeyboardMarkup().add(*buttons)

#Высшая математика


def create_inline_keyboard_section_31():
    buttons = [
        InlineKeyboardButton("интегралы & кратные интегралы", callback_data='section_41'),
        InlineKeyboardButton("ряды & ТФКП", callback_data='section_42'),
        InlineKeyboardButton("диффуры", callback_data='section_43'),
        InlineKeyboardButton("пределы & производные + фнп", callback_data='section_44'),
        InlineKeyboardButton("Назад", callback_data='section_21')
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_41():
    buttons = [
        InlineKeyboardButton("Разбор еще одной задачи", callback_data='section_51'),
        InlineKeyboardButton("Купить курс", callback_data='section_61'),
        InlineKeyboardButton("Назад", callback_data='section_31'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_42():
    buttons = [
        InlineKeyboardButton("Разбор еще одной задачи", callback_data='section_52'),
        InlineKeyboardButton("Купить курс", callback_data='section_62'),
        InlineKeyboardButton("Назад", callback_data='section_31'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_43():
    buttons = [
        InlineKeyboardButton("Разбор еще одной задачи", callback_data='section_53'),
        InlineKeyboardButton("Купить курс", callback_data='section_63'),
        InlineKeyboardButton("Назад", callback_data='section_31'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_44():
    buttons = [
        InlineKeyboardButton("Разбор еще одной задачи", callback_data='section_54'),
        InlineKeyboardButton("Купить курс", callback_data='section_64'),
        InlineKeyboardButton("Назад", callback_data='section_31'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_51():
    buttons = [
        InlineKeyboardButton("Купить курс", callback_data='section_61'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_41'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_52():
    buttons = [
        InlineKeyboardButton("Купить курс", callback_data='section_62'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_42'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_53():
    buttons = [
        InlineKeyboardButton("Купить курс", callback_data='section_63'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_43'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_54():
    buttons = [
        InlineKeyboardButton("Купить курс", callback_data='section_64'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_44'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_61():
    buttons = [
        InlineKeyboardButton("Оптимум", callback_data='section_711'),
        InlineKeyboardButton("Ультра", callback_data='section_721'),
        InlineKeyboardButton("Хочу в рассрочку", callback_data='section_73'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_41'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_62():
    buttons = [
        InlineKeyboardButton("Оптимум", callback_data='section_712'),
        InlineKeyboardButton("Ультра", callback_data='section_722'),
        InlineKeyboardButton("Хочу в рассрочку", callback_data='section_73'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_42'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_63():
    buttons = [
        InlineKeyboardButton("Оптимум", callback_data='section_713'),
        InlineKeyboardButton("Ультра", callback_data='section_723'),
        InlineKeyboardButton("Хочу в рассрочку", callback_data='section_73'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_43'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_64():
    buttons = [
        InlineKeyboardButton("Оптимум", callback_data='section_714'),
        InlineKeyboardButton("Ультра", callback_data='section_724'),
        InlineKeyboardButton("Хочу в рассрочку", callback_data='section_73'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_44'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_711():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=integraly&cost=discountplusterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_61')
        ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_712():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=integraly&cost=discountproterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_62')
        ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_713():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=ryady&cost=discountplusterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_63')
        ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_714():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=ryady&cost=discountproterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_64')
        ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_721():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=dif-i-raz-uravneniya&cost=discountplusterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_61'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_722():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=dif-i-raz-uravneniya&cost=discountproterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_62'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_723():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=pip&cost=discountplusterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_63'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_724():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=pip&cost=discountproterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_64'),
    ]
    return InlineKeyboardMarkup().add(*buttons)

#Физика


def create_inline_keyboard_section_32():
    buttons = [
        InlineKeyboardButton("Электричество", callback_data='section_411'),
        InlineKeyboardButton("Магнетизм", callback_data='section_412'),
        InlineKeyboardButton("МКТ", callback_data='section_413'),
        InlineKeyboardButton("Кинематика", callback_data='section_414'),
        InlineKeyboardButton("Динамика", callback_data='section_415'),
        InlineKeyboardButton("Назад", callback_data='section_21')
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_411():
    buttons = [
        InlineKeyboardButton("Разбор еще одной задачи", callback_data='section_511'),
        InlineKeyboardButton("Купить курс", callback_data='section_611'),
        InlineKeyboardButton("Назад", callback_data='section_32'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_412():
    buttons = [
        InlineKeyboardButton("Разбор еще одной задачи", callback_data='section_512'),
        InlineKeyboardButton("Купить курс", callback_data='section_611'),
        InlineKeyboardButton("Назад", callback_data='section_32'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_413():
    buttons = [
        InlineKeyboardButton("Разбор еще одной задачи", callback_data='section_513'),
        InlineKeyboardButton("Купить курс", callback_data='section_611'),
        InlineKeyboardButton("Назад", callback_data='section_32'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_414():
    buttons = [
        InlineKeyboardButton("Разбор еще одной задачи", callback_data='section_514'),
        InlineKeyboardButton("Купить курс", callback_data='section_611'),
        InlineKeyboardButton("Назад", callback_data='section_32'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_415():
    buttons = [
        InlineKeyboardButton("Разбор еще одной задачи", callback_data='section_515'),
        InlineKeyboardButton("Купить курс", callback_data='section_611'),
        InlineKeyboardButton("Назад", callback_data='section_32'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_511():
    buttons = [
        InlineKeyboardButton("Купить курс", callback_data='section_611'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_411'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_512():
    buttons = [
        InlineKeyboardButton("Купить курс", callback_data='section_611'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_412'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_513():
    buttons = [
        InlineKeyboardButton("Купить курс", callback_data='section_611'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_413'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_514():
    buttons = [
        InlineKeyboardButton("Купить курс", callback_data='section_611'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_414'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_515():
    buttons = [
        InlineKeyboardButton("Купить курс", callback_data='section_611'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_415'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_611():
    buttons = [
        InlineKeyboardButton("Оптимум", callback_data='section_731'),
        InlineKeyboardButton("Ультра", callback_data='section_732'),
        InlineKeyboardButton("Хочу в рассрочку", callback_data='section_73'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_32'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_731():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=fizika&cost=discountproterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_32'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_732():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=fizika&cost=discountproterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_32'),
    ]
    return InlineKeyboardMarkup().add(*buttons)

#Программирование


def create_inline_keyboard_section_33():
    buttons = [
        InlineKeyboardButton("C++", callback_data='section_431'),
        InlineKeyboardButton("Python", callback_data='section_432'),
        InlineKeyboardButton("SQL", callback_data='section_433'),
        InlineKeyboardButton("Назад", callback_data='section_21')
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_431():
    buttons = [
        InlineKeyboardButton("Разбор еще одной задачи", callback_data='section_531'),
        InlineKeyboardButton("Купить курс", callback_data='section_631'),
        InlineKeyboardButton("Назад", callback_data='section_33'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_531():
    buttons = [
        InlineKeyboardButton("Купить курс", callback_data='section_631'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_431'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_631():
    buttons = [
        InlineKeyboardButton("Оптимум", callback_data='section_741'),
        InlineKeyboardButton("Ультра", callback_data='section_742'),
        InlineKeyboardButton("Хочу в рассрочку", callback_data='section_73'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_33'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_741():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=c&cost=discountplusterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_33'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_742():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=c&cost=discountproterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_33'),
    ]
    return InlineKeyboardMarkup().add(*buttons)

#Линал


def create_inline_keyboard_section_441():
    buttons = [
        InlineKeyboardButton("Разбор еще одной задачи", callback_data='section_541'),
        InlineKeyboardButton("Купить курс", callback_data='section_641'),
        InlineKeyboardButton("Назад", callback_data='section_21'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_541():
    buttons = [
        InlineKeyboardButton("Купить курс", callback_data='section_641'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_441'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_641():
    buttons = [
        InlineKeyboardButton("Оптимум", callback_data='section_751'),
        InlineKeyboardButton("Ультра", callback_data='section_752'),
        InlineKeyboardButton("Хочу в рассрочку", callback_data='section_73'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_441'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_751():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=c&cost=discountplusterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_441'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_752():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=c&cost=discountproterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_441'),
    ]
    return InlineKeyboardMarkup().add(*buttons)

#Тервер и матстат


def create_inline_keyboard_section_451():
    buttons = [
        InlineKeyboardButton("Разбор еще одной задачи", callback_data='section_551'),
        InlineKeyboardButton("Купить курс", callback_data='section_651'),
        InlineKeyboardButton("Назад", callback_data='section_21'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_551():
    buttons = [
        InlineKeyboardButton("Купить курс", callback_data='section_651'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_451'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_651():
    buttons = [
        InlineKeyboardButton("Оптимум", callback_data='section_761'),
        InlineKeyboardButton("Ультра", callback_data='section_762'),
        InlineKeyboardButton("Хочу в рассрочку", callback_data='section_73'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_451'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_761():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=terver&cost=discountplusterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_441'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_762():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=terver&cost=discountproterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_441'),
    ]
    return InlineKeyboardMarkup().add(*buttons)

#Матфиз


def create_inline_keyboard_section_561():
    buttons = [
        InlineKeyboardButton("Купить курс", callback_data='section_661'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_451'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_661():
    buttons = [
        InlineKeyboardButton("Оптимум", callback_data='section_771'),
        InlineKeyboardButton("Ультра", callback_data='section_772'),
        InlineKeyboardButton("Хочу в рассрочку", callback_data='section_73'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_561'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_771():
    buttons = [
        InlineKeyboardButton("Оплата", url=" https://math-club.ru/signup.php?course=matfiz&cost=discountplusterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_561'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_772():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=matfiz&cost=discountproterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_561'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


#Химия и органическая химия


def create_inline_keyboard_section_37():
    buttons = [
        InlineKeyboardButton("Химия", callback_data='section_491'),
        InlineKeyboardButton("Органическая химия", callback_data='section_491'),
        InlineKeyboardButton("Назад", callback_data='section_21')
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_38():
    buttons = [
        InlineKeyboardButton("Купить курс", callback_data='section_381'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_21'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_481():
    buttons = [
        InlineKeyboardButton("Оптимум", callback_data='section_581'),
        InlineKeyboardButton("Ультра", callback_data='section_582'),
        InlineKeyboardButton("Хочу в рассрочку", callback_data='section_73'),
        InlineKeyboardButton("Связаться с отделом заботы", callback_data='section_23'),
        InlineKeyboardButton("Назад", callback_data='section_38'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_581():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=fizchem&cost=discountplusterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_481'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_582():
    buttons = [
        InlineKeyboardButton("Оплата", url="https://math-club.ru/signup.php?course=fizchem&cost=discountproterm&utm_source=tg"),
        InlineKeyboardButton("Назад", callback_data='section_481'),
    ]
    return InlineKeyboardMarkup().add(*buttons)

#Экономика


def create_inline_keyboard_section_39():
    buttons = [
        InlineKeyboardButton("Микроэкономика", callback_data='section_491'),
        InlineKeyboardButton("Макроэкономика", callback_data='section_492'),
        InlineKeyboardButton("Экономика", callback_data='section_493'),
        InlineKeyboardButton("Финуч", callback_data='section_494'),
        InlineKeyboardButton("Назад", callback_data='section_21'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_22():
    buttons = [
        InlineKeyboardButton("Высшая математика", callback_data='section_1001'),
        InlineKeyboardButton("Физика", callback_data='section_1002'),
        InlineKeyboardButton("Пограммирование", callback_data='section_1003'),
        InlineKeyboardButton("Экономическое направление", callback_data='section_1004'),
        InlineKeyboardButton("Линал & Ангем", callback_data='section_1000'),
        InlineKeyboardButton("Тервер & Матстат", callback_data='section_1000'),
        InlineKeyboardButton("Матфиз", callback_data='section_1000'),
        InlineKeyboardButton("Химия & органич. химия", callback_data='section_1000'),
        InlineKeyboardButton("Физхим", callback_data='section_1000'),
        InlineKeyboardButton("Назад", callback_data='section_1'),
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_1001():
    buttons = [
        InlineKeyboardButton("интегралы & кратные интегралы", callback_data='section_1000'),
        InlineKeyboardButton("ряды & ТФКП", callback_data='section_1000'),
        InlineKeyboardButton("диффуры", callback_data='section_1000'),
        InlineKeyboardButton("пределы & производные + фнп", callback_data='section_1000'),
        InlineKeyboardButton("Назад", callback_data='section_22')
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_1002():
    buttons = [
        InlineKeyboardButton("Электричество", callback_data='section_1000'),
        InlineKeyboardButton("Магнетизм", callback_data='section_1000'),
        InlineKeyboardButton("МКТ", callback_data='section_1000'),
        InlineKeyboardButton("Кинематика", callback_data='section_1000'),
        InlineKeyboardButton("Динамика", callback_data='section_1000'),
        InlineKeyboardButton("Назад", callback_data='section_22')
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_1003():
    buttons = [
        InlineKeyboardButton("C++", callback_data='section_1000'),
        InlineKeyboardButton("Python", callback_data='section_1000'),
        InlineKeyboardButton("SQL", callback_data='section_1000'),
        InlineKeyboardButton("Назад", callback_data='section_22')
    ]
    return InlineKeyboardMarkup().add(*buttons)


def create_inline_keyboard_section_1004():
    buttons = [
        InlineKeyboardButton("Микроэкономика", callback_data='section_1000'),
        InlineKeyboardButton("Макроэкономика", callback_data='section_1000'),
        InlineKeyboardButton("Экономика", callback_data='section_1000'),
        InlineKeyboardButton("Финуч", callback_data='section_1000'),
        InlineKeyboardButton("Назад", callback_data='section_22'),
    ]
    return InlineKeyboardMarkup().add(*buttons)
