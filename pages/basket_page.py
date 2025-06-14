from .base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

        # негативная проверка
        #assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is empty"

    # если валится на каком то шаге, то дальше не идут тесты
    # потому сообщения об ошибках будут(в случае негативных проверок) у обоих тестов либо Basket is empty либо There's a message that basket is empty

    def should_be_text_cart_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "No message that basket is empty"

        # негативная проверка
        #assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "There's a message that basket is empty"


    # либо вот так:
    # def should_be_empty(self):
    #     assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"
    #
    # def should_not_be_empty(self):
    #     # негативная проверка
    #     assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is empty"
    #
    #
    #
    # def should_be_text_cart_is_empty(self):
    #     assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "No message that basket is empty"
    #
    # def should_not_be_text_cart_is_empty(self):
    #     # негативная проверка
    #     assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "There's a message that basket is empty"


    # цена товара в корзине совпадает с ценой товара который добавили
    # expected_price - см тест test_guest_can_add_product_to_basket
    def should_be_item_price_added_to_cart_equals_item_price(self, expected_price): # expected_price это просто название принимаемого аргумента, а подается сюда фактически значение переменной item_price (в тесте этот метод вызывается со значением item_price)
        item_price_in_basket = self.browser.find_element(*BasketPageLocators.ITEM_PRICE_IN_BASKET).text
        print(f"item_price: '{expected_price}'")
        print(f"item_price_in_basket: '{item_price_in_basket}'")
        assert expected_price == item_price_in_basket, \
            f"Item price '{expected_price}' is not equal item price in basket '{item_price_in_basket}'"
