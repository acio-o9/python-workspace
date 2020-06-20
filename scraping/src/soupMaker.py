from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


class SoupMaker:

    browser = ''
    url = ''

    def __init__(self, url):
        self.browser = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        self.url = url

    def make(self):
        soup = ''
        try:
            self.browser.get(self.url)
            WebDriverWait(self.browser, 15).until(EC.presence_of_all_elements_located)
            html = self.browser.page_source.encode('utf-8')
            soup = BeautifulSoup(html, "html.parser")

            self.browser.close()
            self.browser.quit()
        except:
            self.browser.close()
            self.browser.quit()

        return soup
