from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import src
from base.base_class import Base
from src import Locators_login


class LoginPage(Base, Locators_login):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    # поиск элемента на странице

    def get_account_button(self):
        """Кнопка 'ВОЙТИ'"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.account_button)))

    def get_login_email(self):
        """Поле ввода логина"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_email)))

    def get_password(self):
        """Поле ввода пароля"""
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    # действие с элементом

    def click_account_button(self):
        """Нажатие на кнопку 'ВОЙТИ'"""
        self.get_account_button().click()
        print('Click account button')

    def input_login(self, login_email):
        """Ввод логина"""
        self.get_login_email().send_keys(login_email)
        print('Input login')

    def input_password(self, password):
        """Ввод пароля"""
        self.get_password().send_keys(password)
        print("Input password")

    def click_enter_button(self):
        self.get_enter_button().click()
        print('Click enter button')

    def autorization(self):
        """Проходим все этапы авторизации"""
        self.click_account_button()
        self.input_login(src.LOGIN)
        self.input_password(src.PASSWORD)
        self.click_enter_button()
