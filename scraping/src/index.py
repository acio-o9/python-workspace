from soupMaker import SoupMaker
from estate import Estate
import sys

soup = ''
pageSize = 0

url = ''
maker = SoupMaker(url)

try:
    print('process start.')
    soup, pageSize = maker.make()

except:
    maker.quit()
    print('request failed.', sys.exc_info()[0])
    exit()

# get estates list
estates = []
for html in maker.findEstateTags(soup):
    estates.append(Estate(html))

# search more page estates
for page in range(2, pageSize + 1):
    print('processing on page:', page)
    maker.url = url + '?page=' + str(page)
    soup, _ = maker.make()
    for html in maker.findEstateTags(soup):
        estates.append(Estate(html))

maker.quit()

for estate in estates:
    print(estate.toString())
