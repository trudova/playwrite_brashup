from playwright.sync_api import Playwright, expect

from utils.api_calls import API_calls


def test_eliminating_login(playwright:Playwright):
    get_token = API_calls().create_token(playwright)
    page= playwright.chromium.launch(headless=False).new_context().new_page()
    page.add_init_script(f"""localStorage.setItem('token','{get_token}')""")
    page.goto('https://rahulshettyacademy.com/client')
    page.get_by_role("button", name='ORDERS').click()
    expect(page.get_by_text('Your Orders')).to_be_visible()




