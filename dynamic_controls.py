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
        driver.get('http://the-internet.herokuapp.com/dynamic_controls')
        driver.maximize_window
        driver.implicitly_wait(10)
        
    def test_dynamic_controls(self):
        driver = self.driver
        
        checkbox = driver.find_element(By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')
        checkbox.click()
        
        remove_add_button = driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button')
        remove_add_button.click()
        
        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#checkbox-example > button')))
        remove_add_button.click()
        
        enable_disable_button = driver.find_element(By.CSS_SELECTOR,'#input-example > button')
        enable_disable_button.click()
        
        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#input-example > button')))
        
        text_area = driver.find_element(By.CSS_SELECTOR,'#input-example > input[type=text]')
        text_area.send_keys('Quiubo')
        
        enable_disable_button.click()
    def tearDown(self):
        self.driver.quit()
    
    
if __name__ == '__main__':
	unittest.main(verbosity = 2)