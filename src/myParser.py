import re
class myParser:
    __rawData = ()
    def __init__(self,datafile):
        page_html= open(datafile,"r")
        lines = page_html.readlines()
        """html parsing"""
        for line in lines:
          s = [float(s) for s in re.findall(r'-?\d+\.?\d*', line)]
          self.__rawData.append(s)
        
        if (datafile == "Co2.html"):
            for i in 3:
               self.__rawData.pop(i)
        elif (datafile == "Temperature.html"):
            for i in 4:
                self.__rawData.pop(i)

    def getRawData(self):
        return self.__rawData
        

    