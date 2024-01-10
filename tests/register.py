import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.locators import name_input_xpath, email_input_xpath, password_input_xpath, register_button_xpath, email_xpath, \
    password_xpath, login_button_xpath, element_page_heading_xpath


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/register")

    def tearDown(self):
        self.driver.quit()

    def test_successful_registration(self):
        # Вводим имя
        name_input = self.driver.find_element(By.XPATH, name_input_xpath)
        name_input.click()
        time.sleep(1)
        name_input.send_keys("Имя Фамилия")
        time.sleep(1)

        # Вводим email в правильном формате
        email_input = self.driver.find_element(By.XPATH, email_input_xpath)
        email_input.click()
        time.sleep(1)
        email_input.send_keys("qwerty12345678919@ya.ru")
        time.sleep(1)

        # Вводим пароль
        password_input = self.driver.find_element(By.XPATH, password_input_xpath)
        password_input.click()
        time.sleep(1)
        password_input.send_keys("123456")
        time.sleep(1)

        # Нажимаем на кнопку регистрации
        register_button = self.driver.find_element(By.XPATH,register_button_xpath)
        register_button.click()
        time.sleep(1)

        # Ожидаем перехода на указанный URL
        expected_url = "https://stellarburgers.nomoreparties.site/login"

        # Проверяем, что произошел успешный переход
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_url)

        # Вводим email в правильном формате
        email_input = self.driver.find_element(By.XPATH, email_xpath)
        email_input.click()
        email_input.send_keys("qwerty12345678919@ya.ru")

        # Вводим пароль
        password_input = self.driver.find_element(By.XPATH, password_xpath)
        password_input.click()
        password_input.send_keys("123456")

        # Нажимаем на кнопку Вход
        login_button = self.driver.find_element(By.XPATH, login_button_xpath)
        login_button.click()
        time.sleep(2)

    def test_fail_registration(self):
        # Вводим имя
        name_input = self.driver.find_element(By.XPATH,name_input_xpath)
        name_input.click()
        time.sleep(1)
        name_input.send_keys("Имя Фамилия")

        # Вводим email в правильном формате
        email_input = self.driver.find_element(By.XPATH, email_input_xpath)
        email_input.click()
        time.sleep(1)
        email_input.send_keys("1234@ya.ru")

        # Вводим пароль
        password_input = self.driver.find_element(By.XPATH,password_input_xpath)
        password_input.click()
        time.sleep(1)
        password_input.send_keys("123")

        # Нажимаем на кнопку регистрации
        register_button = self.driver.find_element(By.XPATH,register_button_xpath)
        register_button.click()
        time.sleep(1)

        element_page_heading = self.driver.find_element(By.XPATH, element_page_heading_xpath)
        assert element_page_heading.text == 'Некорректный пароль'


if __name__ == '__main__':
    unittest.main()