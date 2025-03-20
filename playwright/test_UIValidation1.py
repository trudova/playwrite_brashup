import time

from playwright.sync_api import Page, expect


def test_add_product_to_the_cart(page:Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    page.get_by_label('Username').fill('rahulshettyacademy')
    page.get_by_label('Password').fill('learning')
    page.get_by_role("combobox").select_option('teach')
    page.locator('#terms').check()
    page.get_by_role('button', name='Sign In').click()
    iphoneProduct= page.locator('app-card').filter(has_text='iphone X')
    iphoneProduct.get_by_role('button').click()
    iphoneProduct = page.locator('app-card').filter(has_text='Nokia Edge')
    iphoneProduct.get_by_role('button').click()
    page.get_by_text('Checkout').click()
    time.sleep(4)
    expect(page.locator('.media-body')).to_have_count(2)

def test_child_window_handel(page:Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    with page.expect_popup() as new_page_ifo:
        page.locator('.blinkingText').click()
        childPage= new_page_ifo.value
        text =childPage.locator('.red').text_content()
        assert 'mentor@rahulshettyacademy.com' in text #pytest assertion


