
import math

#from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from selenium.common.exceptions import NoAlertPresentException, TimeoutException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Проверка элемента на странице - добавили:
from selenium.common.exceptions import NoSuchElementException

# это как бы реализация общих методов для любой страницы
class BasePage():
    
    def __init__(self, browser, url, timeout=10):     # Проверка элемента на странице - добавили timeout=10
        self.browser = browser
        self.url = url
        # Проверка элемента на странице - добавили:
        self.browser.implicitly_wait(timeout)


    # Проверка элемента на странице - добавили:
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def open(self):
        self.browser.get(self.url)

# в других файлах например в main_page.py, login_page.py, basket_page.py... реализация методов для конкретных страниц
# в файлах начинающихся на test_... - тесты к ним


# для Product Page
# посчитать результат выражения методом solve_quiz_and_get_code() - метод добавить в класс BasePage, метод дан в задании:
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

    