import time

from behave import *

@when('I click on the "{category_filter}" checkbox')
def steps_impl(context,category_filter):
    context.products_page.select_filter_checkbox(category_filter)

@when('I click on the "{range}" radio button')
def steps_impl(context,range):
    context.products_page.select_price_range_radio_button(range)

@then('I should have a list of products between "{range}" price')
def steps_impl(context,range):
    price_list = context.products_page.get_products_price()
    range_lower_limit, range_upper_limit = range.split("-")
    range_lower_limit = int(range_lower_limit.replace(".", ""))
    range_upper_limit = int(range_upper_limit.replace(".", ""))
    for price in price_list:
        print(price)
        assert range_lower_limit <= price <= range_upper_limit

@then('I should have a list of products with the condition described as "{conditie}"')
def steps_impl(context, conditie):
    time.sleep(5)
    products_condition_list = context.products_page.get_producs_condition()
    for product_condition in products_condition_list:
        assert product_condition == conditie, f'Expected: {conditie}, Actual: {product_condition}'