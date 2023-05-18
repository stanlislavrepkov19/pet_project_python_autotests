from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_be_button(self):
        assert self.is_element_present(*ProductPageLocators.SUBMIT_BUTTON), "Button is not presented"

    def press_button(self):
        button = self.browser.find_element(*ProductPageLocators.SUBMIT_BUTTON)
        time.sleep(5)
        button.click()

    def check_name_of_book(self):
        bookname = self.browser.find_element(*ProductPageLocators.NAME_BOOK).text
        bookprice = self.browser.find_element(*ProductPageLocators.PRICE_OF_BOOK).text
        bookbsk = self.browser.find_element(*ProductPageLocators.BOOK_IN_BASKET).text
        bskprice = self.browser.find_element(*ProductPageLocators.PRICE_OF_BASKET).text

        assert (bookname == bookbsk), "Invalid book name"
        time.sleep(5)
        assert (bookprice == bskprice), "Incorrect price"
        time.sleep(5)

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_guest_cant_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def test_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
