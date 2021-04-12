import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = r"./chromedriver.exe")
        driver = cls.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        driver = self.driver
        search_field = self.driver.find_element_by_id("search")

    def test_search_text_field_by_name(self):
        driver = self.driver
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_class_name(self):
        driver = self.driver
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button_enabled(self):
        driver = self.driver
        search_field = self.driver.find_element_by_class_name("button")

    def test_count_of_promo_banner_images(self):
        driver = self.driver
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name("img")
        self.assertEqual(3, len(banners))

    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath("//*[@id='top']/body/div[2]/div[2]/div[2]/div/div/div[2]/div/ul/li[3]/a/img")

    def test_shopping_car(self):
        shopping_car_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)