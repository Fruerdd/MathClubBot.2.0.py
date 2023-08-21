import aiogram
from aiogram.types import message

priceUltra = 9900
priceOptimum = 5500
HELP_TEXT = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>начинаем разговорчики</em>
<b>/description</b> - <em>описание бота</em>
<b>/photo</b> - <em>отправка фото</em>
"""
START_TEXT = """
На связи команда Math Club. Мы создаем онлайн-школу с совершенно новым подходом к подготовке к экзаменам. 

Прописывая тексты для этого бота, мы постарались вложить частичку себя:
📚Наши преподаватели записали примеры видеоуроков
💡SMM-специалисты подготовили полезные подборки и лайфхак
🍀Отдел заботы готов отвечать на твои сообщения и вопросы в любой день недели

Знаешь, что еще важно?

У нас нет отдела продаж, поэтому никто не будет старательно впаривать то, что тебе совершенно не нужно 🙏

Давай определимся, что тебе интересно сейчас. Кликай в нужный вариант из списка ниже:
"""

START_VIDEOS: str = """
“Так просто?” - это фраза, которую чаще всего произносят наши студенты. Секрет прост - мы сами проходили этот путь и
понимаем, что зачастую на парах хочется сойти с ума от терминов и усталости, а лежащий мобильный 
телефон предательски манит 😋

Мы уже подготовили тебе примеры видеоуроков, выбери раздел, чтобы получить нужный видеоурок!
"""

MATH31: str = """
Теперь выбери интересующую тебя тему Вышмата, чтобы получить именно то, что нужно📚
"""

MATH41: str = """
Желание всё бросить, стрессы, риск отчисления и слезы - неприятные аспекты высшего образования.

Благодаря нашим преподавателям мы сделали крутые онлайн-курсы, которые помогают подготовиться и сдать сессию, даже если дела совсем плохи.

Приглашаем посмотреть разбор задачи по теме "Интегрирование по частям"

👉Нажимай кнопку "Разбор еще одной задачи" и смотри разбор еще одного номера по теме "Замена переменных"

👉Хочешь успешно подготовиться к сессии с нами? Тогда твоя кнопка "Купить курс"
"""
MATH42: str = """
Желание всё бросить, стрессы, риск отчисления и слезы - неприятные аспекты высшего образования.

Благодаря нашим преподавателям мы сделали крутые онлайн-курсы, которые помогают подготовиться и сдать сессию, даже если дела совсем плохи.

Приглашаем посмотреть разбор задачи по теме "Вычисление суммы ряда"

👉Нажимай кнопку "Разбор еще одной задачи" и смотри разбор еще одного номера по теме "Геометрическая прогрессия и признак Коши"

👉Хочешь успешно подготовиться к сессии с нами? Тогда твоя кнопка "Купить курс"
"""
MATH43: str = """
Желание всё бросить, стрессы, риск отчисления и слезы - неприятные аспекты высшего образования.

Благодаря нашим преподавателям мы сделали крутые онлайн-курсы, которые помогают подготовиться и сдать сессию, даже если дела совсем плохи.

Приглашаем посмотреть разбор задачи по теме "Разделение переменных в дифференциальных уравнениях"

👉Нажимай кнопку "Разбор еще одной задачи" и смотри разбор еще одного номера по теме "Метод Бернулли"

👉Хочешь успешно подготовиться к сессии с нами? Тогда твоя кнопка "Купить курс"
"""
MATH44: str = """
Желание всё бросить, стрессы, риск отчисления и слезы - неприятные аспекты высшего образования.

Благодаря нашим преподавателям мы сделали крутые онлайн-курсы, которые помогают подготовиться и сдать сессию, даже если дела совсем плохи.

Приглашаем посмотреть разбор задачи по теме "Правило Лопиталя и как его не надо применять"

👉Нажимай кнопку "Разбор еще одной задачи" и смотри разбор еще одного номера по теме "Вычисление пределов методом замены на эквивалент"

👉Хочешь успешно подготовиться к сессии с нами? Тогда твоя кнопка "Купить курс"
"""
MATH51: str = """
Помни, экзамены не так ужасны, даже если сейчас очень хочется все бросить! Мы поможем подобрать оптимальный план обучения и быть во всеоружии на сессии!
Лови разбор ВТОРОГО номера по теме “Вычисление пределов методом замены на эквивалент”

👉Чтобы присоединиться к продуктивной подготовке - жми "Купить курс"
"""
MATH52: str = """
Помни, экзамены не так ужасны, даже если сейчас очень хочется все бросить! Мы поможем подобрать оптимальный план обучения и быть во всеоружии на сессии!

Лови разбор ВТОРОГО номера по теме “Геометрическая прогрессия и признак Коши”

👉Чтобы присоединиться к продуктивной подготовке - жми "Купить курс"
"""
MATH53: str = """
Помни, экзамены не так ужасны, даже если сейчас очень хочется все бросить! Мы поможем подобрать оптимальный план обучения и быть во всеоружии на сессии!
Лови разбор ВТОРОГО номера

А вот и разбор задачи по теме “Метод Бернулли”

👉Чтобы присоединиться к продуктивной подготовке - жми "Купить курс"
"""
MATH54: str = """
Помни, экзамены не так ужасны, даже если сейчас очень хочется все бросить! Мы поможем подобрать оптимальный план обучения и быть во всеоружии на сессии!
Лови разбор ВТОРОГО номера по теме “Вычисление пределов методом замены на эквивалент”

👉Чтобы присоединиться к продуктивной подготовке - жми "Купить курс"
"""
MATH61: str = f"""
У нас есть два тарифа - Оптимум и Ультра.

😸Тариф "Оптимум" - это доступ к нашей платформе, где хранятся видеоуроки со всей теорией и практикой, онлайн-занятия в группе с преподавателем, а также домашки с проверкой и помощь в чате по любым вопросам. Доступ к нему предоставляется до конца сессии, чтобы быть во всеоружии. Его стоимость {priceOptimum} рублей

🐯Тариф "Ультра" помимо всего, что есть в "Оптимум" включает в себя еще два индивидуальных занятия с преподавателем. Одно занятие длится примерно 80 минут (иногда меньше) до полного понимания темы. Доступ к тарифу тоже предоставляется до конца сессии. Его стоимость {priceUltra} рублей

Не забудь почитать отзывы учеников: https://vk.com/math.university?w=app6326142_-204535334
"""
MATH62: str = f"""
У нас есть два тарифа - Оптимум и Ультра.

😸Тариф "Оптимум" - это доступ к нашей платформе, где хранятся видеоуроки со всей теорией и практикой, онлайн-занятия в группе с преподавателем, а также домашки с проверкой и помощь в чате по любым вопросам. Доступ к нему предоставляется до конца сессии, чтобы быть во всеоружии. Его стоимость {priceOptimum} рублей

🐯Тариф "Ультра" помимо всего, что есть в "Оптимум" включает в себя еще два индивидуальных занятия с преподавателем. Одно занятие длится примерно 80 минут (иногда меньше) до полного понимания темы. Доступ к тарифу тоже предоставляется до конца сессии. Его стоимость {priceUltra} рублей

Не забудь почитать отзывы учеников: https://vk.com/math.university?w=app6326142_-204535334
"""
MATH63: str = f"""
У нас есть два тарифа - Оптимум и Ультра.

😸Тариф "Оптимум" - это доступ к нашей платформе, где хранятся видеоуроки со всей теорией и практикой, онлайн-занятия в группе с преподавателем, а также домашки с проверкой и помощь в чате по любым вопросам. Доступ к нему предоставляется до конца сессии, чтобы быть во всеоружии. Его стоимость {priceOptimum} рублей

🐯Тариф "Ультра" помимо всего, что есть в "Оптимум" включает в себя еще два индивидуальных занятия с преподавателем. Одно занятие длится примерно 80 минут (иногда меньше) до полного понимания темы. Доступ к тарифу тоже предоставляется до конца сессии. Его стоимость {priceUltra} рублей

Не забудь почитать отзывы учеников: https://vk.com/math.university?w=app6326142_-204535334
"""
MATH64: str = f"""
У нас есть два тарифа - Оптимум и Ультра.

😸Тариф "Оптимум" - это доступ к нашей платформе, где хранятся видеоуроки со всей теорией и практикой, онлайн-занятия в группе с преподавателем, а также домашки с проверкой и помощь в чате по любым вопросам. Доступ к нему предоставляется до конца сессии, чтобы быть во всеоружии. Его стоимость {priceOptimum} рублей

🐯Тариф "Ультра" помимо всего, что есть в "Оптимум" включает в себя еще два индивидуальных занятия с преподавателем. Одно занятие длится примерно 80 минут (иногда меньше) до полного понимания темы. Доступ к тарифу тоже предоставляется до конца сессии. Его стоимость {priceUltra} рублей

Не забудь почитать отзывы учеников: https://vk.com/math.university?w=app6326142_-204535334
"""
MATH71: str = f""", регистрация и оплата на нашей платформе по кнопке ниже.

Как и писали ранее, сумма к оплате {priceOptimum} рублей

После оплаты пришли в этот чат, пожалуйста, скриншот квитанции об оплате, чтобы мы быстрее проверили твой платеж в системе, добавили на платформу и в чат с преподавателем
"""
MATH72: str = f""", регистрация и оплата на нашей платформе по кнопке ниже.

Как и писали ранее, сумма к оплате {priceUltra} рублей

После оплаты пришли в этот чат, пожалуйста, скриншот квитанции об оплате, чтобы мы быстрее проверили твой платеж в системе, добавили на платформу и в чат с преподавателем
"""
MATH81: str = """
Открываем доступ к твоему чату отделу заботы. Свободный сотрудник уже скоро напишет тебе. Вы обсудите твою ситуацию, план подготовки, чем и как мы можем помочь 😌

Пока мы бежим к тебе - опиши свой запрос)
"""


PHYS32: str = """Теперь выбери интересующую тебя тему университетской физики, чтобы получить именно то, что нужно📚"""
PHYS411: str = """
Желание всё бросить, стрессы, риск отчисления и слезы - неприятные аспекты высшего образования.

Благодаря нашим преподавателям мы сделали крутые онлайн-курсы, которые помогают подготовиться и сдать сессию, даже если дела совсем плохи.

Приглашаем посмотреть разбор задачи по теме "Сопоставление электростатического и гравитационного притяжения"

👉Нажимай кнопку "Разбор еще одной задачи" и смотри разбор еще одного номера по теме "Закон кулона в задачах о равновесии заряженных частиц"

👉Хочешь успешно подготовиться к сессии с нами? Тогда твоя кнопка "Купить курс"
"""
PHYS412: str = """
Желание всё бросить, стрессы, риск отчисления и слезы - неприятные аспекты высшего образования.

Благодаря нашим преподавателям мы сделали крутые онлайн-курсы, которые помогают подготовиться и сдать сессию, даже если дела совсем плохи.

Приглашаем посмотреть разбор задачи по теме "Напряжённость магнитного поля и принцип суперпозиции"

👉Нажимай кнопку "Разбор еще одной задачи" и смотри разбор еще одного номера по теме "Нахождение напряжённости магнитного поля на расстоянии от кругового витка"

👉Хочешь успешно подготовиться к сессии с нами? Тогда твоя кнопка "Купить курс"
"""
PHYS413: str = """
Желание всё бросить, стрессы, риск отчисления и слезы - неприятные аспекты высшего образования.

Благодаря нашим преподавателям мы сделали крутые онлайн-курсы, которые помогают подготовиться и сдать сессию, даже если дела совсем плохи.

Приглашаем посмотреть разбор задачи по теме "Использование уравнения состояния для нахождения концентраций"

👉Нажимай кнопку "Разбор еще одной задачи" и смотри разбор еще одного номера по теме "Уравнение Менделеева-Клапейрона"

👉Хочешь успешно подготовиться к сессии с нами? Тогда твоя кнопка "Купить курс"
"""
PHYS414: str = """
Желание всё бросить, стрессы, риск отчисления и слезы - неприятные аспекты высшего образования.

Благодаря нашим преподавателям мы сделали крутые онлайн-курсы, которые помогают подготовиться и сдать сессию, даже если дела совсем плохи.

Приглашаем посмотреть разбор задачи по теме "Свободно падающее тело"

👉Нажимай кнопку "Разбор еще одной задачи" и смотри разбор еще одного номера по теме "Кинематика вращательного движения"

👉Хочешь успешно подготовиться к сессии с нами? Тогда твоя кнопка "Купить курс"
"""
PHYS415: str = """
Желание всё бросить, стрессы, риск отчисления и слезы - неприятные аспекты высшего образования.

Благодаря нашим преподавателям мы сделали крутые онлайн-курсы, которые помогают подготовиться и сдать сессию, даже если дела совсем плохи.

Приглашаем посмотреть разбор задачи по теме "Динамика поступательного движения"

👉Нажимай кнопку "Разбор еще одной задачи" и смотри разбор еще одного номера по теме "Динамика вращательного движения"

👉Хочешь успешно подготовиться к сессии с нами? Тогда твоя кнопка "Купить курс"
"""
PHYS511: str = """
Держи разбор ВТОРОГО номера💙

Мы разберем задачу на тему "Закон кулона в задачах о равновесии заряженных частиц"

👉Чтобы присоединиться к продуктивной подготовке - жми "Купить курс"
"""
PHYS512: str = """
Держи разбор ВТОРОГО номера💙

Меньше чем за 5 минут мы разберем задачку на тему "Нахождение напряжённости магнитного поля на расстоянии от кругового витка"

👉Чтобы присоединиться к продуктивной подготовке - жми "Купить курс"
"""
PHYS513: str = """
Держи разбор ВТОРОГО номера💙

Всего за 3 минуты мы разберем задачку на тему "Уравнение Менделеева-Клапейрона"

👉Чтобы присоединиться к продуктивной подготовке - жми "Купить курс"
"""
PHYS514: str = """
Держи разбор ВТОРОГО номера💙

Всего за 3 минуты мы разберем задачку на тему "Кинематика вращательного движения"
"""
PHYS515: str = """
Держи разбор ВТОРОГО номера💙

Всего за 3 минуты мы разберем задачку на тему "Динамика вращательного движения"

👉Чтобы присоединиться к продуктивной подготовке - жми "Купить курс"
"""
PHYS611: str = f"""
У нас есть два тарифа - Оптимум и Ультра.

😸Тариф "Оптимум" - это доступ к нашей платформе, где хранятся видеоуроки со всей теорией и практикой, онлайн-занятия в группе с преподавателем, а также домашки с проверкой и помощь в чате по любым вопросам. Доступ к нему предоставляется до конца сессии, чтобы быть во всеоружии. Его стоимость {priceOptimum} рублей

🐯Тариф "Ультра" помимо всего, что есть в "Оптимум" включает в себя еще два индивидуальных занятия с преподавателем. Одно занятие длится примерно 80 минут (иногда меньше) до полного понимания темы. Доступ к тарифу тоже предоставляется до конца сессии. Его стоимость {priceUltra} рублей

Не забудь почитать отзывы учеников: https://vk.com/math.university?w=app6326142_-204535334
"""
PHYS731: str = f"""
, регистрация и оплата на нашей платформе по кнопке ниже.

Как и писали ранее, сумма к оплате {priceOptimum} рублей

После оплаты пришли в этот чат, пожалуйста, скриншот квитанции об оплате, чтобы мы быстрее проверили твой платеж в системе, добавили на платформу и в чат с преподавателем
"""
PHYS732: str = f"""
, регистрация и оплата на нашей платформе по кнопке ниже.

Как и писали ранее, сумма к оплате {priceUltra} рублей

После оплаты пришли в этот чат, пожалуйста, скриншот квитанции об оплате, чтобы мы быстрее проверили твой платеж в системе, добавили на платформу и в чат с преподавателем
"""

PROG33: str = """Теперь выбери интересующую тебя тему программирования, чтобы получить именно то, что нужно📚"""
PROG431: str = """
Желание всё бросить, стрессы, риск отчисления и слезы - неприятные аспекты высшего образования.

Благодаря нашим преподавателям мы сделали крутые онлайн-курсы, которые помогают подготовиться и сдать сессию, даже если дела совсем плохи.

Приглашаем посмотреть разбор задачи по теме "Указатели, основы программирования в С++"

👉Нажимай кнопку "Разбор еще одной задачи" и смотри разбор еще одного номера по теме "Типы данных и их модификаторы"

👉Хочешь успешно подготовиться к сессии с нами? Тогда твоя кнопка "Купить курс"
"""
PROG432: str = """К сожалению, это видео еще записывается 😔

Подскажи, может быть тебе интересны индивидуальные занятия или другие предметы?"""
PROG433: str = """К сожалению, это видео еще записывается 😔

Подскажи, может быть тебе интересны индивидуальные занятия или другие предметы?"""
PROG531: str = """
Держи разбор ВТОРОГО номера💙

Мы разберем задачу на тему "Типы данных и их модификаторы"

👉Чтобы присоединиться к продуктивной подготовке - жми "Купить курс"
"""
PROG631: str = f"""
У нас есть два тарифа - Оптимум и Ультра.

😸Тариф "Оптимум" - это доступ к нашей платформе, где хранятся видеоуроки со всей теорией и практикой, онлайн-занятия в группе с преподавателем, а также домашки с проверкой и помощь в чате по любым вопросам. Доступ к нему предоставляется до конца сессии, чтобы быть во всеоружии. Его стоимость {priceOptimum} рублей

🐯Тариф "Ультра" помимо всего, что есть в "Оптимум" включает в себя еще два индивидуальных занятия с преподавателем. Одно занятие длится примерно 80 минут (иногда меньше) до полного понимания темы. Доступ к тарифу тоже предоставляется до конца сессии. Его стоимость {priceUltra} рублей

Не забудь почитать отзывы учеников: https://vk.com/math.university?w=app6326142_-204535334
"""
PROG741: str = f""", регистрация и оплата на нашей платформе по кнопке ниже.

Как и писали ранее, сумма к оплате {priceOptimum} рублей

После оплаты пришли в этот чат, пожалуйста, скриншот квитанции об оплате, чтобы мы быстрее проверили твой платеж в системе, добавили на платформу и в чат с преподавателем"""
PROG742: str = f"""
, регистрация и оплата на нашей платформе по кнопке ниже.

Как и писали ранее, сумма к оплате {priceUltra} рублей

После оплаты пришли в этот чат, пожалуйста, скриншот квитанции об оплате, чтобы мы быстрее проверили твой платеж в системе, добавили на платформу и в чат с преподавателем
"""


