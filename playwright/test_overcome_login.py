import json
import pytest
from playwright.sync_api import Playwright, expect, Page
from utils.api_calls import API_calls

with open('data/credantiales.json') as file:
    test_data = json.load(file)
    list_of_creds =test_data['creds']


@pytest.mark.parametrize('user_creds',list_of_creds)
def test_eliminating_login(playwright:Playwright,user_creds ):
    get_token = API_calls().create_token(playwright,user_creds)
    page= playwright.chromium.launch(headless=False).new_context().new_page()
    page.add_init_script(f"""localStorage.setItem('token','{get_token}')""")
    page.goto('https://rahulshettyacademy.com/client')
    page.get_by_role("button", name='ORDERS').click()
    expect(page.get_by_text('Your Orders')).to_be_visible()




