from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class DemoFindElement:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def locate_by_id_demo(self):
        self.driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        sleep(2)
        self.driver.maximize_window()
        self.driver.find_element_by_id('login-input').send_keys('test@test.com')
        sleep(2)
        self.driver.close()

    def locate_by_name_demo(self):
        self.driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        sleep(2)
        self.driver.maximize_window()
        self.driver.find_element_by_name('login-input').send_keys('test@test.com')
        sleep(2)
        self.driver.close()

    def locate_by_xpath_demo(self):
        self.driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        sleep(2)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="login-input"]').send_keys('test@test.com')
        sleep(2)
        self.driver.close()

    def locate_by_css_selector_demo(self):
        self.driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        sleep(2)
        self.driver.maximize_window()
        self.driver.find_element_by_css_selector('#login-input').send_keys('test@test.com')
        sleep(2)
        self.driver.close()

    def locate_by_link_test_demo(self):
        self.driver.get('https://www.yatra.com/')
        sleep(2)
        self.driver.maximize_window()
        self.driver.find_element_by_link_text('Yatra for Business').click()
        sleep(2)
        self.driver.close()


    def locate_by_partials_link_test_demo(self):
        self.driver.get('https://www.yatra.com/')
        sleep(2)
        self.driver.maximize_window()
        self.driver.find_element_by_partial_link_text('tra for Business').click()
        sleep(2)
        self.driver.close()

    def locate_by_tag_name_demo(self):
        self.driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        sleep(2)
        self.driver.maximize_window()
        self.driver.find_element_by_tag_name('input').send_keys('teste@teste.com.br')
        sleep(2)
        self.driver.close()

    def locate_by_class_name_demo(self):
        self.driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        sleep(2)
        self.driver.maximize_window()
        self.driver.find_element_by_class_name('yt-sme-mobile-input').send_keys('teste@teste.com.br')
        sleep(2)
        self.driver.close()



find_by = DemoFindElement()
#find_by.locate_by_css_selector_demo()
#find_by.locate_by_link_test_demo()
find_by.locate_by_class_name_demo()
