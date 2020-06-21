class Estate:
    """Estate

    Attributes:
        tag: bs4.element.Tag
        price: int
        roomType: string
        buildAt: date
        estateSize: float
        groundSize: float
    """
    __price = ''
    __roomType = ''
    __buildAt = ''
    __estateSize = ''
    __groundSize = ''

    def __init__(self, tag):
        """constructor

        Args:
            tag (bs4:element.Tag): model tag
        """
        self.__setPrice(tag)
        self.__setMoreInfo(tag)

    def __setPrice(self, tag):
        """convert text to integer
        Args:
            tag (bs4:element.Tag): model tag
        """
        price = tag.find(
            "li",
            {"class": ""}).text
        temp = price[:-2]
        self.__price = int(temp.replace(',', '')) * 10000

    def __setMoreInfo(self, tag):
        """
        Args:
            tag (bs4:element.Tag): model tag
        """
        data = tag.find_all(
            "span",
            {"class": ""})

        self.__setRoomType(data[0].text)
        self.__setBuildAt(data[1].text)
        self.__setEstateSize(data[2].text)
        self.__setGroundSize(data[3].text)

    def __setRoomType(self, text):
        """
        Args:
            tag (bs4:element.Tag): model tag
        """
        self.__roomType = text

    def __setBuildAt(self, text):
        """
        Args:
            tag (bs4:element.Tag): model tag
        """
        temp = text[1:][:-1]
        self.__buildAt = temp

    def __setEstateSize(self, text):
        """
        Args:
            tag (bs4:element.Tag): model tag
        """
        temp = text[:-1]
        self.__estateSize = temp

    def __setGroundSize(self, text):
        """
        Args:
            tag (bs4:element.Tag): model tag
        """
        temp = text[:-1]
        self.__groundSize = temp

    def toString(self):
        """this attributes output as csv

        Returns:
            string: as csv of a record
        """
        return ",".join([
            str(self.__price),
            str(self.__roomType),
            str(self.__buildAt),
            str(self.__estateSize),
            str(self.__groundSize),
        ])
