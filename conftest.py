import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: for example --language=es")
    parser.addoption('--browser_name', action='store', default='chrome')


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        print(f"\nstart chrome browser for test with language: {language}..")
        options = ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)

    else:
        raise pytest.UsageError("--browser_name should be 'chrome'")

    yield browser
    print("\nquit browser..")
    browser.quit()
