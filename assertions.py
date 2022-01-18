import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from pyunitreport import HTMLTestRunner

from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common import service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service = s, options=options)
        driver = self.driver
        driver.get('http://demo.onestepcheckout.com/')
        driver.maximize_window
        driver.implicitly_wait(10)
                
        
    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))
        
    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))
        
    def tearDown(self):
        self.driver.quit()

    #funcion de utilidad para aser cuando un elemento esta presente de acuerdo a sus parametros
    #how : tipo de selector
    #what : valor del selector 

    def is_element_present(self,how, what):
        try :
            self.driver.find_element(by = how, value = what )
        except NoSuchElementException as variable: 
            return False
        return True