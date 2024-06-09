import allure
from conftest import driver, login_user, create_user, auth_token_clean_created_user
from urls import URL
from pages.list_of_orgers_page import ListOfOrders
from pages.main_page import MainFunctional

class TestListOfOrders:

    @allure.title('Проверка всплывающего окна детали заказа')
    @allure.description('Проверяем что после клика на заказ, всплывает окно с деталями заказа')
    def test_click_to_order(self, driver):
        list_of_orders = ListOfOrders(driver)
        main_functional = MainFunctional(driver)
        list_of_orders.open_page(URL.STELLAR_BURGERS)
        main_functional.click_to_order_feed_button()
        list_of_orders.click_to_order()

        assert list_of_orders.text_composition_on_displayed()

    @allure.title('Проверка отображения заказов пользователя в Ленте заказов')
    @allure.description('Проверяем что заказы пользователя из раздела История заказов отображаются на странице Лента заказов')
    def test_history_order_on_list_of_order(self, create_user, login_user, auth_token_clean_created_user, driver):
        list_of_orders = ListOfOrders(driver)
        main_functional = MainFunctional(driver)
        main_functional.drag_and_drop_bun_to_top_area()
        main_functional.click_to_checkout_button()
        main_functional.click_to_close_button()
        main_functional.click_to_personal_account()
        list_of_orders.click_to_history_orders()
        list_of_orders.history_order_active()
        list_of_orders.wait_order_card()
        id_order = list_of_orders.get_id_order_card()
        main_functional.click_to_order_feed_button()
        list_of_orders.wait_orders_list_section()

        assert list_of_orders.check_orders_from_history_in_list_orders(id_order)

    @allure.title('Проверка счетчика Выполнено за все время')
    @allure.description('Проверяем что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_completed_for_all_time(self, create_user, login_user, auth_token_clean_created_user, driver):
        list_of_orders = ListOfOrders(driver)
        main_functional = MainFunctional(driver)
        list_of_orders.open_page(URL.STELLAR_BURGERS + URL.ORDER_FEED_ENDPOINT)
        numbers_before_order = list_of_orders.get_completed_for_all_time()
        main_functional.click_to_constructor_button()
        main_functional.drag_and_drop_bun_to_top_area()
        main_functional.click_to_checkout_button()
        main_functional.click_to_close_button()
        main_functional.click_to_order_feed_button()
        list_of_orders.wait_orders_list_section()
        numbers_after_order = list_of_orders.get_completed_for_all_time()

        assert numbers_before_order < numbers_after_order

    @allure.title('Проверка счетчика Выполнено за сегодня')
    @allure.description('Проверяем что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_completed_for_today(self, create_user, login_user, auth_token_clean_created_user, driver):
        list_of_orders = ListOfOrders(driver)
        main_functional = MainFunctional(driver)
        list_of_orders.open_page(URL.STELLAR_BURGERS + URL.ORDER_FEED_ENDPOINT)
        numbers_before_order = list_of_orders.get_completed_for_today()
        main_functional.click_to_constructor_button()
        main_functional.drag_and_drop_bun_to_top_area()
        main_functional.click_to_checkout_button()
        main_functional.click_to_close_button()
        main_functional.click_to_order_feed_button()
        list_of_orders.wait_orders_list_section()
        numbers_after_order = list_of_orders.get_completed_for_today()

        assert numbers_before_order < numbers_after_order

    @allure.title('Проверка счетчика В работе')
    @allure.description('Проверяем что после оформления заказа его номер появляется в разделе В работе')
    def test_order_in_progress(self, create_user, login_user, auth_token_clean_created_user, driver):
        list_of_orders = ListOfOrders(driver)
        main_functional = MainFunctional(driver)
        main_functional.drag_and_drop_bun_to_top_area()
        main_functional.click_to_checkout_button()
        list_of_orders.wait_order_details_number()
        order_number = list_of_orders.get_order_number()
        main_functional.click_to_close_button()
        main_functional.click_to_order_feed_button()
        list_of_orders.wait_orders_list_section()

        assert list_of_orders.check_order_number_in_progress(order_number)






