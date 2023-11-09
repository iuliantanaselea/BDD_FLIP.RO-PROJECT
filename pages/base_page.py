from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from browser import Browser


class BasePage(Browser):
    SEARCH_BAR_ELEMENT = (By.XPATH, '//input[@class=\"searchBarInput form-control\"]')
    SEARCH_BUTTON = (By.XPATH, '//section[@id=\"searchBar\"]//legend')
    COOKIE_BUTTON =(By.CSS_SELECTOR,'.cookie-text button.primary')
    def go_to_main_page(self):
        self.driver.get("https://flip.ro/")
        self.driver.find_element(*self.COOKIE_BUTTON).click()

    def search_product(self, brand):
        self.driver.find_element(*self.SEARCH_BAR_ELEMENT).send_keys(brand)

    def click_search_button(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def get_product_title_element(self, brand):
        try:
            product_title= self.driver.find_element(By.XPATH, f'//h1[contains(text(),"{brand}")]')
            actions = ActionChains(self.driver)
            actions.move_to_element(product_title).perform()
            return product_title
        except NoSuchElementException:
            return False