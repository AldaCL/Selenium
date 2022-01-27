import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavigationTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service = s, options = options)
        driver = self.driver
        driver.get('https://demo-store.seleniumacademy.com/')
        driver.maximize_window
        driver.implicitly_wait(10)
        
    def test_account_link(self):
        WebDriverWait(self.driver, 10).until(lambda ss : ss.find_element(By.ID,'select-language').get_attribute('length')=='3')
        
        account = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'ACCOUNT')))
        account.click()
    
    def test_create_account_new_costumer(self):
        self.driver.find_element(By.LINK_TEXT,'ACCOUNT').click()
        
        my_account = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'My Account')))
        my_account.click()
        
        create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT,'CREATE AN ACCOUNT')))
        create_account_button.click()
        
        WebDriverWait(self.driver,10).until(EC.title_contains('Create New Customer Account'))
    
    def tearDown(self):
        self.driver.quit()
    
    
if __name__ == '__main__':
	unittest.main(verbosity = 2)


    
    
    
        