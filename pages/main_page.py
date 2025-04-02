from .base_page import BasePage # from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    # вынесли сюда  нахождение элемента и клик по нему
    # def go_to_login_page(browser):
    #     login_page_link = browser.find_element(By.CSS_SELECTOR, "#login_page_link_selector")
    #     login_page_link.click()

    # видоизменили метод выше чтоб все работало
    # браузер больше не передаем в аргумент т к передаем и сохраняем на этапе создания page object, поэтому теперь указываем self
    def go_to_login_page(self):
        # тк браузер у нас хранится как аргумент класса BasePage, обращаться теперь к нему нужно с помощью self
        login_page_link = self.browser.find_element(By.ID, "login_link")
        login_page_link.click()



    # # Методы-проверки в Page Object
    # def should_be_login_link(self):
    #     self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

    # Проверка элемента на странице - изменили метод проверки ссылки на логин, чтобы он выдавал адекватное сообщение об ошибке:
    def should_be_login_link(self):
        #assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
        assert self.is_element_present(By.ID, "login_link"), "Login link is presented"