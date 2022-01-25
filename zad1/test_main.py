import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class MyTestCase(unittest.TestCase):
    def test_title(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(10)
        driver.get("https://duckduckgo.com/")
        driver.find_element(By.ID, "search_form_input_homepage").send_keys("Selenium")
        driver.find_element(By.ID, "search_button_homepage").submit()
        self.assertEqual(driver.title, "Selenium at DuckDuckGo")
        driver.quit()


if __name__ == '__main__':
    unittest.main()
