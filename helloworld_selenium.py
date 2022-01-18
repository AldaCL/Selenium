import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver


class HelloWorld(unittest.TestCase):

	@classmethod
	def setUp(cls):
		cls.driver = webdriver.Chrome(executable_path = r'./chromedriver')
		driver = cls.driver
		driver.implicitly_wait(10)


	def test_hello_wolrd(self):
		driver = self.driver
		driver.get('https://www.platzi.com')

	def test_visit_wikipedia(self):
		driver = self.driver
		driver.get('https://www.wikipedia.com')

	@classmethod
	def tearDown(cls):
		cls.driver.quit()
		# return super().tearDown()

if __name__ == '__main__':
	unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))

