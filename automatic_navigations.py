import unittest
from selenium import webdriver
from api_data_mock import ApiDataMock
from selenium.webdriver.support.ui import Select # Modulo para poder seleccionar del dropdown
from time import sleep

class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://google.com/')

    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        #Borrar lo que hay en la barra de busqueda
        search_field.clear()
        
        search_field.send_keys('platzi')
        search_field.submit()
        #Para retorceder
        driver.back()
        #Se añaden pausas pero no son recomendadas
        sleep(1)
        #Para avanzar
        driver.forward()
        sleep(1)
        #Para refrescar
        driver.refresh()
        sleep(1)

       

    def tearDown(self):
        self.driver.implicitly_wait(5)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)