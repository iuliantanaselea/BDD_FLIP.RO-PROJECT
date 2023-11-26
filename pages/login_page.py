from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, 'login-email')
    PASSWORD_FIELD = (By.ID, 'login-password')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]/span[contains(text(),"Acceseaza cont")]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, 'div[class ="toasted bubble error"]')
    email = "user@email.com"
    password = "password"

    def set_email_object(self):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(self.email)

    def set_password_object(self):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(self.password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text