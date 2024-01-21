import random

rand = random.randint(1,150)
class URLS:
    URL_MAIN = 'https://stellarburgers.nomoreparties.site/'
    EXPECTED_URL = 'https://stellarburgers.nomoreparties.site/'
    EXPECTED_URL_PERSONAL = 'https://stellarburgers.nomoreparties.site/account/profile'
    REGISTER = 'https://stellarburgers.nomoreparties.site/register'
    LOGIN = 'https://stellarburgers.nomoreparties.site/login'


class DATA:
    INCORRECT_PASSWORD = '123'
    PASSWORD = 'QwerZxcv'
    TEST_EMAIL = 'maria_kersnovskaya_4_666@gmail.com'
    REGISTER_EMAIL = f'qwerty{rand}@ya.ru'
    NAME = 'Имя Фамилия'
