from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank
        self.wait_for(lambda:  self.browser.find_element_by_css_selector('#id_text:invalid')
        )

        # She tries again with some text for the item, which now works
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Buy milk")
        self.wait_for(lambda:  self.browser.find_element_by_css_selector('#id_text:valid')
        )

        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy milk')
        # Perversely, she now decides to submit a second blank list item
        # She receives a similar warning on the list page
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for(lambda:  self.browser.find_element_by_css_selector('#id_text:invalid')
        )

        # And she can correct it by filling some text in
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Buy tea")
        self.wait_for(lambda:  self.browser.find_element_by_css_selector('#id_text:valid')
        )
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Buy tea')

    def test_cannot_add_duplicate_items(self):
        # Edith goes to the home page and starts a new list
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys("Buy milk")
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # She accidentally tries to enter a duplicate item
        self.get_item_input_box().send_keys("Buy milk")
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You've already got this in your list"
        ))


