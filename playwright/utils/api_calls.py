from playwright.sync_api import Playwright
orderpayload ={
    "orders": [
        {
            "country": "United States",
            "productOrderedId": "67a8df56c0d3e6622a297ccd"
        }
    ]
}

class API_calls:
    def create_token(self,playwright: Playwright,user_creds):
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        response = api_request_context.post('/api/ecom/auth/login',
                                            data=user_creds,
                                            headers={'Content-Type': 'application/json'})
        assert response.ok
        response.json()
        return response.json()['token']

    def create_order(self, playwright: Playwright,user_creds):
        api_request_context =playwright.request.new_context(base_url='https://rahulshettyacademy.com')
        response= api_request_context.post('api/ecom/order/create-order',
                                 data=orderpayload,
                                 headers={'Authorization': self.create_token(playwright,user_creds),
                                          'Content-Type': 'application/json'})
        order_id= response.json()['orders'][0]
        return order_id

