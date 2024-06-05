import allure
import urls
import locators
from pages.base_page import BasePage

class PersonalAccount(BasePage):
    @allure.step('клик по кнопке Личный кабинет')
    def click_to_personal_account(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    # @allure.step('в поле Email вводим {email}')
    # def input_email(self, email):
    #     element = self.wait_and_find_element(locators.SBurgersLocators.AUTHORIZATION_INPUT_EMAIL)
    #     element.send_keys(email)
    #
    # @allure.step('в поле Пароль вводим {password}')
    # def input_password(self, password):
    #     element = self.wait_and_find_element(locators.SBurgersLocators.AUTHORIZATION_INPUT_PASSWORD)
    #     element.send_keys(password)
    #
    # @allure.step('клик по кнопке Войти')
    # def click_to_login(self):
    #     element = self.wait_and_find_element(locators.SBurgersLocators.AUTHORIZATION_LOGIN_BUTTON)
    #     self.driver.execute_script("arguments[0].click();", element)

    @allure.step('ждем загрузку страницы Личный кабинет')
    def wait_personal_area_page(self):
        element = self.wait_and_find_url(urls.URL.STELLAR_BURGERS + urls.URL.ACCOUNT_PROFILE_ENDPOINT)
        return element

    # @allure.step('ждем загрузку кнопки Оформить заказ')
    # def wait_checkout_button(self):
    #     element = self.wait_and_find_element(locators.SBurgersLocators.CHECKOUT_BUTTON)

    @allure.step('клик по кнопке История заказов')
    def click_to_history_orders(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.HISTORY_ORDERS_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('ждем активацию кнопки История заказов')
    def history_order_active(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.HISTORY_ORDERS_BUTTON)
        return "Account_link_active__2opc9" in element.get_attribute("class")

    @allure.step('клик по кнопке Выход')
    def click_to_exit(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.EXIT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('ждем загрузку страницы Вход')
    def wait_login_page(self):
        element = self.wait_and_find_url(urls.URL.STELLAR_BURGERS + urls.URL.LOGIN_ENDPOINT)
        return element