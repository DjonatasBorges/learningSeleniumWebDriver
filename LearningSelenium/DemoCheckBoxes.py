from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class DemoCheckBoxes:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def demo_check_box(self):
        self.driver.get('https://www.sugarcrm.com/es/request-demo/')
        sleep(2)
        self.driver.maximize_window()
        checkbox_1 = self.driver.find_element_by_id('interest_market_c0').is_selected()
        print(checkbox_1)
        if not checkbox_1:
            self.driver.find_element_by_id('interest_market_c0').click()
            checkbox_1 = self.driver.find_element_by_id('interest_market_c0').is_selected()
        print(checkbox_1)
        self.driver.close()


checkbox = DemoCheckBoxes()
checkbox.demo_check_box()
'''Caixas de seleção checkbox, podem sr selecionadas várias em uma página, sendo elas independentes.'''
