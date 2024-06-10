import allure
import data
from conftest import driver
from urls import URL
from pages.restore_password_page import RestorePassword

class TestRestorePassword:

    @allure.title('Проверка кнопки Восстановить пароль')
    @allure.description('Проверяем что после клика на кнопку Восстановить пароль происходит переход к форме восстановления пароля, полю ввода почты')
    def test_click_restore_password_button(self, driver):
        restore_password_pages = RestorePassword(driver)
        restore_password_pages.open_page(URL.STELLAR_BURGERS)
        restore_password_pages.click_to_personal_account()
        restore_password_pages.click_to_restore_password()
        current_url = restore_password_pages.get_current_url()
        assert current_url == (URL.STELLAR_BURGERS + URL.FORGOT_PASSWORD_ENDPOINT)

    @allure.title('Проверка ввода почты и клика по кнопке Восстановить')
    @allure.description('Проверяем что после ввода почты, клика на кнопку Восстановить происходит переход к полям ввода пароля и кода')
    def test_input_email_and_click_restore_button(self,driver):
        restore_password_pages = RestorePassword(driver)
        restore_password_pages.open_page(URL.STELLAR_BURGERS + URL.FORGOT_PASSWORD_ENDPOINT)
        restore_password_pages.input_email(data.StellarBurgersTestsData.EMAIL)
        restore_password_pages.click_to_restore_button()
        restore_password_pages.wait_restore_password_page()
        current_url = restore_password_pages.get_current_url()
        assert current_url == (URL.STELLAR_BURGERS + URL.RESET_PASSWORD_ENDPOINT)

    @allure.title('Проверка подсветки поля пароль')
    @allure.description('Проверяем что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_eye_active_password_input(self, driver):
        restore_password_pages = RestorePassword(driver)
        restore_password_pages.open_page(URL.STELLAR_BURGERS + URL.RESET_PASSWORD_ENDPOINT)
        restore_password_pages.input_email(data.StellarBurgersTestsData.EMAIL)
        restore_password_pages.click_to_restore_button()
        restore_password_pages.wait_restore_password_page()
        restore_password_pages.click_eye_button()
        assert restore_password_pages.password_input_active()





