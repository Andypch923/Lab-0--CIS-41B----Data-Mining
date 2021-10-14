import re
class myParser:
    
    def __init__(self,datafile):
        self.__rawData = list()
        page_html= open(datafile,"r")
        lines = page_html.readlines()
        """html parsing"""
        for line in lines:
          s = [float(s) for s in re.findall(r'-?\d+\.?\d*', line)]
          self.__rawData.append(s)
        if (datafile == "Co2.html"):
            for i in range(2):
               del self.__rawData[i]
            del self.__rawData[-1]
        elif (datafile == "Temperature.html"):
            for i in range(3):
                del self.__rawData[i]
            del self.__rawData[-1]
        self.__rawData = [x for x in self.__rawData if x != []]
        page_html.close()

    def getRawData(self):
        return self.__rawData
        

    