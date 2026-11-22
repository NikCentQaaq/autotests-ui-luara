from enum import StrEnum


class AllureEpic(StrEnum):
    UI = "UI"



class AllureFeature(StrEnum):
    MAIN_PAGE = "Главная страница"
    HEADER = "Шапка сайта"
    CATALOG = "Каталог"
    PRODUCT = "Карточка товара"
    SEARCH = "Поиск"
    CART = "Корзина"
    AUTHORIZATION = "Авторизация"
    PERSONAL_ACCOUNT = "Личный кабинет"
    FILTER = "Фильтрация"



class AllureStory(StrEnum):
    NAVIGATION = "Навигация"
    DISPLAY = "Отображение элементов"
    SEARCH = "Поиск"
    OPEN_PRODUCT = "Открытие товара"

    ADD_TO_CART = "Добавление товара"
    DELETE_PRODUCT = "Удаление товара"

    CHANGE_QUANTITY = "Изменение количества"
    CART_PRICE = "Цена корзины"

    OPEN_CATEGORY = "Открытие категории"
    SORT = "Сортировка каталога"
    PRICE_FILTER = "Фильтрация Цены"
    METALL_FILTER = 'Фильтрация Металла'
    FILTER = "Фильтрация"


    INVALID_LOGIN = "Вход с невалидными данными"
    LOGIN = "Вход"
    LOGOUT = "Выход"
    PROFILE = "Профиль"