import allure
from conftest import create_user, login_user, auth_token_clean_created_user, driver
from urls import URL
from pages.personal_account_page import PersonalAccount
from pages.main_page import MainFunctional


class TestPersonalAccount:

    @allure.title('Проверка кнопки Личный кабинет')
    @allure.description('Проверяем что после клика на кнопку Личный кабинет происходит переход к личному кабинету пользователя')
    def test_click_login_personal_account(self, create_user, login_user, auth_token_clean_created_user, driver):
        personal_account = PersonalAccount(driver)
        main_functional = MainFunctional(driver)
        main_functional.click_to_personal_account()
        personal_account.wait_personal_area_page()
        current_url = personal_account.get_current_url()

        assert current_url == (URL.STELLAR_BURGERS + URL.ACCOUNT_PROFILE_ENDPOINT)

    @allure.title('Проверка кнопки История заказов')
    @allure.description('Проверяем что после клика на кнопку История заказов происходит переход к истории заказов пользователя')
    def test_click_history_orders(self, create_user, login_user, auth_token_clean_created_user, driver):
        personal_account = PersonalAccount(driver)
        main_functional = MainFunctional(driver)
        main_functional.click_to_personal_account()
        personal_account.wait_personal_area_page()
        personal_account.click_to_history_orders()

        assert personal_account.history_order_active()

    @allure.title('Проверка кнопки Выход из аккаунта')
    @allure.description('Проверяем что после клика на кнопку Выход из аккаунта происходит выход из аккаунта пользователя')
    def test_click_exit(self, create_user, login_user, auth_token_clean_created_user, driver):
        personal_account = PersonalAccount(driver)
        main_functional = MainFunctional(driver)
        main_functional.click_to_personal_account()
        personal_account.click_to_exit()
        personal_account.wait_login_page()
        current_url = personal_account.get_current_url()

        assert current_url == (URL.STELLAR_BURGERS + URL.LOGIN_ENDPOINT)
