from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class DemoHiddenElement:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def demo_is_displayed(self):
        self.driver.get('https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp')
        sleep(2)
        self.driver.maximize_window()
        display_1 = self.driver.find_element_by_xpath("//div[@id='myDIV']").is_displayed()
        print(display_1)
        self.driver.find_element_by_xpath("//button[normalize-space()='Toggle Hide and Show']").click()
        display2 = self.driver.find_element_by_xpath("//div[@id='myDIV']").is_displayed()
        print(display2)
        self.driver.close()

display = DemoHiddenElement()
display.demo_is_displayed()