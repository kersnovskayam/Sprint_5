from selenium.webdriver import Chrome
import pytest

@pytest.fixture()
def set_up():
    driver = Chrome()
    driver.implicitly_wait(10)
    yield driver

    driver.quit()