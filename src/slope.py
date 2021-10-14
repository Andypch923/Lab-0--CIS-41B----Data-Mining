from collections import namedtuple
from typing import NamedTuple
import co2
import temperature
import math
class slope:
    __graphData = namedtuple('graphData',['year','x','y'])
    def __init__(self,co2Obj,tempObj):
        for a in co2Obj.keys():
            for b in tempObj.keys():
                if (a == b):
                    self.__graphData.append((a,co2Obj[a],tempObj[b])) 

    def getLinearRegressionGraph(self):
        '''find means of all x and y values'''
        sumOfX = 0
        sumOfY = 0
        tempSum = 0
        for item in self.__graphData:
            sumOfX += item['x']
            sumOfY += item['y']
        meanOfX =  sumOfX/len(self.__graphData)
        meanOfY =  sumOfY/len(self.__graphData)
        '''find standard deviation of x and y'''
        for item in self.__graphData:
            tempSum += ((item['x'] - meanOfX))**2
        SDofX = math.sqrt(tempSum/(len(self.__graphData)-1))
        
        tempSum = 0
        
        for item in self.__graphData:
            tempSum += ((item['y'] - meanOfY))**2
        SDofY = math.sqrt(tempSum/(len(self.__graphData)-1))

        tempSum = 0
        '''find correlation value r'''
        for item in self.__graphData:
            tempSum += (item['x'] - meanOfX)*(item['y'] - meanOfY)
        
        r = (1/(len(self.__graphData)-1))*(tempSum/(SDofX*SDofY))
        '''get slope using correlation r'''
        slope = r*SDofY/SDofX
        '''get y-intercept'''
        c = self.__graphData[0]['y'] - slope * self.__graphData[0]['x']
        '''returns slope formula in string form'''
        slopeFormula = "y = " + str(slope) + " x + " + str(c)
        return slopeFormula
