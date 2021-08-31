from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from time import sleep


class DemoDropDownMultiSelect():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def demo_dropdown(self):
        self.driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')
        sleep(2)
        dropdown = self.driver.find_element_by_id('multi-select')
        ddmulti = Select(dropdown)
        ddmulti.select_by_index(0)
        sleep(2)
        ddmulti.select_by_visible_text('Florida')
        sleep(2)
        ddmulti.select_by_value('New Jersey')
        sleep(2)
        ddmulti.deselect_all()
        self.driver.quit()

ddm = DemoDropDownMultiSelect()
ddm.demo_dropdown()
