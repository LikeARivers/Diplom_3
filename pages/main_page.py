import allure
import locators
from pages.base_page import BasePage
from seletools.actions import drag_and_drop

class MainFunctional(BasePage):
    @allure.step('клик по кнопке Личный кабинет')
    def click_to_personal_account(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('клик по кнопке Конструктор')
    def click_to_constructor_button(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.CONSTRUCTOR_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('проверка отображения текста Соберите бургер')
    def text_make_burger_on_displayed(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.MAKE_BURGER_TEXT)
        return element.is_displayed()

    @allure.step('клик по кнопке Лента заказов')
    def click_to_order_feed_button(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.ORDER_FEED_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('клик по кнопке Флюоресцентной булке R2-D3')
    def click_to_bun_r2_d3(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.BUN_R2_D3_IMG)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('проверка отображения текста Детали ингредиента')
    def text_details_ingredient_on_displayed(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.DETAILS_INGREDIENT)
        return element.is_displayed()

    @allure.step('провекра отсутствия крестика')
    def close_button_not_on_displayed(self):
        element = self.wait_and_find_close_element(locators.SBurgersLocators.CLOSE_BUTTON)
        return not element.is_displayed()

    @allure.step('клик по крестику')
    def click_to_close_button(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.CLOSE_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('перетаскиваем Флюоресцентную булку R2-D3 к верхней зоне добавления ингредиента')
    def drag_and_drop_bun_to_top_area(self):
        bun_element = self.wait_and_find_element(locators.SBurgersLocators.BUN_R2_D3_IMG)
        top_area_element = self.wait_and_find_element(locators.SBurgersLocators.TOP_AREA_INGREDIENTS)
        drag_and_drop(self.driver, bun_element, top_area_element)

    @allure.step('проверка счетчика ингредиента')
    def indicator_ingredients_on_displayed(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.INDICATOR_INGREDIENTS)
        return element.is_displayed()

    @allure.step('клик по кнопке Оформить заказ')
    def click_to_checkout_button(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.CHECKOUT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('проверка отображения текста идентификатор заказа')
    def text_id_order_on_displayed(self):
        element = self.wait_and_find_element(locators.SBurgersLocators.ORDERS_ID_TEXT)
        return element.is_displayed()