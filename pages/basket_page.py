from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_not_be_item_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.ITEM_IN_BASKET), \
           "Item in basket is presented, but should not be"

    def should_be_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.BASKET_IS_EMPTY_MESSAGE)

    def should_be_basket_is_empty_message(self):
        assert "Your basket is empty. Continue shopping" \
               == self.browser.find_element(*BasePageLocators.BASKET_IS_EMPTY_MESSAGE).text, "Message is not present"
