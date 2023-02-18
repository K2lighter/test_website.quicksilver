import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from src import Locators_product


class ProductPage(Base, Locators_product):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

        # поиск элемента на странице

    def get_quicksilver_logo(self):
        """Ссылка quicksilver_logo"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.quicksilver_logo)))

    def get_see_button(self):
        """Кнопка 'СМОТРЕТЬ'"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.see_button)))

    def get_product(self):
        """Выбор продукта Сноубордическая куртка Highline Pro 3L GORE-TEX®"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_window_size_product(self):
        """Нажатие на окошко размера куртки"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.window_size_product)))

    def get_size_product(self):
        """Выбор размера куртки"""

        # действие с элементом

    def click_quicksilver_logo(self):
        """Нажатие на quicksilver logo"""
        self.get_quicksilver_logo().click()
        print('Click quicksilver logo')

    def click_see_button(self):
        """Нажатие на кнопку 'СМОТРЕТЬ'"""
        self.get_see_button().click()
        print('Click SEE button')

    def choice_product(self):
        """Нажатие на продукт для выбора"""
        self.get_product().click()
        print("Choice product")

    def click_window_size_product(self):
        """Нажатие на окошко выбора размера"""
        self.get_window_size_product().click()


        #  Выбор товара

    def select_product(self):
        self.click_quicksilver_logo()
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.click_see_button()
        self.choice_product()
        self.click_window_size_product()
