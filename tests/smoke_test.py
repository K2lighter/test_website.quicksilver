from selenium import webdriver

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.start_page import StartPage


class Test1:
    def test_select_product(self):
        global driver
        try:
            option = webdriver.FirefoxOptions()
            option.set_preference('general.useragent.override', 'example :)')
            option.set_preference('dom.webdriver.enable', False)  # обходим систему распознавания selenium
            option.set_preference('dom.webnotifications.enabled', False)  # отключаем все всплывающие окна
            option.set_preference('media.volume_scale', '0.0')  # отключаем звук
            driver = webdriver.Firefox(options=option)
            # driver = undetected_chromedriver.Chrome()
            print("Начинаем тестирование")

            start_page = StartPage(driver)
            start_page.load_website()

            login_page = LoginPage(driver)
            login_page.autorization()

            product_page = ProductPage(driver)
            product_page.select_product()

        except Exception as Ex:
            print(Ex)
        finally:
            driver.close()
            driver.quit()


test = Test1()
