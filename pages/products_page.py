from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):
    RESULT_PRODUCTS_ELEMENTS = (By.ID, 'products')
    PRODUCT_PRICE = (By.XPATH, '//div[@data-cy="phone-real-price"]/span')
    CONDITION_FIELD = (By.CSS_SELECTOR, 'span[data-cy="phone-condition"]')

    def get_result_products(self):
        products_list = self.driver.find_elements(*self.RESULT_PRODUCTS_ELEMENTS)
        actions = ActionChains(self.driver)
        actions.move_to_element(products_list[0]).perform()
        # self.driver.execute_script("arguments[0].scrollIntoView();",products_list)
        return products_list

    def select_filter_checkbox(self, category_filter):
        checkbox = self.get_filter_checkbox(category_filter)
        actions = ActionChains(self.driver)
        actions.move_to_element(checkbox).perform()
        checkbox.click()

    def select_price_range_radio_button(self, range):
        radio_button = self.get_filter_radio_button(range)
        actions = ActionChains(self.driver)
        actions.move_to_element(radio_button).perform()
        radio_button.click()

    def get_products_price(self):
        products = self.get_result_products()
        products_price = []
        for product in products:
            price = product.find_element(*self.PRODUCT_PRICE).text
            price = int(price.replace(".", "")) / 100
            products_price.append(price)

        return products_price

    def get_producs_condition(self):
        products = self.get_result_products()
        products_condition = []
        for product in products:
            condition = product.find_element(*self.CONDITION_FIELD).text
            products_condition.append(condition)

        return products_condition
