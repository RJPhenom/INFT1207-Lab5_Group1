# *************************************************************************************
# Title:        Lab 5 Selenium WebDriver Women's Shopping Test Script
# Author:       Robert Macklem
# Date:         March 28 2024
# Description:  Tests website functionality at https://magento.softwaretestingboard.com
#               using Selenium WebDriver
# *************************************************************************************
import time
# Import necessary libraries / modules
from time import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# Define test class
class ShoppingTest:
    def setup(self, method):
        print("Setting up...")  # Debug print
        self.driver = webdriver.Firefox()

    def teardown(self, method):
        print("Tearing down...")  # Debug print
        self.driver.quit()

    def test_navigate_to_category(self, navigator: ActionChains):
        # Click on Women -> Tops -> Hoodies & Sweatshirts
        # XPATHS
        primary_xpath = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[2]"
        secondary_xpath = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/a[1]"
        tertiary_xpath = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/ul[1]/li[1]/a[1]"
        target_xpath = "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/ul[1]/li[2]/a[1]"

        # Get our ELEMENTS
        top_menu = self.driver.find_element(By.XPATH, primary_xpath)  # Finds top-level navigation menu element
        sub_menu = self.driver.find_element(By.XPATH, secondary_xpath)  # Finds second-level navigation menu element
        offset = self.driver.find_element(By.XPATH, tertiary_xpath)  # Moves cursor to avoid closing dropdown menu
        target = self.driver.find_element(By.XPATH, target_xpath)  # Finds the target menu item

        # Navigate submenus to element
        navigator.move_to_element(top_menu).perform()
        navigator.move_to_element(sub_menu).perform()
        navigator.move_to_element(offset).perform()
        navigator.move_to_element(target).perform()

        # Click the link
        target.click()

    def test_set_filters(self, navigator: ActionChains):
        # Select the appropriate Style, Size, Price Range, Color and Material. For e.g.:
        # Style: Pullover, Size: M, Price: $50.00 - $59.99, Color: Purple, Material: Polyester

        # 2a --STYLE--
        # --------------------------------------------------------------------------------------------------------------
        style_xpath = "/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]"
        pullover_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]/div[1]"
                          "/div[2]/div[1]/div[1]/div[2]/ol[1]/li[3]/a[1]")

        style = self.driver.find_element(By.XPATH, style_xpath)
        pullover = self.driver.find_element(By.XPATH, pullover_xpath)

        navigator.move_to_element(style).perform()
        style.click()

        navigator.move_to_element(pullover).perform()
        pullover.click()
        sleep(1)

        # 2b --SIZE--
        # --------------------------------------------------------------------------------------------------------------
        size_xpath = "/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]"
        m_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]/div[1]"
                   "/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/a[3]/div[1]")

        size = self.driver.find_element(By.XPATH, size_xpath)
        m = self.driver.find_element(By.XPATH, m_xpath)

        navigator.move_to_element(size).perform()
        size.click()

        navigator.move_to_element(m).perform()
        m.click()
        sleep(1)

        # 2c --PRICE--
        # --------------------------------------------------------------------------------------------------------------
        price_xpath = "/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div[1]"
        fifty_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]"
                       "/div[1]/div[2]/div[3]/div[1]/div[2]/ol[1]/li[3]/a[1]")

        price = self.driver.find_element(By.XPATH, price_xpath)
        fifty = self.driver.find_element(By.XPATH, fifty_xpath)

        navigator.move_to_element(price).perform()
        price.click()

        navigator.move_to_element(fifty).perform()
        fifty.click()
        sleep(1)

        # 2d --COLOUR--
        # --------------------------------------------------------------------------------------------------------------
        color_xpath = "/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div[1]"
        purple_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]"
                        "/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/a[4]/div[1]")

        color = self.driver.find_element(By.XPATH, color_xpath)
        purple = self.driver.find_element(By.XPATH, purple_xpath)

        navigator.move_to_element(color).perform()
        color.click()

        navigator.move_to_element(purple).perform()
        purple.click()
        sleep(1)

        # 2e --MATERIAL--
        # --------------------------------------------------------------------------------------------------------------
        material_xpath = "/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div[1]"
        polyester_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]"
                           "/div[1]/div[2]/div[3]/div[1]/div[2]/ol[1]/li[3]/a[1]")

        material = self.driver.find_element(By.XPATH, material_xpath)
        polyester = self.driver.find_element(By.XPATH, polyester_xpath)

        navigator.move_to_element(material).perform()
        material.click()

        navigator.move_to_element(polyester).perform()
        polyester.click()
        sleep(1)

    def test_select_item(self, navigator: ActionChains):
        # Select any single dress (if there are multiple depending upon your selection) and click on Add to cart
        item_xpath = "/html[1]/body[1]/div[2]/main[1]/div[3]/div[1]/div[4]/ol[1]/li[1]/div[1]"
        item = self.driver.find_element(By.XPATH, item_xpath)

        navigator.move_to_element(item)
        item.click()
        sleep(3)

        # Confirm style selections (this website should have been coded to do this based on filters... lame)
        # Size...
        size_option_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[2]"
                             "/div[4]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]")
        size_option = self.driver.find_element(By.XPATH, size_option_xpath)
        navigator.move_to_element(size_option)
        size_option.click()
        sleep(1)

        # Color...
        color_option_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[2]"
                              "/div[4]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]")
        color_option = self.driver.find_element(By.XPATH, color_option_xpath)

        navigator.move_to_element(color_option)
        color_option.click()
        sleep(1)

        # Add to cart...
        add_to_cart_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[2]"
                             "/div[4]/form[1]/div[2]/div[1]/div[1]/div[2]/button[1]")
        add_to_cart = self.driver.find_element(By.XPATH, add_to_cart_xpath)
        navigator.move_to_element(add_to_cart)
        add_to_cart.click()
        sleep(3)

    def test_click_cart(self, navigator: ActionChains):
        # Get cart path and click using navigator
        cart_xpath = "/html[1]/body[1]/div[2]/header[1]/div[2]/div[1]/a[1]"
        cart = self.driver.find_element(By.XPATH, cart_xpath)
        navigator.move_to_element(cart)
        cart.click()
        sleep(1)

    def test_proceed_to_checkout(self, navigator: ActionChains):
        # Clicks 'Proceed to checkout'
        proceed_to_checkout_xpath = ("/html[1]/body[1]/div[2]/header[1]/div[2]/div[1]"
                                     "/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/button[1]")
        proceed_to_checkout = self.driver.find_element(By.XPATH, proceed_to_checkout_xpath)
        navigator.move_to_element(proceed_to_checkout)
        proceed_to_checkout.click()
        sleep(5)

    def test_assert_order_summary(self, navigator: ActionChains):
        # First expands the order summary
        order_summary_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[3]"
                               "/aside[1]/div[2]/div[1]/div[1]/div[1]/div[1]")
        order_summary = self.driver.find_element(By.XPATH, order_summary_xpath)
        navigator.move_to_element(order_summary)
        order_summary.click()
        sleep(3)

        # Grab the element with the dress in it
        item_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[2]/div[1]/div[3]/aside[1]/div[2]/div[1]/div[1]/div[1]"
                             "/div[1]/div[2]/div[1]/ol[1]/li[1]/div[1]/div[1]/div[1]/div[1]/strong[1]")
        item = self.driver.find_element(By.XPATH, item_xpath)

        # Assert item text
        assert "Autumn Pullie" in item.text

    def execute(self, method):
        print("Executing...")  # Debug print
        self.driver.get("https://magento.softwaretestingboard.com")
        self.driver.set_window_size(1936, 1048)
        sleep(1)

        # Instantiate our ActionChain
        navigator = ActionChains(self.driver)

        # Execute individual test cases in sequence
        self.test_navigate_to_category(navigator)  # Navigates to the category
        self.test_set_filters(navigator)  # Sets filters
        self.test_select_item(navigator)  # Selects the remaining item
        self.test_click_cart(navigator)  # Clicks the upper right cart icon
        self.test_proceed_to_checkout(navigator)  # Click the 'Proceed to Checkout' button
        self.test_assert_order_summary(navigator)  # Expands order summary and asserts contents


# MAIN
if __name__ == "__main__":
    # Instantiate tester
    test = ShoppingTest()

    test.setup(None)  # Setup
    test.execute(None)  # Execute all test cases
    test.teardown(None)  # Teardown

