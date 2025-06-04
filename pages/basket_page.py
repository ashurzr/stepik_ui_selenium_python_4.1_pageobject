# Реализация методов для BasketPage

# Задание: наследование и отрицательные проверки
from .base_page import BasePage
from pages.locators import BasketPageLocators




class BasketPage(BasePage):

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

        # негативная проверка
        #assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is empty"

    # если валится на каком то шаге то дальше не идут тесты
    # потому сообщения об ошибках будут(в случае негативных проверок) у обоих тестов либо Basket is empty либо There's a message that basket is empty

    def should_be_text_cart_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "No message that basket is empty"

        # негативная проверка
        #assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "There's a message that basket is empty"



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




# from .base_page import BasePage
#
# from .locators import LoginPageLocators
#
#
# class LoginPage(BasePage):
#     def should_be_login_page(self):
#         self.should_be_login_url()
#         self.should_be_login_form()
#         self.should_be_register_form()
#
#     def should_be_login_url(self):
#         # реализуйте проверку на корректный url адрес
#         assert "login" in self.browser.current_url, "'login' is not presented"
#         #assert "loginn" in self.browser.current_url, "'loginn' is not presented"
#
#     def should_be_login_form(self):
#         # реализуйте проверку, что есть форма логина
#         assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"  # из файла locators.py
#
#     def should_be_register_form(self):
#         # реализуйте проверку, что есть форма регистрации на странице
#         assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented" # из файла locators.py
