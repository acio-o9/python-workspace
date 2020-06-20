class Estate:

    price = ''
    roomType = ''
    buildAt = ''
    estateSize = ''
    groundSize = ''

    def __init__(self, html):
        self.price = html.find("li", {"class": ""}).text

        data = html.find_all("span", {"class": ""})
        self.roomType = data[0].text
        self.buildAt = data[1].text
        self.estateSize = data[2].text
        self.groundSize = data[3].text

    def toString(self):
        return ",".join([
            self.price,
            self.roomType,
            self.buildAt,
            self.estateSize,
            self.groundSize
        ])
