from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from pages.product_page import ProductPage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import ProductPageLocators

import pytest


def wait_for_element(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.presence_of_element_located(locator)
    )


# Реализация тестов для ProductPage
# def test_guest_can_add_product_to_basket(browser):
# параметризовали:
@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer6",
                          pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                          "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    #link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()  # 1й шаг

    WebDriverWait(browser, 10).until(EC.presence_of_element_located(ProductPageLocators.BUTTON))
    page.add_product_to_basket()  # 2й шаг
    page.solve_quiz_and_get_code()  # 3й шаг теста
    #time.sleep(10)


    wait_for_element(browser, ProductPageLocators.ITEM_ADDED_MESSAGE)
    page.should_be_message_item_is_added_to_cart() # есть сообщ о том что товар добавлен в корзину


    item_name = page.get_item_name()
    wait_for_element(browser, ProductPageLocators.ITEM_NAME_IN_MESSAGE)
    page.should_be_item_name_in_message_equals_item_name(item_name) # название товара в сообщ совпадает с названием товара который добавили


    wait_for_element(browser, ProductPageLocators.CART_PRICE_MESSAGE)
    page.should_be_message_cart_total_price() # есть сообщ со стоимостью корзины


    wait_for_element(browser, ProductPageLocators.ITEM_PRICE_IN_CART_MESSAGE)
    page.should_be_cart_total_price_equals_item_price() # стоимость корзины совпадает со стоимостью товара


    item_price = page.get_item_price()  # сохраняем цену товара, она станет expected_price
    page.go_to_basket() # жмем на кнопку Посмотреть корзину
    #time.sleep(120)
    #wait_for_element(browser, ProductPageLocators.ITEM_PRICE_IN_BASKET)
    page.should_be_item_price_added_to_cart_equals_item_price(item_price) # передаем item_price котор станет expected_price



# def test_should_be_message_item_is_added_to_cart(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_message_item_is_added_to_cart()


# def test_should_be_message_cart_total_price(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_message_cart_total_price()
#
#
# def test_should_be_cart_total_price_equals_item_price(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_cart_total_price_equals_item_price()
    