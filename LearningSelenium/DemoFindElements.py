from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class DemoFindElements:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def locate_by_tags_name(self):
        self.driver.get('https://www.yatra.com/')
        self.driver.maximize_window()
        sleep(2)
        lista = self.driver.find_elements_by_tag_name('a')
        for i in lista:
            if len(i.text) > 0:
                print(i.text)
        self.driver.close()

    def locate_by_tags_name_2(self):
        self.driver.get('https://www.yatra.com/')
        self.driver.maximize_window()
        sleep(2)
        lista = self.driver.find_elements(By.TAG_NAME, 'a')
        for i in lista:
            if len(i.text) > 0:
                print(i.text)
        self.driver.close()


teste = DemoFindElements()
teste.locate_by_tags_name_2()
