from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class DemoFindElements:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def enable_or_disable(self):
        self.driver.get('https://www.yatra.com/')
        sleep(2)
        self.driver.maximize_window()
        texto = self.driver.find_element_by_xpath("//h2[normalize-space()='Countries Open for Travel']").is_enabled()
        print(texto)
        self.driver.close()


estado = DemoFindElements()
estado.enable_or_disable()
