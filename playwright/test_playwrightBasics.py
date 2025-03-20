import time

from playwright.sync_api import Page, Playwright, expect


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False) #works with chrom and ege
    context =browser.new_context() #incognito will be open
    page = context.new_page() #will open incognito page
    page.goto('https://rahulshettyacademy.com')

#chromium and headless mode( no browser will be visible
def test_playwright_ShortCut(page: Page): #only work with chrome, for firefox will have to set up manually
    page.goto('https://rahulshettyacademy.com')

def test_coreLocators(page: Page): #only work with chrome, for firefox will have to set up manually
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    page.get_by_label('Username').fill('rahulshettyacademy')
    page.get_by_label('Password').fill('learning2')
    page.get_by_role("combobox").select_option('teach')
    page.locator('#terms').check()
    page.get_by_role('button', name='Sign In').click()
    #Incorrect username/password.
    expect(page.get_by_text('Incorrect username/password.')).to_be_visible()

def test_firefox_browser(playwright: Playwright):  # only work with chrome, for firefox will have to set up manually
    browser = playwright.firefox.launch(headless=False)  # works with chrom and ege
    context = browser.new_context()  # incognito will be open
    page = context.new_page()  # will open incognito page
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    page.get_by_label('Username').fill('rahulshettyacademy')
    page.get_by_label('Password').fill('learning2')
    page.get_by_role("combobox").select_option('teach')
    page.locator('#terms').check()
    page.get_by_role('button', name='Sign In').click()
    # Incorrect username/password.
    expect(page.get_by_text('Incorrect username/password.')).to_be_visible()

    #time.sleep(4)
