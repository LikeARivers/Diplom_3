from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_for_text_invisible(self, locator, text):
        WebDriverWait(self.driver, 10).until(lambda driver: self.wait_and_find_element(locator).text != text)

    def wait_and_find_close_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_and_find_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))
        return url

    def open_page(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_tab(self):
        all_tabs = self.driver.window_handles
        new_tab = all_tabs[-1]
        self.driver.switch_to.window(new_tab)

    def set_element_visibility_with_js(self, element, visibility):
        self.driver.execute_script(f"arguments[0].style.visibility = '{visibility}';", element)