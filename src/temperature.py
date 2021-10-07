import myParser
from collections import namedtuple
class temperature:
    tempDataOfYear = namedtuple('tempDataOfYear',['median','upper','lower'])
    listOfTemperatureDicts = ()
    def __init__(self,tempRawData):
        counter = 1
        for s in tempRawData:
            if counter == 1:
                temp1 = s
                counter += 1
            if counter == 2:
                temp2 = s
                counter += 1
            if counter == 3:
                temp3 = s
                counter += 1
            if counter == 4:
                temp4 = s
                tempNamedTuple = self.tempDataOfYear(temp2,temp3,temp4)
                self.__listOfTemperatureData.append({temp1:tempNamedTuple})
                counter = 1
