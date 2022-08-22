import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome('D:\PyCharm\chromedriver.exe') #Укажите путь к своему вебдрайверу.
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
