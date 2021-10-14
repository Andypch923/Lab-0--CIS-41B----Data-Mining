import myParser
import temperature
import co2
import slope

rawParsedCo2 = myParser.myParser("Co2.html")
rawParsedTemp = myParser.myParser("Temperature.html")


tempObj = temperature.temperature(rawParsedTemp.getRawData())
co2Obj = co2.co2(rawParsedCo2.getRawData())

slopeObj = slope.slope(co2Obj.getCo2Dict(),tempObj.getTempDict())
print(slopeObj.getLinearRegressionGraph())