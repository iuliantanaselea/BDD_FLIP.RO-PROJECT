from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from browser import Browser


class BasePage(Browser):
    SEARCH_BAR_ELEMENT = (By.XPATH, '//input[@class=\"searchBarInput form-control\"]')
    SEARCH_BUTTON = (By.XPATH, '//section[@id=\"searchBar\"]//legend')
    COOKIE_BUTTON =(By.CSS_SELECTOR,'.cookie-text button.primary')
    GO_TO_MAINPAGE_BUTTON = (By.XPATH,'//button//div[contains(text(),\"Mergi la flip.ro\")]/ancestor::button')
    def go_to_main_page(self,url):
        self.driver.get(url)
        try:
            self.driver.find_element(*self.COOKIE_BUTTON).click()
        except NoSuchElementException:
            pass
        # TODO: This action not working
        # try:
        #     self.redirect_to_main_page()
        # except NoSuchElementException:
        #     pass


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

    def redirect_to_main_page(self):
        self.driver.find_element(*self.GO_TO_MAINPAGE_BUTTON).click()

    def get_filter_checkbox(self,filter):
        # return self.driver.find_element(By. CSS_SELECTOR, f'input[value="{filter}"][type="checkbox"]')
        return self.driver.find_element(By. XPATH, f'//input[@value="{filter}"][@type=\"checkbox\"]/ancestor::div[@class=\"d-block pt-3 secondary custom-control custom-control-inline custom-checkbox\"]')

    def get_filter_radio_button(self,filter):
        return self.driver.find_element(By.XPATH,f'//label[contains(text(),"{filter}")]/ancestor::div[@class="d-block pt-3 secondary custom-control custom-control-inline custom-radio"]')

    def get_condition_filter_checkbox(self, filter):
        return self.driver.find_element(By.XPATH, f'//div/label[contains(text(),"{filter}")]')

