from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# теперь перепишем тест с помощью Page Object
from pages.main_page import MainPage

from pages.login_page import LoginPage
# способ 2 - переход неявный, страницу инициализируем в теле теста
#from .login_page import LoginPage # делаем импорт страницы с логином


# Задание: наследование и отрицательные проверки
from pages.basket_page import BasketPage

import pytest








@pytest.mark.login_guest
class TestLoginFromMainPage():
    # способ 2 - переход неявный, LoginPage инициализируем в теле теста
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    # Методы-проверки в Page Object - новый тест
    def test_guest_should_see_login_link(self, browser):
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





# Задание: наследование и отрицательные проверки
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):

# Гость открывает главную страницу
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)
    page.open()


# Переходит в корзину по кнопке в шапке сайта
    page.view_basket() # используем метод перехода в корзину
    basket_page = BasketPage(browser, browser.current_url)



# Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty() # should_be_empty()

# Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_text_cart_is_empty() # should_be_text_cart_is_empty()

