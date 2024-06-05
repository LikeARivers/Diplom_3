from selenium import webdriver
import requests
import pytest
import urls
import data
import allure
from locators import SBurgersLocators
from pages.base_page import BasePage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    browser.maximize_window()
    #browser.get(urls.URL.STELLAR_BURGERS)

    yield browser

    browser.quit()

@allure.step("Авторизация")
@pytest.fixture(scope='function')
def login_user(driver):
    base_page = BasePage(driver)
    base_page.open_page(urls.URL.STELLAR_BURGERS)
    personal_account_click = base_page.wait_and_find_element(SBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
    driver.execute_script("arguments[0].click();", personal_account_click)
    input_email = base_page.wait_and_find_element(SBurgersLocators.AUTHORIZATION_INPUT_EMAIL)
    input_email.send_keys(data.StellarBurgersTestsData.EMAIL)
    input_password = base_page.wait_and_find_element(SBurgersLocators.AUTHORIZATION_INPUT_PASSWORD)
    input_password.send_keys(data.StellarBurgersTestsData.PASSWORD)
    click_to_login = base_page.wait_and_find_element(SBurgersLocators.AUTHORIZATION_LOGIN_BUTTON)
    driver.execute_script("arguments[0].click();", click_to_login)
    wait_checkout_button = base_page.wait_and_find_element(SBurgersLocators.CHECKOUT_BUTTON)

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


