import re

with open("Day 2 - reportList.txt") as f:
    reportList = f.read()

print(reportList)


individualReports = re.split("\n", reportList)


print(individualReports)

successReports = 0

for i in individualReports:
    #print(i)
    report = re.split(" ", i)
    reportLoop = 1
    reportLength = len(report)-1
    for r in report:
        if reportLoop == len(report):
            successReports = successReports + 1
            break
        firstValue = int(r)
        #print(firstValue)
        secondValue = int(report[reportLoop])
        #print(secondValue)
        totalValue = firstValue-secondValue
        #print(totalValue)
        if reportLoop == 1:
            if totalValue > 0:
                pos = True
            elif totalValue < 0:
                pos = False
            else:
                break
        else:
            if pos == True:
                if totalValue > 0:
                    pass
                else:
                    break
            elif pos == False:
                if totalValue < 0:
                    pass
                else:
                    break
        totalValue = abs(totalValue)
        #print(totalValue)
        if totalValue >3:
            break
        elif totalValue == 0:
            break
        reportLoop = reportLoop + 1
    #print(report)
    #break

