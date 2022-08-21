import pytest
from pages.Main_page import MainPage
from config import TestData
from time import sleep


# Логотип Ozon виден на странице
def test_main_logo_on_page(driver):
    main_page = MainPage(driver)
    logo = main_page.is_visible(MainPage.MAIN_LOGO)
    assert logo == True

# Попадаем в раздел Выгодные предложения при клике по лого Ozon
def test_logo_ozon_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.MAIN_LOGO)
    title_of_window = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_MAIN_LOGO)
    assert title_of_window == True


# Кнопка "Каталог" видна на странице
def test_button_catalog_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.CATALOG)
    assert button == True


# Кнопка "Каталог" имеет верное название
def test_button_catalog_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.CATALOG)
    assert button_name == TestData.NAME_OF_BUTTON_CATALOG


# Кнопка Избранное видна на странице
def test_button_favourites_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.FAVOURITES)
    assert button == True


# Кнопка Избранное имеет верное название
def test_button_favourites_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.FAVOURITES)
    assert button_name == TestData.NAME_OF_BUTTON_FAVOURITES


# Кнопка локализации поиска видна на странице
def test_search_where_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.SEARCH_WHERE)
    assert button == True


# Строка поиска видна на странице
def test_search_on_page(driver):
    main_page = MainPage(driver)
    field_input = main_page.is_visible(MainPage.SEARCH_INPUT)
    assert field_input == True


# Кнопка подтверждения ввода в строку поиска видна на странице
def test_submit_search_on_page(driver):
    main_page = MainPage(driver)
    submit_search = main_page.is_visible(MainPage.SUBMIT_SEARCH)
    assert submit_search == True


# Кнопка Войти видна на странице
def test_entrance_on_page(driver):
    main_page = MainPage(driver)
    entrance = main_page.is_visible(MainPage.ENTRANCE)
    assert entrance == True


# Кнопка Войти имеет верное название
def test_button_entrance_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.ENTRANCE)
    assert button_name == TestData.NAME_OF_BUTTON_ENTRANCE


# При наведении на кнопку Войти появляется всплывающее окно
def test_popup_window_appear(driver):
    main_page = MainPage(driver)
    main_page.show_popup_window(MainPage.ENTRANCE)
    popup_window = main_page.is_visible(MainPage.POPUP_WINDOW_ENTRANCE)
    assert popup_window == True

# Всплывающее окно исчезает, когда курсор уходит с кнопки Войти
def test_popup_window_message_button_disappeared(driver):
    main_page = MainPage(driver)
    main_page.show_popup_window(MainPage.ENTRANCE)
    popup_window = main_page.is_visible(MainPage.POPUP_WINDOW_ENTRANCE)
    assert popup_window == True
    main_page.put_away_from_element(MainPage.FAVORITES)
    popup_window_disappeared = main_page.isnt_visible(MainPage.POPUP_WINDOW_ENTRANCE)
    assert popup_window_disappeared is True

# Кнопка Заказы видна на странице
def test_button_Orders_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.ORDERS)
    assert button == True


# Кнопка Заказы имеет верное название
def test_button_Orders_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.ORDERS)
    assert button_name == TestData.NAME_OF_BUTTON_ORDERS


# Кнопка Избранное кликабельна, попадаем в соответствующий раздел
def test_Orders_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.FAVORITES)
    Favorites_page_header = main_page.get_text_of_element(MainPage.HEAD_OF_PAGE_FAVORITES)
    assert Favorites_page_header == TestData.HEADER_OF_PAGE_FAVORITES

# Кнопка Корзина видна на странице
def test_button_basket_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.BASKET)
    assert button == True


# Кнопка Корзина имеет верное название
def test_button_basket_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.BASKET)
    assert button_name == TestData.NAME_OF_BUTTON_BASKET


# Кнопка Корзина кликабельна и попадаем в соответствующий раздел
def test_basket_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.BASKET)
    window_title = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_BASKET)
    assert window_title == True

# Кнопка раздела Ozon fresh видна на странице
def test_button_Ozon_fresh_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.OZON_FRESH)
    assert button == True


# Кнопка Ozon fresh имеет верное название
def test_button_Ozon_fresh_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.OZON_FRESH)
    assert button_name == TestData.NAME_OF_BUTTON_TOP_FRESH


# Кнопка Ozon fresh кликабельна и попадаем в соответствующий раздел
def test_Ozon_fresh_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.OZON_FRESH)
    page_header = main_page.get_text_of_element(MainPage.HEAD_OF_PAGE_FRESH)
    assert page_header == TestData.FRESH

# Кнопка раздела Premium видна на странице
def test_button_Premium_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.PREMIUM)
    assert button == True


# Кнопка Premium имеет верное название
def test_button_Premium_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.PREMIUM)
    assert button_name == TestData.NAME_OF_BUTTON_PREMIUM

# Кнопка раздела Билеты и Отели видна на странице
def test_button_ozon_travel_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.OZON_TRAVEL)
    assert button == True


# Кнопка Билеты и Отели имеет верное название
def test_button_ozon_travel_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.OZON_TRAVEL)
    assert button_name == TestData.NAME_OF_BUTTON_OZON_TRAVEL


# Кнопка Билеты и Отели кликабельна, попадаем в соответствующий раздел
def test_Ozon_travel_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.OZON_TRAVEL)
    window_title = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_OZON_TRAVEL)
    assert window_title == True


# Кнопка раздела Ozon Карта видна на странице
def test_button_Ozon_card_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.OZON_CARD)
    assert button == True

# Кнопка Ozon Карта имеет верное название
def test_button_ozon_card_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.OZON_CARD)
    assert button_name == TestData.NAME_OF_BUTTON_OZON_CARD

# Кнопка Ozon Карта кликабельна, попадаем в соответствующий раздел
def test_Ozon_card_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.OZON_CARD)
    window_title = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_OZON_CARD)
    assert window_title == True

# Кнопка раздела Рассрочка видна на странице
def test_button_instalment_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.INSTALMENT)
    assert button == True


# Кнопка Рассрочка имеет верное название
def test_button_instalment_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.INSTALMENT)
    assert button_name == TestData.NAME_OF_BUTTON_INSTALMENT


# Кнопка Рассрочка кликабельна, попадаем в соответствующий раздел
def test_instalment_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.INSTALMENT)
    window_title = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_INSTALMENT)
    assert window_title == True
    
# Кнопка раздела Акции счет видна на странице
def test_button_actions_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.ACTIONS)
    assert button == True


# Кнопка Акции имеет верное название
def test_button_action_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.ACTIONS)
    assert button_name == TestData.NAME_OF_BUTTON_ACTIONS


# Кнопка Акции кликабельна, попадаем в соответствующий раздел
def test_actions_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.ACTIONS)
    title_of_page = main_page.get_text_of_element(MainPage.HEAD_OF_PAGE_ACTIONS)
    assert title_of_page == TestData.HEADER_OF_PAGE_OF_ACTIONS

# Кнопка раздела Бренды видна на странице
def test_button_brands_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.BRENDS)
    assert button == True


# Кнопка Бренды имеет верное название
def test_button_brands_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.BRENDS)
    assert button_name == TestData.NAME_OF_BUTTON_BRANDS


# Кнопка Бренды кликабельна, попадаем в соответствующий раздел
def test_brends_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.BRENDS)
    title_of_page = main_page.get_text_of_element(MainPage.HEAD_OF_PAGE_BRENDS)
    assert title_of_page == TestData.HEADER_OF_PAGE_OF_BRENDS

# Кнопка раздела Express видна на странице
def test_button_shops_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.SHOPS)
    assert button == True


# Кнопка раздела Express имеет верное название
def test_button_shops_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.SHOPS)
    assert button_name == TestData.NAME_OF_BUTTON_SHOPS


# Кнопка Магазины кликабельна, попадаем в соответствующий раздел
def test_shops_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.SHOPS)
    title_of_page = main_page.get_text_of_element(MainPage.HEAD_OF_PAGE_SHOPS)
    assert title_of_page == TestData.HEADER_OF_PAGE_OF_SHOPS

#  #Кнопка раздела Электроника видна на странице
def test_button_electronica_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.ELECTRONICA_MAIN)
    assert button == True


# Кнопка раздела Электроника имеет верное название
def test_button_electronics_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.ELECTRONICA_MAIN)
    assert button_name == TestData.NAME_OF_BUTTON_ELECTRONICA_MAIN


# Кнопка Электроника кликабельна, попадаем в соответствующий раздел
def test_electronica_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.ELECTRONICA_MAIN)
    window_title = main_page.get_text_of_element(MainPage.ELECTRONICA_MAIN)
    assert window_title == TestData.HEADER_OF_PAGE_OF_ELECTRONICA_MAIN

# Кнопка раздела Одежда и обувь видна на странице
def test_button_clothes_and_shoes_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.CLOTHES_AND_SHOES)
    assert button == True


# Кнопка раздела Одежда и обувь имеет верное название
def test_button_clothes_and_shoes_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.CLOTHES_AND_SHOES)
    assert button_name == TestData.NAME_OF_BUTTON_CLOTHES_AND_SHOES


# Кнопка Одежда и обувь кликабельна, попадаем в соответствующий раздел
# Присутствует раздел "Женщинам"
def test_clothes_and_shoes_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.CLOTHES_AND_SHOES)
    window_title = main_page.get_text_of_element(MainPage.CHAPTER_OF_CLOTHES_AND_SHOES)
    assert window_title == TestData.HEADER_OF_CHAPTER_OF_CLOTHES_AND_SHOES

# Кнопка раздела Детские товары видна на странице
def test_button_kids_goods_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.KIDS_GOODS)
    assert button == True


# Кнопка раздела Детские товары имеет верное название
def test_button_kids_goods_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.KIDS_GOODS)
    assert button_name == TestData.NAME_OF_BUTTON_KIDS_GOODS


# Кнопка Детские товары кликабельна, попадаем в соответствующий раздел
def test_kids_goods_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.KIDS_GOODS)
    window_title = main_page.get_text_of_element(MainPage.KIDS_GOODS)
    assert window_title == TestData.HEADER_OF_PAGE_OF_KIDS_GOODS

# Кнопка раздела Дом и сад видна на странице
def test_button_house_and_garden_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.HOUSE_AND_GARDEN)
    assert button == True


# Кнопка раздела Дом и сад имеет верное название
def test_button_house_and_garden_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.HOUSE_AND_GARDEN)
    assert button_name == TestData.NAME_OF_BUTTON_HOUSE_AND_GARDEN


# Кнопка Дом и сад кликабельна, попадаем в соответствующий раздел
def test_button_house_and_garden_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.HOUSE_AND_GARDEN)
    window_title = main_page.get_text_of_element(MainPage.HOUSE_AND_GARDEN)
    assert window_title == TestData.HEADER_OF_PAGE_OF_HOUSE_AND_GARDEN

# Кнопка раздела Реферальная программа видна на странице
def test_button_top_fashion_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.REFERRAL_PROGRAM)
    assert button == True


# Кнопка Реферальная программа имеет верное название
def test_button_top_fashion_has_true_name(driver):
    main_page = MainPage(driver)
    button_name = main_page.get_text_of_element(MainPage.REFERRAL_PROGRAM)
    assert button_name == TestData.NAME_OF_BUTTON_REFERRAL_PROGRAM


# Кнопка города видна на странице
def test_definite_city_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.BUTTON_SELECT_CITY)
    assert button == True


# При нажатии кнопки города появляется кнопка измененить город
def test_definite_city_appear_window(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.BUTTON_SELECT_CITY)
    window_title = main_page.get_text_of_element(MainPage.FIELD_CITY)
    assert window_title == TestData.FIELD_CITY


# Кнопка изменить раздела выбор города имеет верное название
def test_button_house_and_garden_has_true_name(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.BUTTON_SELECT_CITY)
    button_name = main_page.get_text_of_element(MainPage.FIELD_CITY)
    assert button_name == TestData.HEADER_OF_WINDOW_FIELD_CITY


# При нажатии кнопки изменить появляется окно выбора города
def test_definite_city_appear_window(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.BUTTON_SELECT_CITY)
    window_title = main_page.get_text_of_element(MainPage.LIST_OF_SUITABLE_CITIES)
    assert window_title == TestData.LIST_OF_SUITABLE_CITIES
