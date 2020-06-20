import soupMaker
import estate

soup = ''

url = ''
maker = soupMaker.SoupMaker(url)

try:
    print('process start.')
    soup = maker.make()

except:
    print('request failed.')
    exit()

# get estates list
estates = []
for html in soup.find_all("div", {"class": ""}):
    estates.append(estate.Estate(html))

for estate in estates:
    print(estate.toString())
