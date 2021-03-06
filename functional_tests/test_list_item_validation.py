from .base import FunctionalTest
from unittest import skip
from selenium.webdriver.common.keys import Keys     

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        import time
        # Edith goes to the home page and accidentally tries to submit
        self.browser.get(self.server_url)

        # an empty list item. She hits Enter on the empty input box
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        time.sleep(3)

        # The home page refreshes, and there is an error message saying        
        # that list items cannot be blank
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again with some text for the item, which now works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy Milk\n')
        self.check_for_row_in_list_table('1: Buy Milk')

        # Perversely she now decides to to submit a second blank list item
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        time.sleep(3)
        
        # She receives a similar warning on the list page
        self.check_for_row_in_list_table('1: Buy Milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # And she can correct it by filling some text in
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1: Buy Milk')
        self.check_for_row_in_list_table('2: Make tea')

