import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Tables(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        
        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service = s, options = options)
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/tables')
        # driver.find_element(By.LINK_TEXT,"Sortable Data Tables")
        
        
    def test_sort_table(self):
        driver = self.driver
        
        table_data = [[] for i in range(5)]
        print (table_data)
        
        for i in range (5):
            header = driver.find_element(By.XPATH,f'//*[@id="table1"]/thead/tr/th[{i+1}]')
            table_data[i].append(header.text)
            
            for j in range(4):
                row_data = driver.find_element(By.XPATH,f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]')
                table_data[i].append(row_data.text)
                
        print(table_data)
        
        
            
    def tearDown(self):
        self.driver.quit()
    
    
if __name__ == '__main__':
	unittest.main(verbosity = 2)


    
    
    
        