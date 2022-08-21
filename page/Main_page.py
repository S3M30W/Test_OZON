from selenium.webdriver.common.by import By
from pages.Base_page import BasePage
from config import TestData


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    MAIN_LOGO = (By.CSS_SELECTOR, "#stickyHeader div")
    HEADER_OF_WINDOW_MAIN_LOGO = (By.XPATH, "//div[@class='text']")
    CATALOG = (By.CSS_SELECTOR, "div[data-widget ='catalogMenu'] div button")
    ELECTRONICA_SUB = (By.XPATH, "//a[@class = 'a3p5 g5s4 g5s6 g5t' and @href='/category/elektronika-15500/']")
    HEAD_OF_PAGE_ELECTRONICA_SUB = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'Электроника')]")
    SEARCH_WHERE = (By.CSS_SELECTOR, "div[data-widget = 'searchBarDesktop'] form div span")
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder = 'Искать на Ozon']")
    SUBMIT_SEARCH = (By.XPATH, "//button[@class='ia0a']")
    ENTRANCE = (By.CSS_SELECTOR, "div[data-widget = 'profileMenuAnonymous']")
    POPUP_WINDOW_ENTRANCE = (By.XPATH, "//div[@style='position: absolute; top: -9999px; left: -9999px;']")
    FAVOURITES = (By.XPATH, "//a[@href = '/my/favorites']")
    HEAD_OF_PAGE_FAVOURITES = (By.XPATH, "//div[@class = 'a3p5' and contains (text(), 'Избранное')]")
    BASKET = (By.XPATH, "//a[@href = '/cart']")
    HEADER_OF_WINDOW_BASKET = (By.XPATH, "//h1[@class='ra4']")
    ORDERS = (By.CSS_SELECTOR, "div[data-widget = 'orderInfo']")
    OZON_FRESH = (By.XPATH, "//a[@target='_self' and contains (text(), 'Ozon fresh')]")
    HEAD_OF_PAGE_FRESH = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'TOP Fashion')]")
    PREMIUM = (By.XPATH, "//a[@href = '/highlight/premium/' and @class='a4 r5c']")
    OZON_TRAVEL = (
        By.XPATH, "//a[@href='https://www.ozon.ru/travel/?perehod=ozon_menu_header' and @class = 'a4 r5c']")
    OZON_CARD = (By.XPATH,
                 "//a[@href='https://www.ozon.ru/highlight/keshbek-do-30-dlya-ozon-schet-i-premium-323369' and @class='a4 r5c']")
    INSTALMENT = (By.XPATH, "//a[@href='/section/limit/' and @class = 'a4 r5c']")
    STOCKS = (By.XPATH, "//a[@href='/highlight/globalpromo/' and @class = 'a4 r5c']")
    HEAD_OF_PAGE_ACTIONS = (By.XPATH, "//div[@class = 'a3p5' and contains (text(), 'Акции и спецпредложения')]")
    BRENDS = (By.XPATH, "//a[@href = '/brand/' and @class = 'a4 r5c']")
    HEAD_OF_PAGE_BRENDS = (By.XPATH, "//h1[@class = 'a9u6 f-h1' and contains (text(), 'Все бренды')]")
    EXPRESS = (By.XPATH, "//a[@href='/highlight/express/' and @class = 'a4 r5c']")
    HEADER_OF_PAGE_OF_EXPRESS = (
        By.XPATH, "//div[@class='a4 a5 dx tsHead' and contains (text(), 'Популярное на express')]")
    ELECTRONICA_MAIN = (By.XPATH, "//a[@href = '/category/elektronika-15500/' and contains (text(), 'Электроника')]")
    HEAD_OF_PAGE_ELECTRONICA_MAIN = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'Электроника')]")
    CLOTHES_AND_SHOES = (
        By.XPATH, "//a[@href='/category/zhenskaya-odezhda-7501/' and contains (text(), 'Одежда и обувь')]")
    CHAPTER_OF_CLOTHES_AND_SHOES = (By.XPATH, "//div[@class = 'a3p5' and contains (text(), 'Женщинам')]")
    KIDS_GOODS = (By.XPATH, "//a[@href = '/category/detskie-tovary-7000/' and contains (text(), 'Детские товары')]")
    HEAD_OF_PAGE_KIDS_GOODS = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'Детские товары')]")
    HOUSE_AND_GARDEN = (By.XPATH, "//a[@href = '/category/dom-i-sad-14500/' and contains (text(), 'Дом и сад')]")
    HEAD_OF_PAGE_HOUSE_AND_GARDEN = (By.XPATH, "//h1[@class = 'b3a0' and contains (text(), 'Дом и сад')]")
    REFERRAL_PROGRAM = (By.XPATH, "//a[@href='https://www.ozon.ru/b2bref' and @class='a4 r5c']")
    HEADER_OF_PAGE_OF_REFERRAL_PROGRAM = (
        By.XPATH, "//h2[@class='tsHeadXL us2' and contains (text(), 'Регистрируйтесь в реферальной программе')]")
    BUTTON_SELECT_CITY = (By.XPATH, "//span[@class='ui-j3' and contains (text(), 'Санкт-Петербург')]")
    FIELD_CITY = (By.XPATH, "//span[@class='m6d']")
    LIST_OF_SUITABLE_CITIES = (By.XPATH, "//span[@class='rd6 r8d tsHeadL q0']")
