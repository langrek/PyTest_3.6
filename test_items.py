import time
link = "http://selenium1py.pythonanywhere.com/"


def test_add_to_basket_btn(browser):
    browser.get(link)

    #Выбираем книжки
    browser.find_element_by_css_selector('#browse > li > ul > li.dropdown-submenu > a').click()

    #Выбираем первый предложенный товар
    first_book_css = '#default > div.container-fluid.page > div > div > div > section > div > ol > li:nth-child(1) > article > h3 > a'
    browser.find_element_by_css_selector(first_book_css).click()

    time.sleep(30)

    #Если элемент находится, создается список длинной 1. Иначе - пустой список
    button = browser.find_elements_by_css_selector('#add_to_basket_form > button')

    assert len(button) > 0, f'Кнопки "добавить в корзину" нет'