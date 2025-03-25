Feature: Order creation
  Test related to creating and viewing orders
  Scenario Outline: Verify the order number is present in the order ditail page url
    Given user on the loging page
    When user logs in with valid <login> and <password>
    And user creates an order with  <login> and <password>
    And user navigates to orders page
    And user fines the newly created order and navigates to this order pade
    Then order is is present in the order page url
    Examples:
      |login                 |password   |
      |rahulshetty@gmail.com"|Iamking@000|
      |anshika@gmail.com     |Iamking@000|

