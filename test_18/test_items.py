import time
import pytest

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"])
def test_add_to_cart_button(browser, link):
    browser.get(link)
    time.sleep(5)  # Ждем, чтобы страница полностью загрузилась
    assert browser.find_element("css selector", ".btn-add-to-basket"), "Кнопка добавления в корзину не найдена"
