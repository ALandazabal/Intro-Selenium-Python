import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select # Modulo para poder seleccionar del dropdown
from time import sleep
from selenium.webdriver.common.by import By #Hacer referencia a un elemento del sitio web, para interactuar
from selenium.webdriver.support.ui import WebDriverWait # Modulo para  manejo de esperas explicitas
from selenium.webdriver.support import expected_conditions as EC #esperas explicitas




class TestingMercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.mercadolibre.com') # adiconar la pagina


    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element_by_id('CO')
        country.click()
        sleep(2)
        search_field = driver.find_element_by_name('as_word')
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(2)
        
        location = driver.find_element_by_xpath('/html/body/main/div/div/aside/section[2]/dl[8]/dd[1]/a/span[1]')
        driver.execute_script("arguments[0].click();", location)
        # location.click()
        sleep(2)
        condition = driver.find_element_by_partial_link_text('Nuevo')
        driver.execute_script("arguments[0].click();", condition)
        # condition.click()
        sleep(2)
        order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
        order_menu.click()
        higher_price = driver.find_element_by_css_selector('li.andes-list__item:nth-child(3) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)')
        higher_price.click()
        sleep(2)

        articles = []
        prices = []

        for i in range(5):
            article_name = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            price_article = driver.find_element_by_xpath(f'/html/body/main/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div/div/span[1]/span[2]').text
            articles.append(article_name)
            prices.append(price_article)
        
        print(articles,prices)

        

    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)