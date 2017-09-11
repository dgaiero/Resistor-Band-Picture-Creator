# 2 DECIMAL POINT
#9-3-17

# Initialize resistor colors
BLACK  = ['black', 0, 0, 0, 1, None]
BROWN  = ['brown', 1, 1, 1, 10, "1%"]
RED    = ['red', 2, 2, 2, 100, "2%"]
ORANGE = ['orange', 3, 3, 3, 1000, "3%"]
YELLOW = ['yellow', 4, 4, 4, 10000, "4%"]
GREEN  = ['green', 5, 5, 5, 100000, "0.5%"]
BLUE   = ['blue', 6, 6, 6, 1000000, "0.25"]
PURPLE = ['purple', 7, 7, 7, 10000000, "0.15%"]
GREY   = ['grey', 8, 8, 8, None, "0.05%"]
WHITE  = ['white', 9, 9, 9, None, None]
GOLD   = ['gold', None, None, None, 0.1, "5%"]
SILVER = ['silver', None, None, None, 0.01, "10%"]
RESISTORCOLORS = [BLACK, BROWN, RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, GREY, WHITE, GOLD, SILVER]

currentColorBandDict = {}
newResistorValueList = []

# Ask for user input of resistor value, number of bands, and tolerance value
userInputResistorValue = float(input("Enter the resistor value: "))
#userInputNumBands = int(input("Enter the number of bands: "))
userInputNumBands = 5
print ("Tolerance Values: 0.05% | 0.1% | 0.25% | 0.5% | 1% | 2% | 5% | 10% | 20%")
#userInputToleranceValue = str(input("Enter the tolerance value: "))
userInputToleranceValue = '5%'

# Add each digit in userInputResistorValue to string in a list
oldResistorValueList = list(str(userInputResistorValue))

# Add a '0' to fix input values less than 1 rounded to 1 decimal place
if userInputResistorValue < 10 and (len(oldResistorValueList) == 3 or len(oldResistorValueList) == 4):
    oldResistorValueList.append('0')

# Create a new list with digits other than 0 and a decimal point
# Determine if userInputResistorValue is a decimal number
for item in oldResistorValueList:
    if item == '.':
        if newResistorValueList[0] == 0:
            del newResistorValueList[0]
    else:
        newResistorValueList.append(int(item))

# Executes if 4 band color code is requested
if userInputNumBands == 5:
    i = 0 # first band iterator
    j = 0 # second band iterator
    k = 0 # third band iterator
    l = 0 # multiplier iterator
    m = 0 # tolerance iterator

    # Get firstBandNum and firstBandColor
    while i <= 11:
        if RESISTORCOLORS[i][1] == newResistorValueList[0]:
            currentColorBandDict['firstBandColor'] = RESISTORCOLORS[i][0]
            #if DECIMAL == True and userInputResistorValue < 1:
            if userInputResistorValue < 1:
                firstBandNum = oldResistorValueList[2]
            else:
                firstBandNum = oldResistorValueList[0]
        i += 1

    # Get secondBandNum and secondBandColor
    while j <= 11:
        if RESISTORCOLORS[j][2] == newResistorValueList[1]:
            currentColorBandDict['secondBandColor'] = RESISTORCOLORS[j][0]
            if userInputResistorValue < 1:
                secondBandNum = oldResistorValueList[3]
            elif userInputResistorValue >= 1 and userInputResistorValue < 10:
                secondBandNum = oldResistorValueList[2]
            else:
                secondBandNum = oldResistorValueList[1]
        j += 1

    # Get thirdBandNum and thirdBandColor
    while k <= 11:
        if RESISTORCOLORS[k][3] == newResistorValueList[2]:
            currentColorBandDict['thirdBandColor'] = RESISTORCOLORS[k][0]
            if oldResistorValueList[2] == '.':
                thirdBandNum = oldResistorValueList[3]
            else:
                thirdBandNum = oldResistorValueList[2]
        k += 1

    # Calculate multiplier value
    firstSecondAndThirdBandNum = float(firstBandNum + secondBandNum + thirdBandNum)
    multiplier = round((userInputResistorValue / firstSecondAndThirdBandNum), 3)

    # Get fourthBandColor
    while l <= 11:
        if RESISTORCOLORS[l][4] == multiplier:
            currentColorBandDict['fourthBandColor'] = RESISTORCOLORS[l][0]
        l += 1

    # Get fifthBandColor
    while m <= 11:
        if RESISTORCOLORS[m][5] == userInputToleranceValue:
            currentColorBandDict['tolerance'] = RESISTORCOLORS[m][0]
        m += 1

# Display current color band in the terminal
print (currentColorBandDict)
