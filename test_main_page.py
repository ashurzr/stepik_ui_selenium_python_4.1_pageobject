from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# теперь перепишем тест с помощью Page Object
from pages.main_page import MainPage


# link = "http://selenium1py.pythonanywhere.com/"

# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#
#
# def test_guest_should_see_button_addtocart(browser):
#     browser.get(link)
#     time.sleep(30)
#     button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
#     assert button, "Кнопка добавления в корзину не найдена!"

# def test_guest_can_go_to_login_page(browser):
#     browser.get(link)
#     login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()


# # дробим действия:
#
# # вынесли сюда  нахождение элемента и клик по нему
# def go_to_login_page(browser):
#     login_page_link = browser.find_element(By.CSS_SELECTOR, "#login_page_link_selector")
#     login_page_link.click()
#
# # а тут только запускаем браузер и т д - см фикстуру browser в conftest.py
# def test_guest_can_go_to_login_page(browser):
#     browser.get(link)
#     # вызываем предыдущий метод в котором  находим элемент и кликаем по нему
#     go_to_login_page(browser)


# теперь перепишем тест с помощью Page Object
def test_guest_can_go_to_login_page(browser):
    
    link = "http://selenium1py.pythonanywhere.com/"

    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера aka browser и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
