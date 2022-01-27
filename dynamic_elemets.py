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
        driver.get('http://the-internet.herokuapp.com/disappearing_elements')
        driver.maximize_window
        driver.implicitly_wait(10)
        
    def test_name_elements(self):
        driver = self.driver
        
        options = []
        menu = 5
        tries = 1
        
        while len(options)<5 :
            options.clear()
            
            for i in range(menu):
                try:
                    option_name = driver.find_element(By.XPATH,f'/html/body/div[2]/div/div/ul/li[{i+1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option number {i+1} is NOT FOUND")
                    tries += 1
                    driver.refresh()
                    
        print(f"Finished in {tries} tries")
                    
                    
        
    def tearDown(self):
        self.driver.quit()
    
    
if __name__ == '__main__':
	unittest.main(verbosity = 2)