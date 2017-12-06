# Project: Resistor-Band-Picture-Creator
# Author: Dominic Gaiero, Russell Caletena
# File: resistorColor.py
# These functions return the color bands of the resistor


# A value is an unsigned int, representing the resistor value (normalized at ohms)
# A exp is a signed int, representing the exponent of the resistor
# A tolerance is an unsigned int, representing the tolerance of the resistor
# ->
# This function takes a value, exp, and optional tolerance and returns a
# tuple with the color bands


def getFourBands(userInputResistorValue, userInputToleranceValue=5):
    # bands=("red","gold","black","violet","none")

    # Initialize resistor colors
    BLACK = ['black', 0, 0, 0, 1, None]
    BROWN = ['brown', 1, 1, 1, 10, 1]
    RED = ['red', 2, 2, 2, 100, 2]
    ORANGE = ['orange', 3, 3, 3, 1000, None]
    YELLOW = ['yellow', 4, 4, 4, 10000, None]
    GREEN = ['green', 5, 5, 5, 100000, 0.5]
    BLUE = ['blue', 6, 6, 6, 1000000, 0.25]
    PURPLE = ['violet', 7, 7, 7, 10000000, 0.1]
    GREY = ['grey', 8, 8, 8, None, 0.05]
    WHITE = ['white', 9, 9, 9, None, None]
    GOLD = ['gold', None, None, None, 0.1, 5]
    SILVER = ['silver', None, None, None, 0.01, 10]
    RESISTORCOLORS = [BLACK, BROWN, RED, ORANGE, YELLOW,
                      GREEN, BLUE, PURPLE, GREY, WHITE, GOLD, SILVER]

    currentColorBandDict = {}
    newResistorValueList = []

    # Add each digit in userInputResistorValue to string in a list
    oldResistorValueList = list(str(userInputResistorValue))

    # Add a '0' to fix input values less than 1 rounded to 1 decimal place
    if userInputResistorValue < 10 and len(oldResistorValueList) == 3:
        oldResistorValueList.append('0')

    # Create a new list with digits other than 0 and a decimal point
    for item in oldResistorValueList:
        if item == '.':
            if newResistorValueList[0] == 0:
                del newResistorValueList[0]
        else:
            newResistorValueList.append(int(item))

    i = 0  # first band iterator
    j = 0  # second band iterator
    k = 0  # multiplier iterator
    l = 0  # tolerance iterator

    # Get firstBandNum and firstBandColor
    while i <= 11:
        if RESISTORCOLORS[i][1] == newResistorValueList[0]:
            band1 = RESISTORCOLORS[i][0]
            # if DECIMAL == True and userInputResistorValue < 1:
            if userInputResistorValue < 1:
                firstBandNum = oldResistorValueList[2]
            else:
                firstBandNum = oldResistorValueList[0]
        i += 1

    # Get secondBandNum and secondBandColor
    while j <= 11:
        if RESISTORCOLORS[j][2] == newResistorValueList[1]:
            band2 = RESISTORCOLORS[j][0]
            if userInputResistorValue < 1:
                secondBandNum = oldResistorValueList[3]
            elif userInputResistorValue >= 1 and userInputResistorValue < 10:
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
            band3 = RESISTORCOLORS[k][0]
        k += 1

    # Get fourthBandColor
    while l <= 11:
        if RESISTORCOLORS[l][5] == userInputToleranceValue:
            band4 = RESISTORCOLORS[l][0]
        l += 1

    # Display current color band in the terminal
    band5 = "none"
    bands = (band1, band2, band3, band4, band5)
    return bands


def getFiveBands(userInputResistorValue, userInputToleranceValue=5):
    # Initialize resistor colors
    BLACK = ['black', 0, 0, 0, 1, None]
    BROWN = ['brown', 1, 1, 1, 10, 1]
    RED = ['red', 2, 2, 2, 100, 2]
    ORANGE = ['orange', 3, 3, 3, 1000, None]
    YELLOW = ['yellow', 4, 4, 4, 10000, None]
    GREEN = ['green', 5, 5, 5, 100000, 0.5]
    BLUE = ['blue', 6, 6, 6, 1000000, 0.25]
    PURPLE = ['violet', 7, 7, 7, 10000000, 0.1]
    GREY = ['grey', 8, 8, 8, None, 0.05]
    WHITE = ['white', 9, 9, 9, None, None]
    GOLD = ['gold', None, None, None, 0.1, 5]
    SILVER = ['silver', None, None, None, 0.01, 10]
    RESISTORCOLORS = [BLACK, BROWN, RED, ORANGE, YELLOW,
                      GREEN, BLUE, PURPLE, GREY, WHITE, GOLD, SILVER]

    currentColorBandDict = {}
    newResistorValueList = []

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

    i = 0  # first band iterator
    j = 0  # second band iterator
    k = 0  # third band iterator
    l = 0  # multiplier iterator
    m = 0  # tolerance iterator

    # Get firstBandNum and firstBandColor
    while i <= 11:
        if RESISTORCOLORS[i][1] == newResistorValueList[0]:
            band1 = RESISTORCOLORS[i][0]
            # if DECIMAL == True and userInputResistorValue < 1:
            if userInputResistorValue < 1:
                firstBandNum = oldResistorValueList[2]
            else:
                firstBandNum = oldResistorValueList[0]
        i += 1

    # Get secondBandNum and secondBandColor
    while j <= 11:
        if RESISTORCOLORS[j][2] == newResistorValueList[1]:
            band2 = RESISTORCOLORS[j][0]
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
            band3 = RESISTORCOLORS[k][0]
            if oldResistorValueList[2] == '.':
                thirdBandNum = oldResistorValueList[3]
            else:
                thirdBandNum = oldResistorValueList[2]
        k += 1

    # Calculate multiplier value
    firstSecondAndThirdBandNum = float(
        firstBandNum + secondBandNum + thirdBandNum)
    multiplier = round(
        (userInputResistorValue / firstSecondAndThirdBandNum), 3)

    # Get fourthBandColor
    while l <= 11:
        if RESISTORCOLORS[l][4] == multiplier:
            band4 = RESISTORCOLORS[l][0]
        l += 1

    # Get fifthBandColor
    while m <= 11:
        if RESISTORCOLORS[m][5] == userInputToleranceValue:
            band5 = RESISTORCOLORS[m][0]
        m += 1

    # Display current color band in the terminal
    bands = (band1, band2, band3, band4, band5)
    return bands


# A value is a string, representing the un-normalized resistor value
# ->
# This function takes a value and returns a normalized value and an exponent


def getWholeValue(value):
    exp = {"f": -15, "p": -12, "n": -9, "u": -6, "m": -3,
           "": 0, "k": 3, "M": 6, "G": 9, "T": 12, "P": 15}
    modifier = value[-1]
    if modifier.isalpha():
        value = value[0:-1]
    else:
        modifier = ""
    value = float(float(value) * 10**exp[modifier])
    return value, exp[modifier]


if __name__ == "__main__":
    # Default test value
    resistorValue = "170k"
    resistorData = getWholeValue(resistorValue)
    getFiveBands(resistorData[0], resistorData[1])
