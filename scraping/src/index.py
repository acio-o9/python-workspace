from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

import estate

soup = ''

try:
    browser = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)

    print('process start.')

    url = ''
    browser.get(url)

    WebDriverWait(browser, 15).until(EC.presence_of_all_elements_located)

    html = browser.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")

    browser.close()
    browser.quit()

except:
    browser.close()
    browser.quit()

# get estates list
estates = []
for html in soup.find_all("div", {"class": ""}):
    estates.append(estate.Estate(html))

for estate in estates:
    print(estate.toString())
