from selenium.webdriver.common.by import By


def test_guest_should_see_button_addToBasket(browser):
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    button_text = button.text
    button_es = "Añadir al carrito"
    assert button_text == button_es, (f"Ожидалось 'Añadir al carrito',"
                                      f" а отображается '{button_text}'")
