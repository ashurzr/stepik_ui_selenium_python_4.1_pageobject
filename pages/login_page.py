from .base_page import BasePage
from .locators import LoginPageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' is not presented"
        #assert "loginn" in self.browser.current_url, "'loginn' is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"


    # метод регистрирует нового пользователя
    def register_new_user(self):
        # генерация емейла и пароля
        email_generator = str(time.time()) + "@fakemail.org"
        password_generator = "fakepassword"
        # нашли элемент
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        # и в элемент отправили
        email_input.send_keys(email_generator)
        # нашли элемент
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        # и в элемент отправили
        password_input.send_keys(password_generator)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD)
        confirm_password_input.send_keys(password_generator)
        # ищем и жмем кнопку Зарегистрироваться
        register_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        register_button.click()
        