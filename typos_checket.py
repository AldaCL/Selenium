from pickle import FALSE
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class NavigationTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service = s, options = options)
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/typos')
        driver.maximize_window
        driver.implicitly_wait(10)
        
    def test_Typos(self):
        driver = self.driver
        paragraph_to_check = driver.find_element(By.CSS_SELECTOR,'#content > div > p:nth-child(3)')
        
        text_to_check = paragraph_to_check.text
        print(text_to_check)
        
        tries = 1
        found = FALSE
        
        correct_text = "Sometimes you'll see a typo, other times you won't."
        
        while text_to_check != correct_text:  
            
            paragraph_to_check = driver.find_element(By.CSS_SELECTOR,'#content > div > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            tries +=1  
            driver.refresh()
            
            
            
        while not found :
            if text_to_check == correct_text:   
                driver.refresh()
                found = True
            self.assertEqual(found,True)
        
        print(f"it took {tries} tries to find the typo")
        
       
       
       
    def tearDown(self):
        self.driver.quit()
    
    
if __name__ == '__main__':
	unittest.main(verbosity = 2)