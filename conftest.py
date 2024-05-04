import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="--language: es/rus...")


@pytest.fixture(scope="function")
def browser(request):
    site_language = request.config.getoption("language")
    browser = webdriver.Chrome()
    link = f"https://selenium1py.pythonanywhere.com/{site_language}/catalogue/coders-at-work_207/"
    browser.get(link)
    # raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
