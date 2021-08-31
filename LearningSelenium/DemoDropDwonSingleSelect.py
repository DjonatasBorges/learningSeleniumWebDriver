from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from time import sleep


class DemoDropDwonSingleSelect():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def demo_dropdown(self):
        self.driver.get('https://www.salesforce.com/au/form/demo/overview-demo/?d=7010M000001yJbq')
        sleep(2)
        self.driver.find_element_by_id('onetrust-accept-btn-handler').click()
        sleep(2)
        dropdown = self.driver.find_element_by_name('CompanyEmployees')
        dd = Select(dropdown)
        dd.select_by_index(0)
        sleep(2)
        dd.select_by_visible_text('16 - 100 employees')
        sleep(2)
        dd.select_by_value('250')
        sleep(2)
        self.driver.quit()


dd = DemoDropDwonSingleSelect()
dd.demo_dropdown()