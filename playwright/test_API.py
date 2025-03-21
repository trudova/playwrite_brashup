import time

from playwright.sync_api import Playwright, expect, Page

from utils.api_calls import API_calls


def test_order_placed(playwright: Playwright):
    page = playwright.chromium.launch(headless=False).new_context().new_page()
    page.goto('https://rahulshettyacademy.com/client')
    page.get_by_placeholder('email@example.com').fill('rahulshetty@gmail.com')
    page.get_by_placeholder('enter your passsword').fill('Iamking@000')
    page.locator('#login').click()

    orderID= API_calls().create_order(playwright)

    page.get_by_role("button", name='ORDERS').click()
    order_row =page.locator('tr').filter(has_text=orderID)
    order_row.get_by_role("button", name='View').click()
    assert orderID in page.url



making_payload ={
    "data": [],
    "message": "No Orders"
}
def intercept_response(route):
    route.fulfill(
        json=making_payload
    )


def test_making_API(page:Page):
    page.goto('https://rahulshettyacademy.com/client')
    page.get_by_placeholder('email@example.com').fill('rahulshetty@gmail.com')
    page.get_by_placeholder('enter your passsword').fill('Iamking@000')
    page.locator('#login').click()

    page.route('https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*',intercept_response)
    page.get_by_role("button", name='ORDERS').click()
    no_orders_confirmation= page.locator('.mt-4').text_content()
    print(no_orders_confirmation)


def intercept_request(route):
    route.continue_(url='https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=67ddbcc9c019fb1ad632c845')

def test_making_API_dif_route(page:Page):
    page.goto('https://rahulshettyacademy.com/client')
    page.get_by_placeholder('email@example.com').fill('rahulshetty@gmail.com')
    page.get_by_placeholder('enter your passsword').fill('Iamking@000')
    page.locator('#login').click()

    page.route('https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*',intercept_request)
    page.get_by_role("button", name='ORDERS').click()
    page.get_by_role('button',name='View').first.click()
    expect(page.locator('.blink_me')).to_contain_text('You are not authorize to view this order')







