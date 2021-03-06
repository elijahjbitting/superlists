from .base import FunctionalTest 
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class NewVisitorTest(FunctionalTest):
    def test_can_start_a_test_and_retrieve_it_later(self):
            # Edith has heard about a cool new online to-do app. She goes
            # to check out it's homepage
            self.browser.get(self.server_url)

            # She notices that the page title and header mention to-do lists
            self.assertIn('To-Do', self.browser.title)
            header_text = self.browser.find_element_by_tag_name('h1').text
            self.assertIn('To-Do', header_text)

            # She is invited to enter a to-do item straight away
            inputbox = self.browser.find_element_by_id('id_new_item')
            self.assertEqual(
                    inputbox.get_attribute('placeholder'),
                    'Enter a to-do item'
            )
            


            # She types "Buy peacock feathers" into a text box (Edith's hobby is fly tying")
            newItemText1 = 'Buy peacock feathers'
            inputbox.send_keys(newItemText1)

            # When she hits enter she is taken to a new URL 
            # and now the page lists '1: Buy peacock feathers' as an item in a 
            # to-do list table
            
            import time     
            inputbox.send_keys(Keys.ENTER)
            time.sleep(3)
            edith_list_url = self.browser.current_url
            self.assertRegex(edith_list_url, '/lists/.+')
            expectedRowText1 = '1: ' + newItemText1
            time.sleep(1)
            self.check_for_row_in_list_table(expectedRowText1)

            # There is still a textbox inviting her to add another item. She 
            # enters "Use peacock feathers to make a fly" (Edith is very methodical)
            inputbox = self.browser.find_element_by_id('id_new_item')
            newItemText2 = 'Use peacock feathers to make a fly'
            inputbox.send_keys(newItemText2)
            expectedRowText2 = '2: ' + newItemText2
            inputbox.send_keys(Keys.ENTER)

            # The page updates again, and now shows both items on her list
            time.sleep(1)
            self.check_for_row_in_list_table(expectedRowText1)
            self.check_for_row_in_list_table(expectedRowText2)

            # Now a new User, Francis, comes along to the site

            ## We use a new browser session to ensure no information 
            ## of Eidth's is coming through from cookies etc.

            self.browser.quit()
            self.browser = webdriver.Firefox()
            
            # Francis visits the home page. There is no sign of Edith's 
            # list
            self.browser.get(self.server_url)
            page_text = self.browser.find_element_by_tag_name('body').text
            self.assertNotIn(newItemText1, page_text)
            self.assertNotIn('make a fly', page_text)
            
            # Francis starts a new list by enterinf a new item. He
            # is less interesting than Edith
            inputbox = self.browser.find_element_by_id('id_new_item')
            FrancisItemText1 = 'Buy milk'
            inputbox.send_keys(FrancisItemText1)
            inputbox.send_keys(Keys.ENTER)

            time.sleep(3)
            # Francis gets his own unique URL
            francis_list_url = self.browser.current_url
            self.assertRegex(francis_list_url, '/lists.+')
            self.assertNotEqual(francis_list_url, edith_list_url)

            # Again there is no trace of Edith's list
            page_text = self.browser.find_element_by_tag_name('body').text
            self.assertNotIn(newItemText1, page_text)
            self.assertNotIn('make a fly', page_text)
            
            # Satisfied, they both go back to sleep
