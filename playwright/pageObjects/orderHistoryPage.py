class OrderHistoryPage:
    def __init__(self, page):
        self.page = page

    def get_view_of_specific_order(self,orderID):
        order_row = self.page.locator('tr').filter(has_text=orderID)
        order_row.get_by_role("button", name='View').click()


