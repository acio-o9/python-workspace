from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import re
import time


class SoupMaker:
    """BeautifulSoup Maker

    Attributes:
        browser:
        url:
        pageSize: int
    """

    browser = ''
    url = ''

    PAGE_PER_ESTATE = 20

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

        pageSize = self.__getPageSize(soup)

        time.sleep(1)
        return soup, pageSize

    def __getPageSize(self, soup):

        pageString = soup.find(
                "div",
                {"class": ""}).text
        matchObject = re.search(r'[1-9][0-9]+', pageString)
        total = int(matchObject.group())

        pageSize, mod = divmod(total, self.PAGE_PER_ESTATE)

        if mod > 0:
            pageSize += 1

        return pageSize

    def findEstateTags(self, soup):
        return soup.find_all(
                "div",
                {"class": ""})
