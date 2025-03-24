import json
import time
import pytest
from playwright.sync_api import Playwright, expect, Page
from pageObjects.loginPage import LoginPage
from utils.api_calls import API_calls

with open('data/credantiales.json') as file:
    test_data = json.load(file)
    list_of_creds =test_data['creds']


@pytest.mark.parametrize('user_creds',list_of_creds)
def test_order_placed(playwright: Playwright,browser_instance, user_creds):
    print(user_creds)
    userName =user_creds['userEmail']
    userPassword =user_creds['userPassword']
    loginPage = LoginPage(browser_instance)
    #loginPage.navigate() - done in fixture
    dash_board_page = loginPage.login(userName,userPassword)
    #dash_board_page = DashboardPage(page)
    orderID= API_calls().create_order(playwright,user_creds)
    order_history = dash_board_page.select_orders_link()
    order_history.get_view_of_specific_order(orderID)
    assert orderID in browser_instance.url



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







