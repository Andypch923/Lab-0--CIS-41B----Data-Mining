import re
testfile = open("Co2.html",'r')
stuff = list()
for line in testfile:
    x = line[re.search([0-9], line):re.search([0-9], line)+4]
    stuff.append(x)

for x in stuff:
    print(x)