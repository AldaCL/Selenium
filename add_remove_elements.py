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
        driver.get('http://the-internet.herokuapp.com/add_remove_elements/')
        driver.maximize_window
        driver.implicitly_wait(10)
        
    def test_account_link(self):
        pass
        driver = self.driver
        
        elements_added = int(input('How many elements will toy add? : '))
        elements_removed = int(input('How many elements will you remove? :'))
        
        total_elements = elements_added - elements_removed
    
        add_button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/button')
        
        sleep(3)
        
        for i in range (elements_added):
            add_button.click()
            
        sleep(3)           
            
        for i in range (elements_removed):
            try:
                delete_button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/button')
                delete_button.click()
            except:
                print("You're trying to delete more elements than existent")
                break
            
        if total_elements>0:
            print(f"There are {total_elements}  elements on screen")
        else:
            print("There are 0 elements on screen")
                
        
        
        
        
    def tearDown(self):
        self.driver.quit()
    
    
if __name__ == '__main__':
	unittest.main(verbosity = 2)


    
    
    
        