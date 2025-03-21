import time

from playwright.sync_api import Page, expect


def test_checks(page:Page):
    #hide, display, placeholder
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_visible()
    page.get_by_role('button',name='Hide').click()
    expect(page.get_by_placeholder('Hide/Show Example')).to_be_hidden()
    #alert handling
    page.on('dialog', lambda dialog: dialog.accept())
    page.get_by_role('button', name='Confirm').click()
    #hover over
    page.locator('#mousehover').hover()
    page.get_by_role('link',name='Top').click()

    # Frame handeling
    page_frame = page.frame_locator('#courses-iframe')
    page_frame.get_by_role('link', name='All Access plan').click()
    expect(page_frame.locator('body')).to_contain_text('Happy Subscibers!')

def test_table_dynamically(page: Page):
    global price_column_index
    page.goto('https://rahulshettyacademy.com/seleniumPractise/#/offers')
    for i in range(page.locator('th').count()):
        if page.locator('th').nth(i).filter(has_text='Price').count()>0:
            price_column_index=i
            break


    rise_row = page.locator('tr').filter(has_text='Rice')
    expect(rise_row.locator('td').nth(price_column_index)).to_contain_text('37')






