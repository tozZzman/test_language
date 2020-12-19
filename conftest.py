from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb', help='Choose language: ru, en-gb, de, es')

@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print('\n' + '-'*10 + 'Браузер открыт' + '-'*10)
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\n' + '-'*10 + 'Браузер закрыт' + '-'*10)
    browser.quit()

