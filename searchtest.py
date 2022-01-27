from re import search
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class SearchTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        s = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service = s, options=options)
        driver = self.driver
        driver.get('http://demo.onestepcheckout.com/')
        driver.maximize_window
        driver.implicitly_wait(10)


    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, "q")
        
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()
        
    def test_search_saltshaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, "q")
        search_field.send_keys('salt shaker')
        search_field.submit()
        a =driver.find_element_by_id('a')
        self.assertTrue(a.is)
        
        products = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/a/img')
        
        self.assertEqual(1,len(products))

    # def test_search_element_field(self):
    #     search_field = self.driver.find_element(By.ID, "shopify-section-footer")

    # def test_search_text_field_class_field(self):
    #     search_field = self.driver.find_element(By.CLASS_NAME, "large")

    # def test_search_text_field_by_name(self):
    #     search_field = self.driver.find_element(By.NAME, "q")

    # def test_search_button_enabled(self):
    #     button = self.driver.find_element(By.CLASS_NAME, "button")

    # def test_count_of_promo_images(self):
    #     banner_list = self.driver.find_element(By.CLASS_NAME,"promos")
    #     banners = banner_list.find_elements(By.TAG_NAME , "img")
    #     self.assertEqual(3,len(banners))


    # def test_vip_promo(self):
    #     vip_promo = self.driver.find_element(By.XPATH,'//*[@id="header"]/div/a/img[1]')

    # def test_shoping_cart(self):
    #     shoping_cart_icon = self.driver.find_element(By.CSS_SELECTOR, 'div.header-minicart span.icon')



    # def tearDown(self):
    #     self.driver.quit()


if __name__ == '__main__':
	unittest.main(verbosity = 2)

