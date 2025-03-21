import time

from playwright.sync_api import Playwright, expect

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






