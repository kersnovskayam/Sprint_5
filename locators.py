class Locators:
    # локатор поля email, авторизация и регистрация
    email_xpath = "//label[text()='Email']/following-sibling::input"

    # локатор поля пароль, авторизация и регистрация
    password_xpath = "//input[@type='password']"

    # локатор поля имя регистрация
    name_input_xpath = "//label[text()='Имя']/following-sibling::input"

    # локатор кнопки зарегистрироваться
    register_button_xpath = "//button[contains(@class,'button_button_type_primary')]"

    # локатор кнопки войти
    login_button_xpath = "//button[contains(@class,'button_button_type_primary')]"

    # локатор кнопки личный кабинет
    personal_cabinet_link_xpath = "(//p[text()='Личный Кабинет'])"

    # локатор уведомления о некорректном пароле
    element_page_heading_xpath = "(//p[contains(@class,'input__error text_type_main-default')])[1]"

    # локатор кнопки конструктор
    constructor_link_xpath = "(//p[text()='Конструктор'])"

    # локатор логотипа stellar burgers
    constructor_svg_xpath = "//*[@id='root']/div/header/nav/div"

    # локатор кнопки выход
    logout_xpath = "(//button[text()='Выход'])"

    # локатор таба булки
    element_bulki_xpath = "//span[text()='Булки']/parent::div"

    # локатор таба соусы
    element_sauce_xpath = "//span[text()='Соусы']/parent::div"

    # локатор таба начинки
    element_nachinki_xpath = "//span[text()='Начинки']/parent::div"

    # локатор кнопки войти, восстановление пароля
    login_xpath = "(//a[text()='Войти'])"

    # xpath локатора уведомления об ошибочном пароле
    password_error_xpath = '//p[@class="input__error text_type_main-default"]'
