
# это как бы реализация общих методов для любой страницы
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        
    def open(self):
        self.browser.get(self.url)

# в других файлах например в main_page.py, login_page.py, basket_page.py... реализация методов для конкретных страниц
# в файлах начинающихся на test_... - тесты к ним 