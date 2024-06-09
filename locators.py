from selenium.webdriver.common.by import By


class SBurgersLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # кнопка Личный кабинет
    RESTORE_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")  # кнопка Восстановить пароль на странице авторизации
    INPUT_EMAIL = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")  # поле Email на странице регистрации
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")  # кнопка Восстановить на странице восстановления пароля
    NON_ACTIVE_INPUT_NEW_PASSWORD = (By.XPATH, "//div[contains(@class, 'input') and contains(@class, 'input_type_text') and contains(@class, 'input_size_default')]")  # неактивное поле Пароль на странице восстановления пароля
    SHOW_HIDE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "div.input__icon.input__icon-action svg path") #кнопка показать/скрыть пароль
    AUTHORIZATION_INPUT_EMAIL = (By.XPATH, "//input[@name='name']")  # поле Email на странице авторизации
    AUTHORIZATION_INPUT_PASSWORD = (By.XPATH, "//input[@name='Пароль']")  # поле Пароль на странице авторизации
    AUTHORIZATION_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка Войти на странице авторизации
    CHECKOUT_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # кнопка Оформить заказ в конструкторе
    HISTORY_ORDERS_BUTTON = (By.XPATH, "//a[@href='/account/order-history']") # кнопка История заказов в личном кабинете
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']") # кнопка выход в личном кабинете
    CONSTRUCTOR_BUTTON = (By.CLASS_NAME, "AppHeader_header__linkText__3q_va")  # кнопка Конструктор
    MAKE_BURGER_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")  # текст Соберите бургер на главной странице
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']") # кнопка Лента заказов
    BUN_R2_D3_IMG = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']") # Флюоресцентная булка R2-D3
    DETAILS_INGREDIENT = (By.XPATH, "//h2[text()='Детали ингредиента']") # надпись Детали ингредиента во всплывающем окне
    CLOSE_BUTTON = (By.CLASS_NAME, "Modal_modal__close__TnseK") # кнопка закрытия окна
    TOP_AREA_INGREDIENTS = (By.CSS_SELECTOR, 'span.constructor-element__text') # верхняя зона добавления ингредиента
    INDICATOR_INGREDIENTS = (By.XPATH, '//p[@class="counter_counter__num__3nue1" and text()="2"]') #счетчик ингредиента
    ORDERS_ID_TEXT = (By.XPATH, "//p[text()='идентификатор заказа']") # надпись идентификатор заказа в окне оформления заказа
    ORDER_ON_LIST = (By.CLASS_NAME, "OrderHistory_dataBox__1mkxK") # первый заказ в ленте заказов
    COMPOSITION_TEXT = (By.XPATH, "//p[text()='Cостав']") # текст Состав в окне с деталями заказа
    ORDER_CARD = (By.XPATH, "//*[contains(@class, 'OrderHistory_listItem')]") # карточка с заказом в истории заказов
    HISTORY_ORDER_CARD_ID = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[1]") # номер заказа в истории заказов
    SECTION_LIST_OF_ORDERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]") # карточки заказов в ленте заказов
    LIST_OF_ORDERS_CARD_ID = (By.XPATH, "(//p[contains(@class, 'text text_type_digits-default')])[1]") # номер заказа в ленте заказов
    ORDERS_COMPLETED_FOR_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p") # количество заказов, выполненных за все время
    ORDERS_COMPLETED_FOR_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")  # количество заказов, выполненных за сегодня
    ORDER_DETAILS = (By.XPATH, '//h2[contains(@class, "text_type_digits-large")]') # детали заказа
    ORDER_NUMBER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2") # номер оформленного заказа
    ORDER_NUMBER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[contains(@class, 'text_type_digits-default')]") # номер заказа в работе