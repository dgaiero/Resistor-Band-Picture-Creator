# 2 DECIMAL POINT
#9-3-17

# Initialize resistor colors
BLACK  = ['black', 0, 0, 0, 1, None]
BROWN  = ['brown', 1, 1, 1, 10, "1%"]
RED    = ['red', 2, 2, 2, 100, "2%"]
ORANGE = ['orange', 3, 3, 3, 1000, None]
YELLOW = ['yellow', 4, 4, 4, 10000, None]
GREEN  = ['green', 5, 5, 5, 100000, "0.5%"]
BLUE   = ['blue', 6, 6, 6, 1000000, "0.25"]
PURPLE = ['purple', 7, 7, 7, 10000000, "0.1%"]
GREY   = ['grey', 8, 8, 8, None, "0.05%"]
WHITE  = ['white', 9, 9, 9, None, None]
GOLD   = ['gold', None, None, None, 0.1, "5%"]
SILVER = ['silver', None, None, None, 0.01, "10%"]
RESISTORCOLORS = [BLACK, BROWN, RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, GREY, WHITE, GOLD, SILVER]

#currentColorBandList = []
currentColorBandDict = {}
newResistorValueList = []
DECIMAL = None

# Ask for user input of resistor value and number of bands
userInputResistorValue = float(input("Enter the resistor value: "))
userInputNumBands = int(input("Enter the number of bands: "))

# Add each digit in userInputResistorValue to string in a list
oldResistorValueList = list(str(userInputResistorValue))

# Add a '0' to fix input values less than 1 rounded to 1 decimal place
if userInputResistorValue < 10 and len(oldResistorValueList) == 3:
    oldResistorValueList.append('0')

# Create a new list with digits other than 0 and a decimal point
# Determine if userInputResistorValue is a decimal number
for item in oldResistorValueList:
    if item == '.':
        if newResistorValueList[0] == 0:
            del newResistorValueList[0]
        DECIMAL = True
    else:
        newResistorValueList.append(int(item))

print (oldResistorValueList)
print (newResistorValueList)
print (DECIMAL)

# Executes if 4 band color code is requested
if userInputNumBands == 4:
    i = 0 # first band iterator
    j = 0 # second band iterator
    k = 0 # multiplier iterator

    # Get firstBandNum and firstBandColor
    while i <= 11:
        if RESISTORCOLORS[i][1] == newResistorValueList[0]:
            #currentColorBandList.append(RESISTORCOLORS[i][0])
            currentColorBandDict['firstBandColor'] = RESISTORCOLORS[i][0]
            if DECIMAL == True and userInputResistorValue < 1:
            #if userInputResistorValue < 1:
                firstBandNum = oldResistorValueList[2]
            elif DECIMAL == True and userInputResistorValue >= 1 and userInputResistorValue < 10:
            #elif userInputResistorValue >= 1 and userInputResistorValue < 10:
                firstBandNum = oldResistorValueList[0]
            else:
                firstBandNum = oldResistorValueList[0]
        i += 1

    # Get secondBandNum and secondBandColor
    while j <= 11:
        if RESISTORCOLORS[j][2] == newResistorValueList[1]:
            #currentColorBandList.append(RESISTORCOLORS[j][0])
            currentColorBandDict['secondBandColor'] = RESISTORCOLORS[j][0]
            if DECIMAL == True and userInputResistorValue < 1:
            #if userInputResistorValue < 1:
                secondBandNum = oldResistorValueList[3]
            elif DECIMAL == True and userInputResistorValue >= 1 and userInputResistorValue < 10:
            #elif userInputResistorValue >= 1 and userInputResistorValue < 10:
                secondBandNum = oldResistorValueList[2]
            else:
                secondBandNum = oldResistorValueList[1]
        j += 1

    # Calculate multiplier value
    firstAndSecondBandNum = float(firstBandNum + secondBandNum)
    multiplier = round((userInputResistorValue / firstAndSecondBandNum), 3)

    # Get thirdBandColor
    while k <= 11:
        if RESISTORCOLORS[k][4] == multiplier:
            #currentColorBandList.append(RESISTORCOLORS[k][0])
            currentColorBandDict['thirdBandColor'] = RESISTORCOLORS[k][0]
        k += 1

# Display current color band in the terminal
#print (currentColorBandList)
print (currentColorBandDict)
