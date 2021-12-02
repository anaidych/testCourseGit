from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_added_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Message is not present"

    def should_check_added_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text, "Product name is not the same"

    def should_check_added_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in \
               self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text, "Price name is not the same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_wait_until_element_disappears(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should disappear"
