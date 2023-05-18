from .pages.product_page import ProductPage
#import pytest - switch on when parameterizing

#@pytest.mark.parametrize('promo_offer', ["0","1","2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_button()
    product_page.press_button()
    product_page.check_name_of_book()
    product_page.test_guest_cant_see_success_message_after_adding_product_to_basket()
    #product_page.test_guest_cant_see_success_message() - disable "Add to cart" button click feature
    product_page.test_message_disappeared_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

