from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link") # селектор с ссылки шапки промоакции

# Реализация локаторов для LoginPage
class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form") # селектор формы регистрации
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") # селектор формы логина


# Реализация локаторов для ProductPage
class ProductPageLocators():
    #BUTTON = (By.XPATH, "//button[contains(., 'Добавить в корзину')]") # xpath кнопки Добавить в корзину
    BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    # вот тут вот сделала чтоб по обоим ссылкам находило кнопку (тоже потому что на англ там - Add to basket)


    ITEM_ADDED_MESSAGE = (By.CSS_SELECTOR, "div.alert-success .alertinner")  # поиск текста "был добавлен в вашу корзину" в диве с классами .alert-success и .alertinner
    # вот тут не находит потому что по второй ссылке сообщения на англ а не на русском - надо универсальный локатор сделать как то


    CART_PRICE_MESSAGE = (By.CSS_SELECTOR, "div.alert-info .alertinner p") # поиск текста "Стоимость корзины теперь составляет" в диве с классами .alert-info и .alertinner и внутри p


    ITEM_PRICE = (By.CSS_SELECTOR, "div.alert-info div.alertinner p strong") # а это точно откуда нужно айтем прайс????

    ITEM_PRICE_IN_CART_MESSAGE = (By.XPATH, "//div[@class='basket-mini pull-right hidden-xs']") # получили <selenium.webdriver.remote.webelement.WebElement (session="8cf53978b2a681aede9bcecfb1f49910", element="f.0D0A1099B07B827BB26ACB36F5576C0C.d.FD3AAC3E1AF87C258F48A0A756E6924B.e.23")>


    #BASKET_VIEW_BUTTON = (By.LINK_TEXT, "Посмотреть корзину") # заменю на более уникальный чтоб на англ тоже работало и уберу в base page locators класс т к эта кнопка на всех страницах

    ITEM_PRICE_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items div.row div.col-sm-1 p")


    # название товара в сообщ совпадает с названием товара который добавили
    ITEM_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ITEM_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alertinner strong")



# Отрицательные проверки: как проверить отсутствие элемента - проверяем success message 
    
    # локатор для success message - первое сообщение что книга добавлена в корзину - the shellcoders's handbook has been added to your basket
    # Coders at Work был добавлен в вашу корзину
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")



# Плюсы наследования: пример
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_VIEW_BUTTON = (By.CSS_SELECTOR, 'a[href$="/basket/"]')



# Задание: наследование и отрицательные проверки
class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")  # элементы с товарами
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")  # текст о пустой корзине

