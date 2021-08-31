from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class AutoSuggest():
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def auto_suggest(self):
        self.driver.get('https://www.yatra.com')
        sleep(2)
        self.driver.maximize_window()
        depart_from = self.driver.find_element(By.XPATH, '//*[@id="BE_flight_origin_city"]')
        depart_from.click()
        depart_from.send_keys('New Delhi')
        depart_from.send_keys(Keys.ENTER)
        going_to = self.driver.find_element(By.XPATH, '//*[@id="BE_flight_arrival_city"]')
        going_to.click()
        sleep(2)
        going_to.send_keys('New')
        search_results = self.driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(search_results))
        lista = []
        for results in search_results:
            print(results.text)
            lista.append(results.text)
            if 'New York (JFK)' in results.text:
                results.click()
                break
        print(lista)

        self.driver.find_element(By.XPATH, '//*[@id="BE_flight_flsearch_btn"]').click()
        agenda = "//input[@id='BE_flight_origin_date']"
        dia = '//*[@id="25/12/2021"]'
        self.driver.find_elements(By.XPATH, agenda)
        sleep(2)
        self.driver.find_element(By.XPATH, dia).click()
        sleep(2)

        self.driver.quit()


sugest = AutoSuggest()
sugest.auto_suggest()