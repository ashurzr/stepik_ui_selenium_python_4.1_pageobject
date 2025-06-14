import math
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from .locators import ProductPageLocators
import string
import random


# реализация общих методов для любой страницы
class BasePage():
    # Проверка элемента на странице
    def __init__(self, browser, url, timeout=10): # добавили timeout=10
        self.browser = browser
        self.url = url
        # Проверка элемента на странице
        # добавили
        self.browser.implicitly_wait(timeout)


    # Проверка элемента на странице
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True


    def open(self):
        self.browser.get(self.url)


# для Product Page
# посчитать результат выражения методом solve_quiz_and_get_code()
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        # try:
        #     alert = self.browser.switch_to.alert
        #     alert_text = alert.text
        #     print(f"Your code: {alert_text}")
        #     alert.accept()
        # except NoAlertPresentException:
        #     print("No second alert presented")
        # Второй alert с кодом (если появится)
        
        try:
            # Ждём появления второго alert в течение 5 секунд
            WebDriverWait(self.browser, 5).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except (NoAlertPresentException, TimeoutException):
            print("No second alert presented")


# Отрицательные проверки: как проверить отсутствие элемента - проверяем success message
    # элемент не появляется на странице в течение заданного времени is_not_element_present
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # элемент исчезает is_disappeared
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


# Плюсы наследования: пример
# из файла main_page.py эти методы забраны:
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        #login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        login_link.click()


    # Проверка элемента на странице - изменили метод проверки ссылки на логин, чтобы он выдавал адекватное сообщение об ошибке:
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        #assert self.is_element_present(*BasePageLocators.LOGIN_LINK_INVALID), "Login link is not presented"
        

# Задание: наследование и отрицательные проверки
    # реализация метода перехода в корзину
    def view_basket(self): # переход по кнопке Посмотреть корзину
        self.should_be_view_cart_button()  # проверка наличия кнопки Посмотреть корзину, используем метод should_be_view_cart_button() см ниже
        button = self.browser.find_element(*BasePageLocators.BASKET_VIEW_BUTTON) # в BasePageLocators т к кнопка Посмотреть корзину она отовсюду доступна
        button.click()


    def should_be_view_cart_button(self):
        assert self.is_element_present(*BasePageLocators.BASKET_VIEW_BUTTON), "Basket view button is not visible"


    # Задание: группировка тестов и setup
    # проверка что пользователь залогинен
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
