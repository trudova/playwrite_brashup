from pytest_bdd import given, scenarios, when,parsers

scenarios('.features/orderCreation.feature')
@given('user on the loging page')
def navigate_to_login():
    print('test TEST')

@when(parsers.parse('user logs in with valid {login} and {password}'))
def login_to_the_app(login,password ):
    print(f'WORKS {login}, {password}')
