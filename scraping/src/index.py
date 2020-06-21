from soupMaker import SoupMaker
from estate import Estate

soup = ''

url = ''
maker = SoupMaker(url)

try:
    print('process start.')
    soup = maker.make()

except:
    print('request failed.')
    exit()

# get estates list
estates = []
for html in soup.find_all("div", {"class": ""}):
    estates.append(Estate(html))

for estate in estates:
    print(estate.toString())
