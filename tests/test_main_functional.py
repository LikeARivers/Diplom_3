import allure
from conftest import create_user, login_user, auth_token_clean_created_user, driver
from urls import URL
from pages.main_page import MainFunctional

class TestMainFunctional:

    @allure.title('Проверка кнопки Конструктор')
    @allure.description('Проверяем что после клика на кнопку Конструктор происходит переход к конструктору бургеров')
    def test_click_constructor_button(self, driver):
        main_functional = MainFunctional(driver)
        main_functional.open_page(URL.STELLAR_BURGERS + URL.LOGIN_ENDPOINT)
        main_functional.click_to_constructor_button()

        assert main_functional.text_make_burger_on_displayed()

    @allure.title('Проверка кнопки Лента заказов')
    @allure.description('Проверяем что после клика на кнопку Лента заказов происходит переход к ленте заказов')
    def test_click_order_feed(self, driver):
        main_functional = MainFunctional(driver)
        main_functional.open_page(URL.STELLAR_BURGERS)
        main_functional.click_to_order_feed_button()
        current_url = main_functional.get_current_url()

        assert current_url == (URL.STELLAR_BURGERS + URL.ORDER_FEED_ENDPOINT)

    @allure.title('Проверка клика на ингредиент')
    @allure.description('Проверяем что после клика на ингредиент, всплывает окно с деталями')
    def test_click_constructor_button(self, driver):
        main_functional = MainFunctional(driver)
        main_functional.open_page(URL.STELLAR_BURGERS)
        main_functional.click_to_bun_r2_d3()

        assert main_functional.text_details_ingredient_on_displayed()

    @allure.title('Проверка клика крестик')
    @allure.description('Проверяем что после клика на крестик, всплывающее окно с деталями закрывается')
    def test_click_close_button(self, driver):
        main_functional = MainFunctional(driver)
        main_functional.open_page(URL.STELLAR_BURGERS)
        main_functional.click_to_bun_r2_d3()
        main_functional.click_to_close_button()

        assert main_functional.close_button_not_on_displayed()

    @allure.title('Проверка добавления ингредиента')
    @allure.description('Проверяем что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_add_ingredients(self, driver):
        main_functional = MainFunctional(driver)
        main_functional.open_page(URL.STELLAR_BURGERS)
        main_functional.drag_and_drop_bun_to_top_area()

        assert main_functional.indicator_ingredients_on_displayed()

    @allure.title('Проверка оформления заказа')
    @allure.description('Проверяем что при залогиненный пользователь может оформить заказ')
    def test_success_checkout(self, create_user, login_user, auth_token_clean_created_user, driver):
        main_functional = MainFunctional(driver)
        main_functional.drag_and_drop_bun_to_top_area()
        main_functional.click_to_checkout_button()

        assert main_functional.text_id_order_on_displayed()






