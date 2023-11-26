from browser import Browser
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def before_all(context):
    context.driver = Browser()
    context.base_page=BasePage()
    context.products_page =ProductsPage()
    context.login_page=LoginPage()

def after_all(context):
    context.driver.close()