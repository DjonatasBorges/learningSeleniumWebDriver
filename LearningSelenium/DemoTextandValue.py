from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class DemoFindElements:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def text_test_demo(self):
        self.driver.get('https://www.yatra.com/')
        sleep(2)
        self.driver.maximize_window()
        texto = self.driver.find_element_by_xpath("//h2[normalize-space()='Countries Open for Travel']").text
        print(texto)
        try:
            assert texto in self.driver.find_element_by_xpath("//h2[normalize-space()='Countries Open for Travel']").text
            print(f'Texto esta validado!')
            self.driver.close()
        except:
            self.driver.close()

    def value_test_demo(self):
        self.driver.get('https://www.yatra.com/')
        sleep(2)
        self.driver.maximize_window()
        value = self.driver.find_element_by_xpath("//div[@id='credit-shellBtnID']//input[@id='BE_flight_flsearch_btn']").get_attribute('value')
        print(value)
        try:
            assert value in self.driver.find_element_by_xpath("//div[@id='credit-shellBtnID']//input[@id='BE_flight_flsearch_btn']").get_attribute('value')
            print(f'Valor esta validado!')
            self.driver.close()
        except:
            self.driver.close()



'''texto = DemoFindElements()
texto.text_test_demo()'''
valor = DemoFindElements()
valor.value_test_demo()
