from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def check_book_list(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_LIST), "There are books in the basket"

    def check_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket isn't empty"
