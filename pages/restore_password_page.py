import allure
import urls
import locators
from pages.base_page import BasePage

class RestorePassword(BasePage):
    @allure.step('клик по кнопке Личный кабинет')
    def click_to_personal_account(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('клик по кнопке Восстановить пароль')
    def click_to_restore_password(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.RESTORE_PASSWORD_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('в поле Email вводим {email}')
    def input_email(self, email):
        element = self.wait_and_find_element(locators.SBurgersLocators.INPUT_EMAIL)
        element.send_keys(email)

    @allure.step('клик по кнопке Восстановить')
    def click_to_restore_button(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.RESTORE_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('ждем загрузку страницы Восстановления пароля')
    def wait_restore_password_page(self):
        element = self.wait_and_find_url(urls.URL.STELLAR_BURGERS + urls.URL.RESET_PASSWORD_ENDPOINT)
        return element

    @allure.step('кликаем на кнопку показать/скрыть пароль')
    def click_eye_button(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.SHOW_HIDE_PASSWORD_BUTTON)
        self.driver.execute_script("arguments[0].style.visibility = 'visible';", element)
        element.click()

    @allure.step('ждем активацию кнопки')
    def password_input_active(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.NON_ACTIVE_INPUT_NEW_PASSWORD)
        return "input_status_active" in element.get_attribute("class")


