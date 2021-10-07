from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
class myParser:
    __rawData = ()
    def __init__(self,datafile):
        page_html= open(datafile,"r")
        """html parsing"""
        page_soup = soup(page_html, "html.parser")
        '''Stores each line with tag <td> into a list'''
        DataLines = page_soup.findAll("td")
        '''creates a new list that removes the html tags off the values'''
        
        for s in DataLines:
            for s2 in s:
                self.rawData.append(s2)
        if (datafile == "Co2.html"):
            for i in 2:
               self.rawData.pop(i)
        elif (datafile == "Temperature.html"):
            for i in 3:
                self.rawData.pop(i)

    def getRawData(self):
        return self.__rawData

    