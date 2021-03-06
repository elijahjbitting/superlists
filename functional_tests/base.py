import sys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

class FunctionalTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()
    
    def setUp(self):
            self.browser = webdriver.Firefox()
            self.browser.implicitly_wait(3)
    
    def tearDown(self):
            self.browser.quit()
            
    # helper 
    def check_for_row_in_list_table(self, row_text):
            todotable = self.browser.find_element_by_id('id_list_table')
            rows = todotable.find_elements_by_tag_name('tr')
            self.assertIn(row_text, [row.text for row in rows])
