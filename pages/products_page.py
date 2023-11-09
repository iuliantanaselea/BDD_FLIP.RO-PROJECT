from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):
    RESULT_PRODUCTS_ELEMENTS = (By.ID, 'products')

    def get_result_products(self):
        products_list = self.driver.find_elements(*self.RESULT_PRODUCTS_ELEMENTS)
        actions = ActionChains(self.driver)
        actions.move_to_element(products_list[0]).perform()
        # self.driver.execute_script("arguments[0].scrollIntoView();",products_list)
        return products_list
