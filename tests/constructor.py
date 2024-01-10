import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import email_xpath, password_xpath, login_button_xpath, element_souse_xpath, element_bulki_xpath, \
    element_nachinki_xpath


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/login")

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        # Вводим email в правильном формате
        email_input = self.driver.find_element(By.XPATH,email_xpath)
        email_input.click()
        email_input.send_keys("maria_kersnovskaya_4_666@gmail.com")
        time.sleep(3)

        # Вводим пароль
        password_input = self.driver.find_element(By.XPATH,password_xpath)
        password_input.click()
        time.sleep(3)
        password_input.send_keys("QwerZxcv")

        # Нажимаем на кнопку Вход
        login_button = self.driver.find_element(By.XPATH,login_button_xpath)
        login_button.click()
        time.sleep(3)

        # Ожидаем перехода на указанный URL
        expected_url = "https://stellarburgers.nomoreparties.site/"
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
        time.sleep(3)

        # Кликаем по элементу "Соусы"
        element = self.driver.find_element(By.XPATH,element_souse_xpath)
        element.click()
        'current' in element.get_attribute('class')
        time.sleep(3)

        # Кликаем по элементу "Булки"
        element = self.driver.find_element(By.XPATH,element_bulki_xpath)
        element.click()
        'current' in element.get_attribute('class')
        time.sleep(3)

        # Кликаем по элементу "Начинки"

        element = self.driver.find_element(By.XPATH,element_nachinki_xpath)
        element.click()
        'current' in element.get_attribute('class')
        time.sleep(3)

        self.driver.close()

if __name__ == '__main__':
    unittest.main()