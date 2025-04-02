
# Проверка элемента на странице - добавили:
from selenium.common.exceptions import NoSuchElementException

# это как бы реализация общих методов для любой страницы
class BasePage():
    def __init__(self, browser, url, timeout=10):     # Проверка элемента на странице - добавили timeout=10
        self.browser = browser
        self.url = url
        # Проверка элемента на странице - добавили:
        self.browser.implicitly_wait(timeout)

    # Проверка элемента на странице - добавили:
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True



    def open(self):
        self.browser.get(self.url)

# в других файлах например в main_page.py, login_page.py, basket_page.py... реализация методов для конкретных страниц
# в файлах начинающихся на test_... - тесты к ним 