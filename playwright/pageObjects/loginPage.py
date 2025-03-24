

class LoginPage:
    def __init__(self, page):
        self.page = page


    def navigate(self):
        self.page.goto('https://rahulshettyacademy.com/client')

    def login(self, userName,userPassword):
        self.page.get_by_placeholder('email@example.com').fill(userName)
        self.page.get_by_placeholder('enter your passsword').fill(userPassword)
        self.page.locator('#login').click()







