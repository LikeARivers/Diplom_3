from selenium import webdriver
import requests
import pytest
import urls
import data
import allure
from pages.personal_account_page import PersonalAccount
from pages.main_page import MainFunctional


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    browser.quit()

@allure.step("Авторизация")
@pytest.fixture(scope='function')
def login_user(driver):
    login_personal_account = PersonalAccount(driver)
    main_functional = MainFunctional(driver)
    login_personal_account.open_page(urls.URL.STELLAR_BURGERS)
    main_functional.click_to_personal_account()
    login_personal_account.input_email(data.StellarBurgersTestsData.EMAIL)
    login_personal_account.input_password(data.StellarBurgersTestsData.PASSWORD)
    login_personal_account.click_to_login()
    login_personal_account.wait_checkout_button()

@allure.step("Создание пользователя")
@pytest.fixture(scope='function')
def create_user():
    response_create_user = requests.post(urls.URL.STELLAR_BURGERS + urls.URL.CREATE_USER_ENDPOINT, json= data.DataCreateUser.CREATE_USER_BODY)
    return response_create_user

@allure.step("Получение токена и удаление пользователя")
@pytest.fixture(scope='function')
def auth_token_clean_created_user():
    yield
    auth_response = requests.post(urls.URL.STELLAR_BURGERS + urls.URL.AUTH_USER_ENDPOINT, json= data.DataCreateUser.CREATE_USER_BODY)
    user_access_token = auth_response.json().get("accessToken").replace("Bearer ", "")
    headers = {'Authorization': f'Bearer {user_access_token}'}
    delete_response = requests.delete(urls.URL.STELLAR_BURGERS + urls.URL.DELETE_USER_ENDPOINT, headers = headers)


