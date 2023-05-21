import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser():
    #Опции
    chrome_options = Options()
    #Не показывать запуск браузера каждый тест
    chrome_options.add_argument("--headless")
    print("\nstart browser for test..")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    print("\nquit browser..")
    browser.quit()