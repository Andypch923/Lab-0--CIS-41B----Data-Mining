import myParser
from collections import namedtuple
class co2:
    co2DataOfYear = namedtuple('co2DataOfYear',['year','month','deciaml','average','interpolated','trend','days'])
    __listOfCo2Data = ()
    __listOfCo2Dicts = ()
    def __init__(self,tempRawData):
        for s in tempRawData:
            tempNamedTupleOfCo2Data = self.co2DataOfYear(s[0],s[1],s[2],s[3],s[4],s[5],s[6])
            self.__listOfCo2Data.append(tempNamedTupleOfCo2Data)
    
    def getListOfCo2Dicts(self):
        return self.__listOfCo2Dicts

    def createDict(self,listOfMonthlyData):
        tempSumOfAverage = 0
        counter = 0
        for listOfData in self.__listOfCo2Data:
            if counter == 0:
                tempYear = int(listOfData[0])
            tempSumOfAverage += listOfData[3]
            counter += 1
            if counter == 12:
                yearAverage = tempSumOfAverage/12
                self.__listOfCo2Dicts.append({tempYear:yearAverage})
                tempYear = 0
                tempSumOfAverage = 0
                counter = 0

