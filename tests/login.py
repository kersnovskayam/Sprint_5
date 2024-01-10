import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import email_xpath, password_xpath, login_button_xpath, personal_cabinet_link_xpath, login_xpath


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def login_action(self):
        # Вводим email в правильном формате
        email_input = self.driver.find_element(By.XPATH,email_xpath)
        email_input.click
        email_input.send_keys("maria_kersnovskaya_4_666@gmail.com")

        # Вводим пароль
        password_input = self.driver.find_element(By.XPATH,password_xpath)
        password_input.click()
        password_input.send_keys("QwerZxcv")

        # Нажимаем на кнопку Вход
        login_button = self.driver.find_element(By.XPATH,login_button_xpath)
        login_button.click()
        time.sleep(2)

        # Ожидаем перехода на указанный URL
        expected_url = "https://stellarburgers.nomoreparties.site/"
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))

    def test_login_from_main(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")
        enterButton = self.driver.find_element(By.XPATH,login_button_xpath)
        enterButton.click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        self.login_action()

    def test_login_from_lk(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")
        enterButton = self.driver.find_element(By.XPATH,personal_cabinet_link_xpath)
        enterButton.click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        self.login_action()

    def test_login_from_registration(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/register")
        enterButton = self.driver.find_element(By.XPATH,login_xpath)
        enterButton.click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        self.login_action()

    def test_login_from_forgot_pass(self):
        self.driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        enterButton = self.driver.find_element(By.XPATH,login_xpath)
        enterButton.click()
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        self.login_action()


if __name__ == '__main__':
    unittest.main()