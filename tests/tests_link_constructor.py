from constants import URLS
from locators import Locators
from constants import DATA
from selenium.webdriver.common.by import By
from conftest import set_up
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class TestConstructor():
    def test_link_constructor_button(self, set_up):
        driver = set_up
        # Переходим на страницу авторизации
        driver.get(URLS.LOGIN)
        # Вставляем почту в поле ввода почты
        input_login = driver.find_element(By.XPATH, Locators.email_xpath)
        input_login.click()
        input_login.send_keys(DATA.TEST_EMAIL)
        # Вставляем пароль в поле ввода пароля
        input_password = driver.find_element(By.XPATH, Locators.password_xpath)
        input_password.click()
        input_password.send_keys(DATA.PASSWORD)
        # Кликаем по кнопке авторизации
        button_auth = driver.find_element(By.XPATH, Locators.login_button_xpath)
        button_auth.click()

        button_personal_kabinet = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.personal_cabinet_link_xpath))
        )
        button_personal_kabinet.click()

        button_link_constructor = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.constructor_link_xpath))
        )
        button_link_constructor.click()
        driver.get(URLS.EXPECTED_URL)

        assert driver.current_url == URLS.EXPECTED_URL

    def test_link_constructor_logo(self, set_up):
        driver = set_up
        # Переходим на страницу авторизации
        driver.get(URLS.LOGIN)
        # Вставляем почту в поле ввода почты
        input_login = driver.find_element(By.XPATH, Locators.email_xpath)
        input_login.click()
        input_login.send_keys(DATA.TEST_EMAIL)
        # Вставляем пароль в поле ввода пароля
        input_password = driver.find_element(By.XPATH, Locators.password_xpath)
        input_password.click()
        input_password.send_keys(DATA.PASSWORD)
        # Кликаем по кнопке авторизации
        button_auth = driver.find_element(By.XPATH, Locators.login_button_xpath)
        button_auth.click()

        button_personal_kabinet = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.personal_cabinet_link_xpath))
        )
        button_personal_kabinet.click()

        button_link_constructor_logo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.constructor_svg_xpath))
        )
        button_link_constructor_logo.click()
        driver.get(URLS.EXPECTED_URL)

        assert driver.current_url == URLS.EXPECTED_URL