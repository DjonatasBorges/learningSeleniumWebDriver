from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class DemoRadio:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def demo_radio_button(self):
        self.driver.get('https://www.sugarcrm.com/es/request-demo/')
        sleep(2)
        self.driver.maximize_window()
        radio_01Element = 'doi0'
        radio_02Element = 'doi1'
        radio_01 = self.driver.find_element_by_id(radio_01Element)
        radio_02 = self.driver.find_element_by_id(radio_02Element)
        self.driver.find_element_by_id(radio_01Element).click()
        print(radio_01.is_selected())
        print(radio_02.is_selected())
        if not radio_02.is_selected():
            radio_02.click()

        print(radio_01.is_selected())
        print(radio_02.is_selected())
        self.driver.close()


radio = DemoRadio()
radio.demo_radio_button()
'''Caixas de tipo radio, quando vc seleciona uma, as outras ficam não estarão. uma depende da outra para existir'''