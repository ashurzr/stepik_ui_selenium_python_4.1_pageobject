# Реализация методов для ProductPage

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators



class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_to_cart_button()
        button = self.browser.find_element(*ProductPageLocators.BUTTON)
        button.click()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON), "отсутствует кнопка Добавить в корзину"


# методы-проверки:
    def should_be_message_item_is_added_to_cart(self):
        item_added_message = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_MESSAGE) # получаем 
        assert "был добавлен в вашу корзину" in item_added_message.text.lower() # есть сообщ о том что товар добавлен в корзину; lower() преобразует заглавные буквы в строчные



    def get_item_name(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text


    # название товара в сообщ совпадает с названием товара который добавили
    def should_be_item_name_in_message_equals_item_name(self, expected_name):
        item_name_in_message = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_MESSAGE).text
        assert expected_name == item_name_in_message, \
            f"Item name '{expected_name}' is no equal item name in message '{item_name_in_message}'"



    def get_item_price(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text

    def go_to_basket(self):
        self.should_be_add_to_cart_button()
        button = self.browser.find_element(*ProductPageLocators.BASKET_VIEW_BUTTON)
        button.click()

    # цена товара в корзине совпадает с ценой товара который добавили
    def should_be_item_price_added_to_cart_equals_item_price(self, expected_price):
        #item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        #item_price = self.get_item_price()

        item_price_in_basket = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_IN_BASKET).text

        print(f"item_price: '{expected_price}'")
        print(f"item_price_in_basket: '{item_price_in_basket}'")

        assert expected_price == item_price_in_basket, \
            f"Item price '{expected_price}' is not equal item price in basket '{item_price_in_basket}'"



    def should_be_message_cart_total_price(self):
        cart_price_message = self.browser.find_element(*ProductPageLocators.CART_PRICE_MESSAGE) # получаем
        assert cart_price_message.is_displayed() # есть сообщ со стоимостью корзины


    def should_be_cart_total_price_equals_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text # получаем item_price

        # получили все что в диве 'Всего в корзине: 9,99 £ в том числе надпись кнопки Посмотреть корзину'
        item_price_in_cart_message_text = self.browser.find_element(*ProductPageLocators.ITEM_PRICE_IN_CART_MESSAGE).text # .text возвращает весь видимый текст, который содержится внутри этого элемента и его вложенных тегов.
        # разделили "построчно" используя splitlines:
        lines = item_price_in_cart_message_text.splitlines()
        # получаем нужный момент текста из нужной "строки":
        item_price_in_cart_message = lines[0].split(':')[-1].strip() # строку тоже делим по : после "Всего в корзине:", берем нужный элемент, убираем пробелы

        print(f"item_price: '{item_price}'")
        print(f"item_price_in_cart_message: '{item_price_in_cart_message}'")
        
        assert item_price == item_price_in_cart_message # стоимость корзины совпадает со стоимостью товара




# Отрицательные проверки: как проверить отсутствие элемента - проверяем success message 
    
    # элемент не появляется на странице в течение заданного времени is_not_element_present
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    # элемент исчезает is_disappeared
    def should_success_message_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappear, but should have"


    # позитивная проверка is_element_present
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented, but should be"

        # для print
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text  # .text возвращает весь видимый текст, который содержится внутри этого элемента и его вложенных тегов.
        print(f"success_message: '{success_message}'") # 'The shellcoder's handbook был добавлен в вашу корзину.'

        