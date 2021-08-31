from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class DemoScreenCapture():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())


    def demo_screen_capture(self):
        self.driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        sleep(2)
        self.driver.maximize_window()
        login = self.driver.find_element_by_id("login-continue-btn")
        login.click()
        self.driver.get_screenshot_as_file('.//foto.jpg')
        self.driver.close()


foto = DemoScreenCapture()
foto.demo_screen_capture()