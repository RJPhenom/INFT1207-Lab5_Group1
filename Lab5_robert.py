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
    def setup(self):
        print("Setting up...")  # Debug print
        self.driver = webdriver.Firefox()

    def teardown(self):
        print("Tearing down...")  # Debug print
        self.driver.quit()

    def execute(self):
        print("Executing...")  # Debug print
        self.driver.get("https://magento.softwaretestingboard.com")
        self.driver.set_window_size(1936, 1048)

        # Instantiate our ActionChain
        navigate = ActionChains(self.driver)

        # TEST STEPS
        # 1. NAVIGATING TO THE SECTION
        # --------------------------------------------------------------------------------------------------------------
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
        navigate.move_to_element(top_menu).perform()
        navigate.move_to_element(sub_menu).perform()
        navigate.move_to_element(offset).perform()
        navigate.move_to_element(target).perform()

        # Click the link
        target.click()

        # 2. SETTING OUR FILTERS
        # --------------------------------------------------------------------------------------------------------------
        # Select the appropriate Style, Size, Price Range, Color and Material. For e.g.:
        # Style: Pullover, Size: M, Price: $50.00 - $59.99, Color: Purple, Material: Polyester

        # 2a --STYLE--
        # --------------------------------------------------------------------------------------------------------------
        style_xpath = "/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]"
        pullover_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]/div[1]"
                          "/div[2]/div[1]/div[1]/div[2]/ol[1]/li[3]/a[1]")

        style = self.driver.find_element(By.XPATH, style_xpath)
        pullover = self.driver.find_element(By.XPATH, pullover_xpath)

        navigate.move_to_element(style).perform()
        style.click()

        navigate.move_to_element(pullover).perform()
        pullover.click()
        sleep(1)

        # 2b --SIZE--
        # --------------------------------------------------------------------------------------------------------------
        size_xpath = "/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]"
        m_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]/div[1]"
                   "/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/a[3]/div[1]")

        size = self.driver.find_element(By.XPATH, size_xpath)
        m = self.driver.find_element(By.XPATH, m_xpath)

        navigate.move_to_element(size).perform()
        size.click()

        navigate.move_to_element(m).perform()
        m.click()
        sleep(1)

        # 2c --PRICE--
        # --------------------------------------------------------------------------------------------------------------
        price_xpath = "/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div[1]"
        fifty_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]"
                       "/div[1]/div[2]/div[3]/div[1]/div[2]/ol[1]/li[3]/a[1]")

        price = self.driver.find_element(By.XPATH, price_xpath)
        fifty = self.driver.find_element(By.XPATH, fifty_xpath)

        navigate.move_to_element(price).perform()
        price.click()

        navigate.move_to_element(fifty).perform()
        fifty.click()
        sleep(1)

        # 2d --COLOUR--
        # --------------------------------------------------------------------------------------------------------------
        color_xpath = "/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div[1]"
        purple_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]"
                        "/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/a[4]/div[1]")

        color = self.driver.find_element(By.XPATH, color_xpath)
        purple = self.driver.find_element(By.XPATH, purple_xpath)

        navigate.move_to_element(color).perform()
        color.click()

        navigate.move_to_element(purple).perform()
        purple.click()
        sleep(1)

        # 2e --MATERIAL--
        # --------------------------------------------------------------------------------------------------------------
        material_xpath = "/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]/div[1]/div[2]/div[3]/div[1]"
        polyester_xpath = ("/html[1]/body[1]/div[2]/main[1]/div[3]/div[2]"
                           "/div[1]/div[2]/div[3]/div[1]/div[2]/ol[1]/li[3]/a[1]")

        material = self.driver.find_element(By.XPATH, material_xpath)
        polyester = self.driver.find_element(By.XPATH, polyester_xpath)

        navigate.move_to_element(material).perform()
        material.click()

        navigate.move_to_element(polyester).perform()
        polyester.click()
        sleep(1)

        # 3.	Select any single dress (if there are multiple depending upon your selection) and click on Add to cart

        # 5.	Click the “cart icon”.

        # 6.	Click on the “Proceed to Checkout” Button.

        # 7.	Assert the “Ordersummary”. Your shopping cart should show the dress selected by you.


# PROGRAM
# main
if __name__ == "__main__":
    # Instantiate tester
    test = ShoppingTest()

    # Setup
    test.setup()

    # Test Execution
    test.execute()

    # Teardown
    test.teardown()

