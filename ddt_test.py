import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

import csv
from ddt import ddt, data, unpack


@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service = s, options = options)
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        # driver.find_element(By.LINK_TEXT,"Sortable Data Tables")
    
    @data(('dress',6),('music',5))
    @unpack
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver
        
        search_field = driver.find_element(By.NAME,'q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()
        
        products = driver.find_elements(By.XPATH,'//h2[@class ="product-name"]/a')
        print(f'Found {len(products)} products')
            
        for product in products:
            print(product.text)
            
        self.assertEqual(expected_count,len(products))
            
            
    def tearDown(self):
        self.driver.quit()
    
    
if __name__ == '__main__':
	unittest.main(verbosity = 2)


    
    
    
        