from behave import *


@given('I am on the "{url}" page')
def step_impl(context,url):
    context.base_page.go_to_main_page(url)


@when('I enter "{brand}" on the search bar')
def step_impl(context, brand):
    context.base_page.search_product(brand)


@when('I click on the search button')
def steps_impl(context):
    context.base_page.click_search_button()


@then('I should see "{brand}" as filter')
def step_impl(context, brand):
    element = context.base_page.get_product_title_element(brand)
    assert element is not False, \
        f"Product title with {brand} not found"


@then('I should have a list of "{brand}" products')
def step_impl(context, brand):
    products = context.products_page.get_result_products()
    assert len(products) > 0 , "No products were returned"
    for product in products:
        assert brand in product.text
