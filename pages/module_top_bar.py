from selenium.webdriver.common.by import By
from utils.utils import slow_input
from pages.main_page_object import MainPageObject


class TopBar(MainPageObject):
    CART_COUNTER = (By.CSS_SELECTOR, "a.b-top-profile__cart .b-top-profile__counter")
    CART_LINK = (By.CLASS_NAME, "b-top-profile__cart")

    def __init__(self, browser):
        super().__init__(browser)

    def num_of_products_in_cart(self):
        return self.browser.find_element(*self.CART_COUNTER).get_attribute('innerHTML')

    def click_on_cart(self):
        r = self.browser.find_element(*self.CART_LINK)
        self.browser.execute_script("arguments[0].click();", r)  # simple click doesn't work here


class Search(MainPageObject):
    SEARCH_INPUT_BASIC = (By.NAME, "query")
    SEARCH_RESULTS = (By.CLASS_NAME, "search__result")
    SEARCH_INPUT_IN_IFRAME = (By.CLASS_NAME, "search__input")
    RESULT_PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product__title a.product__title-link")

    def __init__(self, browser):
        super().__init__(browser)

    def search_basic_input(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT_BASIC)
        search_input.send_keys(phrase)  # + Keys.RETURN

    def switch_to_search_results_iframe(self):
        self.browser.switch_to.frame(self.browser.find_element_by_class_name('modal-iframe'))

    def search_popup_input(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT_IN_IFRAME)
        slow_input(search_input, phrase)

    def search_popup_get_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT_IN_IFRAME)
        return search_input.get_attribute('value')

    def found_products(self):
        r = self.browser.find_elements(*self.RESULT_PRODUCT_TITLE)
        list_of_products = []
        for _ in r:
            list_of_products.append(_.get_attribute('innerHTML'))
        return list_of_products

    def count_results(self):
        return len(self.browser.find_elements(*self.SEARCH_RESULTS))

    def click_on_first_search_result(self):
        r = self.browser.find_element_by_class_name("product__title-link")
        r.click()
