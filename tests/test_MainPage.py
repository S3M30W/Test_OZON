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
# def test_logo_ozon_clickable(driver):
# main_page = MainPage(driver)
# main_page.find_click(MainPage.MAIN_LOGO)
# title_of_window = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_MAIN_LOGO)
# assert title_of_window == True


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
    
#Кнопка Избранное видна на странице
def test_button_favorites_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.FAVORITES)
    assert button == True    


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


# При наведении на кнопку Войти появляется всплывающее окно
# def test_popup_window_appear(driver):
# main_page = MainPage(driver)
# main_page.show_popup_window(MainPage.ENTRANCE)
# popup_window = main_page.is_visible(MainPage.POPUP_WINDOW_ENTRANCE)
# assert popup_window == True

# Всплывающее окно исчезает, когда курсор уводим с кнопки Войти
#def test_popup_window_message_button_disappeared(driver):
    #main_page = MainPage(driver)
    #main_page.show_popup_window(MainPage.ENTRANCE)
    #popup_window = main_page.is_visible(MainPage.POPUP_WINDOW_ENTRANCE)
    #assert popup_window == True
    #main_page.put_away_from_element(MainPage.FAVORITES)
    #popup_window_disappeared = main_page.isnt_visible(MainPage.POPUP_WINDOW_ENTRANCE)
    #assert popup_window_disappeared is True
    
#Кнопка Заказы видна на странице
def test_button_Orders_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.ORDERS)
    assert button == True
    
#Кнопка Избранное кликабельна, попадаем в соответствующий раздел
#def test_favorites_clickable(driver):
    #main_page = MainPage(driver)
    #main_page.find_click(MainPage.FAVORITES)
    #Favorites_page_header = main_page.get_text_of_element(MainPage.HEAD_OF_PAGE_FAVORITES)
    #assert Favorites_page_header == TestData.HEADER_OF_PAGE_FAVORITES
    
#Кнопка Корзина видна на странице
def test_button_cart_on_page(driver):
    main_page = MainPage(driver)
    button = main_page.is_visible(MainPage.CART)
    assert button == True
#Кнопка Корзина кликабельна и попадаем в соответствующий раздел
def test_cart_clickable(driver):
    main_page = MainPage(driver)
    main_page.find_click(MainPage.CART)
    window_title = main_page.get_windows_title(TestData.HEADER_OF_WINDOW_CART)
    assert window_title == True
