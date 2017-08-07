from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
            # Edith goes to the homepage
            self.browser.get(self.server_url)
            self.browser.set_window_size(1024, 768)
            # she notices that the input box is nicely centered 
            inputbox = self.browser.find_element_by_id('id_new_item')
            inputBoxXLoc = 0
            if inputbox.location['x']:
                inputBoxXLoc = inputbox.location['x']
            inputBoxWidth = 0
            if inputbox.size['width']:
                    inputBoxWidth = inputbox.size['width']
            self.assertAlmostEqual(inputBoxXLoc + inputBoxWidth / 2, 512,delta=5)
            # she starts a new list and sees the input is nicely 
            # centered there too
            inputbox.send_keys('testing')
            inputbox.send_keys(Keys.ENTER)
            import time     
            time.sleep(3)
            inputbox = self.browser.find_element_by_id('id_new_item')
            inputBoxXLoc = 0
            if inputbox.location['x']:
                inputBoxXLoc = inputbox.location['x']
            inputBoxWidth = 0
            if inputbox.size['width']:
                inputBoxWidth = inputbox.size['width']
            self.assertAlmostEqual(inputBoxXLoc + inputBoxWidth / 2, 512,delta=5)
