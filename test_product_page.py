from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.product_page import ProductPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import ProductPageLocators

import pytest



# Плюсы наследования: пример
from pages.login_page import LoginPage


# Задание: наследование и отрицательные проверки
from pages.basket_page import BasketPage
from pages.locators import BasketPageLocators



from pages.locators import BasePageLocators








def wait_for_element(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(locator)
    )



# Отрицательные проверки: как проверить отсутствие элемента - проверяем success message 

# он же test_guest_cant_see_success_message №2
# Негативный тест: сообщение НЕ должно появляться само по себе
def test_success_message_is_not_present(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


# он же test_message_disappeared_after_adding_product_to_basket №3
# Негативный тест: сообщение должно исчезнуть - а вот этот кейс не подходит - у нас же не исчезает сообщение а остается !!!!!!!!
@pytest.mark.xfail
def test_success_message_disappears_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()

    # д вия должны быть чтоб сообщ сперва появилось
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    # и тут сообщ уже должно исчезнуть
    page.should_success_message_disappear()



# Позитивный тест: сообщение появляется после добавления товара
def test_success_message_appears_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()

    # д вия должны быть чтоб сообщ появилось
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_success_message()


    
# Плюсы наследования: пример
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()


    page.should_be_login_link()

    page.go_to_login_page()
    # def go_to_login_page(self):
        # login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        # login_link.click()

    # какбы сгенерели чтоли логин страницу
    login_page = LoginPage(browser, browser.current_url)
    # Здесь переключаемся с ProductPage на LoginPage, так как теперь мы на другой странице, и логика проверки (методы, локаторы) будет другой.
    # Это как: «мы на новой странице, значит нам нужен объект этой новой страницы — LoginPage».

    # и проверяем что это/там  логин страница
    login_page.should_be_login_page()
    # а это вот это в login_page.py
    # def should_be_login_page(self):
        # self.should_be_login_url()
        # self.should_be_login_form()
        # self.should_be_register_form()




# Задание: наследование и отрицательные проверки
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):

# Гость открывает страницу товара
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/hacking-exposed-wireless_208/"
    page = ProductPage(browser, link)
    page.open()


# Переходит в корзину по кнопке в шапке
    page.view_basket()  # используем метод перехода в корзину
    basket_page = BasketPage(browser, browser.current_url)



# Ожидаем, что в корзине нет товаров
    basket_page.should_be_empty()  # should_be_empty()

# Ожидаем, что есть текст о том что корзина пуста
    basket_page.should_be_text_cart_is_empty() # should_be_text_cart_is_empty()







# Задание: группировка тестов и setup
class TestUserAddToBasketFromProductPage():

    # сначала фикстура
    # добавляем фикстуру которая будет выполняться перед каждым тестом
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # открыть страницу регистрации
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link) # вообще это мы page object логина генерим какбы или методы страницы логина
        page.open()
        

        # зарегистрировать нового пользователя
        page.register_new_user()


        # проверить, что пользователь залогинен
        page.should_be_authorized_user()


    # потом тесты
    # Реализация тестов для ProductPage
    def test_user_can_add_product_to_basket(self, browser):
        # def test_guest_can_add_product_to_basket(browser, link):
        #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
        # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        # link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()  # 1й шаг

        WebDriverWait(browser, 10).until(EC.presence_of_element_located(ProductPageLocators.BUTTON))
        page.add_product_to_basket()  # 2й шаг

        # по ссылке в этом тесте нет алерта поэтому закоментим
        # page.solve_quiz_and_get_code()  # 3й шаг теста
        #time.sleep(60)

        wait_for_element(browser, ProductPageLocators.ITEM_ADDED_MESSAGE)
        page.should_be_message_item_is_added_to_cart()  # есть сообщ о том что товар добавлен в корзину

        #time.sleep(30)

        item_name = page.get_item_name()
        wait_for_element(browser, ProductPageLocators.ITEM_NAME_IN_MESSAGE)
        page.should_be_item_name_in_message_equals_item_name(item_name)  # название товара в сообщ совпадает с названием товара который добавили

        wait_for_element(browser, ProductPageLocators.CART_PRICE_MESSAGE)
        page.should_be_message_cart_total_price()  # есть сообщ со стоимостью корзины

        wait_for_element(browser, ProductPageLocators.ITEM_PRICE_IN_CART_MESSAGE)
        page.should_be_cart_total_price_equals_item_price()  # стоимость корзины совпадает со стоимостью товара

        item_price = page.get_item_price()  # сохраняем цену товара, она станет expected_price
        page.go_to_basket()  # жмем на кнопку Посмотреть корзину
        # time.sleep(120)
        # wait_for_element(browser, ProductPageLocators.ITEM_PRICE_IN_BASKET)
        page.should_be_item_price_added_to_cart_equals_item_price(item_price)  # передаем item_price котор станет expected_price





    # test_guest_cant_see_success_message_after_adding_product_to_basket №1
    # дописываю тест которого у меня нет - проверка что нет сообщения после добавления товара - тест упадет т к есть
    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()

        # д вия должны быть чтоб сообщ появилось
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()

        page.should_not_be_success_message()

