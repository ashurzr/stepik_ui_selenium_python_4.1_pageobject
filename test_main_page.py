from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# теперь перепишем тест с помощью Page Object
from pages.main_page import MainPage

from pages.login_page import LoginPage
# способ 2 - переход неявный, страницу инициализируем в теле теста
#from .login_page import LoginPage # делаем импорт страницы с логином


# link = "http://selenium1py.pythonanywhere.com/"

# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#
#
# def test_guest_should_see_button_addtocart(browser):
#     browser.get(link)
#     time.sleep(30)
#     button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
#     assert button, "Кнопка добавления в корзину не найдена!"

# def test_guest_can_go_to_login_page(browser):
#     browser.get(link)
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()


# # дробим действия:
#
# # вынесли сюда  нахождение элемента и клик по нему
# def go_to_login_page(browser):
#     login_page_link = browser.find_element(By.CSS_SELECTOR, "#login_page_link_selector")
#     login_page_link.click()
#
# # а тут только запускаем браузер и т д - см фикстуру browser в conftest.py
# def test_guest_can_go_to_login_page(browser):
#     browser.get(link)
#     # вызываем предыдущий метод в котором  находим элемент и кликаем по нему
#     go_to_login_page(browser)


# # теперь перепишем тест с помощью Page Object
# def test_guest_can_go_to_login_page(browser):
#
#     link = "http://selenium1py.pythonanywhere.com/"
#     #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer" # ссылка шапки промоакции
#
#     page = MainPage(browser, link)   # инициализируем Page Object,  передаем браузер и ссылку  в конструктор BasePage
#     page.open()                      # открываем страницу
#     page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

# # реализуем переход способ 1 - возвращаем нужный page object
# # теперь в тесте не нужно думать про инициализацию страницы т к она уже создана
# def test_guest_can_go_to_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     login_page = page.go_to_login_page()
#     login_page.should_be_login_page()

# способ 2 - переход неявный, LoginPage инициализируем в теле теста
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


# Методы-проверки в Page Object - новый тест
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer" # ссылка шапки промоакции
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link() # вот этот метод



# Реализация тестов для LoginPage
# из login_page.py  тестим  def should_be_login_page(self):
#         self.should_be_login_url()
#         self.should_be_login_form()
#         self.should_be_register_form()

def test_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url() # вот этот метод тестируем

def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form() # вот этот метод тестируем

def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form() # вот этот метод тестируем


# # ну или с переходом с основной страницы на страницу логина
# def test_should_be_login_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#
#     page.go_to_login_page() # переход с мейна на логин - метод находит элемент и кликает по нему
#
#     login_page = LoginPage(browser, browser.current_url) # без - ошибка 'login_page' is not defined
#     login_page.should_be_login_url()
#     login_page.should_be_login_form()
#     login_page.should_be_register_form()
