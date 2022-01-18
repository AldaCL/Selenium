import unittest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class RegisterNewUser(unittest.TestCase):
    
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service = s, options = options)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo.onestepcheckout.com/')
        
        
    def test_new_user(self):
        driver = self.driver
        driver.find_element(By.XPATH, '/html/body/div/div[2]/header/div/div[2]/div/a').click()
        driver.find_element(By.LINK_TEXT,'Log In').click()
        
        create_account_button = driver.find_element(By.XPATH,'/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        
        self.assertEqual('Create New Customer Account',driver.title)
        
        first_name = driver.find_element( By.ID ,"firstname")
        last_name = driver.find_element(By.ID, "lastname")
        email_address = driver.find_element(By.ID, "email_address")
        news_letter_subscription = driver.find_element(By.ID, "is_subscribed")
        
        password = driver.find_element(By.ID, "password")
        confirm_password = driver.find_element(By.ID, "confirmation")
        submit_button = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button")
        
       
        self.assertTrue(first_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled()
        )
        
        first_name.send_keys('Test')
        driver.implicitly_wait(1)
        last_name.send_keys('Test2')
        email_address.send_keys('test@gmailaa.com')
        password.send_keys('password123')
        confirm_password.send_keys('password123')
        submit_button.click()
    
        
    def tearDown(self):
        self.driver.quit()
    
if __name__ =='__main__':
    unittest.main(verbosity=2)