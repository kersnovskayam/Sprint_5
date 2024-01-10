import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import email_xpath, password_xpath, login_button_xpath, personal_cabinet_link_xpath, \
    constructor_link_xpath, constructor_svg_xpath


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

    def test_successful_login(self):
        # Вводим email в правильном формате
        email_input = self.driver.find_element(By.XPATH,email_xpath)
        email_input.clear()
        email_input.send_keys("maria_kersnovskaya_4_666@gmail.com")

        # Вводим пароль
        password_input = self.driver.find_element(By.XPATH,password_xpath)
        password_input.click()
        password_input.send_keys("QwerZxcv")

        # Нажимаем на кнопку Вход
        login_button = self.driver.find_element(By.XPATH,login_button_xpath)
        login_button.click()

        # Ожидаем перехода на указанный URL
        expected_url = "https://stellarburgers.nomoreparties.site/"
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

        # Клик на "Личный Кабинет"
        personal_cabinet_link = self.driver.find_element(By.XPATH,personal_cabinet_link_xpath)
        personal_cabinet_link.click()

        # Ожидаем перехода на указанный URL
        expected_url = "https://stellarburgers.nomoreparties.site/account/profile"
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

        # Клик по "Конструктор"
        constructor_link = self.driver.find_element(By.XPATH,constructor_link_xpath)
        constructor_link.click()

        # Ожидаем перехода на указанный URL
        expected_url = "https://stellarburgers.nomoreparties.site/"
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

        # Клик на "Личный Кабинет"
        personal_cabinet_link = self.driver.find_element(By.XPATH,personal_cabinet_link_xpath)
        personal_cabinet_link.click()

        # Ожидаем перехода на указанный URL
        expected_url = "https://stellarburgers.nomoreparties.site/account/profile"
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

        # Клик логотипу Stellar Burgers"
        constructor_svg = self.driver.find_element(By.XPATH,constructor_svg_xpath)
        constructor_svg.click()

        # Ожидаем перехода на указанный URL
        expected_url = "https://stellarburgers.nomoreparties.site/"
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

        self.driver.close()

if __name__ == '__main__':
    unittest.main()