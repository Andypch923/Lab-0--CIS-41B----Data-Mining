import myParser
from collections import namedtuple
class temperature:
    tempDataOfYear = namedtuple('tempDataOfYear',['year','median','upper','lower'])
    __listOfTemperatureData = list()
    __TemperatureDict = dict()
    def __init__(self,tempRawData):   
        for s in tempRawData:
            temp1 = int(s[0])
            temp2 = s[1]
            temp3 = s[2]
            temp4 = s[3]
            tempNamedTuple = self.tempDataOfYear(temp1,temp2,temp3,temp4)
            self.__listOfTemperatureData.append(tempNamedTuple)
            self.__TemperatureDict[temp1] = temp2
                
    def getTempDict(self):
        return self.__TemperatureDict