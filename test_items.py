import time
link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'

def test_localization(browser, request):
    browser.get(link)
    basket = browser.find_element_by_css_selector('.btn-primary.btn-add-to-basket')
    time.sleep(30)
    language = request.config.getoption('language')
    if language == 'fr':
        basket_text = basket.text
        assert basket_text == 'Ajouter au panier', 'Название кнопки добавления в корзину не соответствует ожидаемому результату'

