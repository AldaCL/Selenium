import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

from google_page import GooglePage

class GoogleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        s = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service = s, options = options)
        
    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')
        
        self.assertEqual('Platzi',google.keyword)
            
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
    
    
if __name__ == '__main__':
	unittest.main(verbosity = 2)


    
    
    
        