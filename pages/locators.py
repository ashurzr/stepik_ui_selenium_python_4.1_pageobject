from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link") # селектор с ссылки шапки промоакции

# Реализация LoginPage
class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form") # селектор формы регистрации
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") # селектор формы логина