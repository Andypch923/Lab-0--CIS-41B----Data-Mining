import myParser
from collections import namedtuple
class temperature:
    tempDataOfYear = namedtuple('tempDataOfYear',['year','median','upper','lower'])
    __listOfTemperatureData = ()
    __listOfTemperatureDicts = ()
    def __init__(self,tempRawData):   
        for s in tempRawData:
            temp1 = int(s[0])
            temp2 = s[1]
            temp3 = s[2]
            temp4 = s[3]
            tempNamedTuple = self.tempDataOfYear(temp1,temp2,temp3,temp4)
            self.__listOfTemperatureData.append(tempNamedTuple)
            self.__listOfTemperatureDicts.append({temp1:temp2})
                
    def returnListOfTempDicts(self):
        return self.__listOfTempDicts