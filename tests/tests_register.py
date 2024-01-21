from constants import URLS
from locators import Locators
from constants import DATA
from selenium.webdriver.common.by import By
from conftest import set_up
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class TestRegister():

    def test_fail(self, set_up):
        driver = (set_up)

        # Открываем страницу регистрации
        driver.get(URLS.REGISTER)
        # Вставляем почту в поле ввода почты
        input_login = driver.find_element(By.XPATH, Locators.email_xpath)
        input_login.click()
        input_login.send_keys(DATA.REGISTER_EMAIL)
        # Вставляем пароль в поле ввода пароля
        input_password = driver.find_element(By.XPATH, Locators.password_xpath)
        input_password.click()
        input_password.send_keys(DATA.INCORRECT_PASSWORD)
        # Вставляем имя в поле ввода имени
        input_name = driver.find_element(By.XPATH, Locators.name_input_xpath)
        input_name.click()
        input_name.send_keys(DATA.NAME)
        # Кликаем по кнопке регистрации
        button_register = driver.find_element(By.XPATH, Locators.register_button_xpath)
        button_register.click()
        # Ищем элемент всплывающей ошибки
        error_message = driver.find_element(By.XPATH, Locators.password_error_xpath)

        assert error_message.text == 'Некорректный пароль'

    def test_success(self, set_up):
        driver = (set_up)

        # Открываем страницу регистрации
        driver.get(URLS.REGISTER)
        # Вставляем почту в поле ввода почты
        input_login = driver.find_element(By.XPATH, Locators.email_xpath)
        input_login.click()
        input_login.send_keys(DATA.REGISTER_EMAIL)

        # Вставляем пароль в поле ввода пароля
        input_password = driver.find_element(By.XPATH, Locators.password_xpath)
        input_password.click()
        input_password.send_keys(DATA.PASSWORD)

        # Вставляем имя в поле ввода имени
        input_name = driver.find_element(By.XPATH, Locators.name_input_xpath)
        input_name.click()
        input_name.send_keys(DATA.NAME)

        # Килкаем по кнопке регистрации
        button_register = driver.find_element(By.XPATH, Locators.register_button_xpath)
        button_register.click()
        # Переходим на страницу авторизации
        driver.get(URLS.LOGIN)

        # Вставляем почту в поле ввода почты
        input_login = driver.find_element(By.XPATH, Locators.email_xpath)
        input_login.click()
        input_login.send_keys(DATA.REGISTER_EMAIL)

        # Вставляем пароль в поле ввода пароля
        input_password = driver.find_element(By.XPATH, Locators.password_xpath)
        input_password.click()
        input_password.send_keys(DATA.PASSWORD)

        # Кликаем по кнопке авторизации
        button_auth = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.login_button_xpath))
        )
        button_auth.click()
        driver.get(URLS.URL_MAIN)

        assert driver.current_url == URLS.URL_MAIN