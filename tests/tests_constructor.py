from constants import URLS
from locators import Locators
from constants import DATA
from selenium.webdriver.common.by import By
from conftest import set_up
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructor():

    def test_sauce(self, set_up):
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
        # Ищем кнопку начинки и кликаем
        button_sauce = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.element_sauce_xpath))
        )
        button_sauce.click()

        assert button_sauce.get_attribute(
            'class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

        button_nachinki = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.element_nachinki_xpath))
        )
        button_nachinki.click()

        assert button_nachinki.get_attribute(
            'class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

        button_bulki = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.element_bulki_xpath))
        )
        button_bulki.click()

        assert button_bulki.get_attribute(
            'class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'