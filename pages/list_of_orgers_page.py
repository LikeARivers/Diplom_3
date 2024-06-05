import allure
import locators
from pages.base_page import BasePage
from seletools.actions import drag_and_drop

class ListOfOrders(BasePage):

    @allure.step('Клик по кнопке Лента Заказов')
    def click_to_list_of_orders_button(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.LIST_OF_ORDERS_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Клик по заказу в ленте заказов')
    def click_to_order(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.ORDER_ON_LIST)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Проверка отображения текста Состав')
    def text_composition_on_displayed(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.COMPOSITION_TEXT)
        return element.is_displayed()

    @allure.step('Перемещение Флюоресцентную булку R2-D3 к верхней зоне добавления ингредиента')
    def drag_and_drop_bun_to_top_area(self):
        bun_element = self.wait_and_find_element(locators.SBurgersLocators.BUN_R2_D3_IMG)
        top_area_element = self.wait_and_find_element(locators.SBurgersLocators.TOP_AREA_INGREDIENTS)
        drag_and_drop(self.driver, bun_element, top_area_element)

    @allure.step('Клик по кнопке Оформить заказ')
    def click_to_checkout_button(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.CHECKOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('клик по крестику')
    def click_to_close_button(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.CLOSE_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Клик по кнопке Личный кабинет')
    def click_to_personal_account(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Клик по кнопке История заказов')
    def click_to_history_orders(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.HISTORY_ORDERS_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ожидание активацию кнопки История заказов')
    def history_order_active(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.HISTORY_ORDERS_BUTTON)
        return "Account_link_active__2opc9" in element.get_attribute("class")

    @allure.step('Ожидание загрузки карточки в Истории заказов')
    def wait_order_card(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.ORDER_CARD)

    @allure.step('Получение номера заказа из карточки в истории заказов')
    def get_id_order_card(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.HISTORY_ORDER_CARD_ID)
        return element.text

    @allure.step('Ожидание загрузки заказов в ленте заказов')
    def wait_orders_list_section(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.SECTION_LIST_OF_ORDERS)

    @allure.step('Проверка наличия номера заказа в ленте')
    def check_orders_from_history_in_list_orders(self, id_order):
        element = locators.SBurgersLocators.LIST_OF_ORDERS_CARD_ID
        xpath_with_text = f"{element[1]}[contains(text(), '{id_order}')]"
        element_with_text = (element[0], xpath_with_text)
        return self.wait_and_find_element(element_with_text)

    @allure.step('Получение количества заказов, выполненных за все время')
    def get_completed_for_all_time(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.ORDERS_COMPLETED_FOR_ALL_TIME)
        return element.text

    @allure.step('Получение количества заказов, выполненных за сегодня')
    def get_completed_for_today(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.ORDERS_COMPLETED_FOR_TODAY)
        return element.text

    @allure.step('Клик по кнопке Конструктор')
    def click_to_constructor_button(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.CONSTRUCTOR_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ожидание загрузки номера заказа')
    def wait_order_details_number(self):
        self.wait_for_text_invisible(locators.SBurgersLocators.ORDER_DETAILS, '9999')

    @allure.step('Получение номера заказа')
    def get_order_number(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.ORDER_NUMBER)
        return element.text

    @allure.step('Проверка наличия номера заказа в работе')
    def check_order_number_in_progress(self, order_number):
        element = locators.SBurgersLocators.ORDER_NUMBER_IN_PROGRESS
        xpath_with_text = f"{element[1]}[contains(normalize-space(), '{order_number}')]"
        element_with_text = (element[0], xpath_with_text)
        return self.wait_and_find_element(element_with_text)

