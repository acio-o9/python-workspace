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
            {"class": ""})
        self.__price = price.text

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
        self.__buildAt = text

    def __setEstateSize(self, text):
        """
        Args:
            tag (bs4:element.Tag): model tag
        """
        self.__estateSize = text

    def __setGroundSize(self, text):
        """
        Args:
            tag (bs4:element.Tag): model tag
        """
        self.__groundSize = text

    def toString(self):
        """this attributes output as csv

        Returns:
            string: as csv of a record
        """
        return ",".join([
            self.__price,
            self.__roomType,
            self.__buildAt,
            self.__estateSize,
            self.__groundSize
        ])
