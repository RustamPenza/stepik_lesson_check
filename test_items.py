from selenium.webdriver.common.by import By


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_button_addToBasket(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    button_text = button.text
    button_es = "Añadir al carrito"
    assert button_text == button_es, (f"Ожидалось 'Añadir al carrito',"
                                      f" а отображается '{button_text}'")
