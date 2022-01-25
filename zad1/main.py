import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    def test_title(self):
        driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
        driver.implicitly_wait(10)
        driver.get("https://duckduckgo.com/")
        driver.find_element(By.ID, "search_form_input_homepage").send_keys("Selenium")
        driver.find_element(By.ID, "search_button_homepage").submit()
        self.assertEqual(driver.title, "Selenium at DuckDuckGo")
        driver.quit()


if __name__ == '__main__':
    unittest.main()
