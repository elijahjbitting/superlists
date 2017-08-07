from .base import FunctionalTest
from unittest import skip
from selenium.webdriver.common.keys import Keys     

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        import time
        # Edith goes to the home page and accidentally tries to submit
        self.browser.get(self.server_url)

        # an empty list item. She hits Enter on the empty input box
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        # The home page refreshes, and there is an error message saying        
        # that list items cannot be blank
        page_text = self.browser.find_element_by_tag_name('body').text
        
        # She tries again with some text for the item, which now works

        # Perversely she now decides to to submit a second blank list item

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')