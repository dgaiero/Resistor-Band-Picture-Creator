# Project: Resistor-Band-Picture-Creator
# Author: Dominic Gaiero, Russell Caletena
# File: resistorColor.py
# These functions return the color bands of the resistor


import math
# A value is an unsigned int, representing the resistor value (normalized at ohms)
# A exp is a signed int, representing the exponent of the resistor
# A tolerance is an unsigned int, representing the tolerance of the resistor
# ->
# This function takes a value, exp, and optional tolerance and returns a tuple with the color bands
def getFourBands(value,numBands,tolerance=5):

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

    currentColorBandDict = {}
    newResistorValueList = []

    # Add each digit in value to string in a list
    oldResistorValueList = list(str(value))

    # Add a '0' to fix input values less than 1 rounded to 1 decimal place
    if value < 10 and len(oldResistorValueList) == 3:
        oldResistorValueList.append('0')

    # Create a new list with digits other than 0 and a decimal point
    # Determine if value is a decimal number
    for item in oldResistorValueList:
        if item == '.':
            if newResistorValueList[0] == 0:
                del newResistorValueList[0]
        else:
            newResistorValueList.append(int(item))

    # Executes if 4 band color code is requested
    if numBands == 4:
        i = 0 # first band iterator
        j = 0 # second band iterator
        k = 0 # multiplier iterator
        l = 0 # tolerance iterator

        # Get firstBandNum and firstBandColor
        while i <= 11:
            if RESISTORCOLORS[i][1] == newResistorValueList[0]:
                band1 = RESISTORCOLORS[i][0]
                #if DECIMAL == True and value < 1:
                if value < 1:
                    band1Num = oldResistorValueList[2]
                else:
                    band1Num = oldResistorValueList[0]
            i += 1

        # Get secondBandNum and secondBandColor
        while j <= 11:
            if RESISTORCOLORS[j][2] == newResistorValueList[1]:
                band2 = RESISTORCOLORS[j][0]
                if value < 1:
                    band2Num = oldResistorValueList[3]
                elif value >= 1 and value < 10:
                    band2Num = oldResistorValueList[2]
                else:
                    band2Num = oldResistorValueList[1]
            j += 1

        # Calculate multiplier value
        firstAndSecondBandNum = float(band1Num + band2Num)
        multiplier = round((value / firstAndSecondBandNum), 3)

        # Get thirdBandColor
        while k <= 11:
            if RESISTORCOLORS[k][4] == multiplier:
                band3 = RESISTORCOLORS[k][0]
            k += 1

        # Get fourthBandColor
        while l <= 11:
            if RESISTORCOLORS[l][5] == tolerance:
                band4 = RESISTORCOLORS[l][0]
            l += 1

    # Display current color band in the terminal
    band5 = "none"
    bands = (band1,band2,band3,band4,band5)
    return bands

def getFiveBands(value,exp,tolerance=5):
    # Dictionary for color codes
    colorcode={-2:"silver", -1:"gold", 0:"black", 1:"brown", 2:"red", 3:"orange", 4:"yellow", 5:"green", 6:"blue", 7:"violet", 8:"grey", 9:"white", 10:"none"}
    valueNormalize = value/10**exp
    values = str(valueNormalize).split(".")

    if tolerance == 5:
        toleranceColor = -1
    elif tolerance == 10:
        toleranceColor = -2
    elif tolerance == 1:
        toleranceColor = 1
    print(exp)
    precision = 5
    print(value)
    value1=math.floor(value * 100 * math.pow(10, precision)) / math.pow(10, precision)
    print(value1)
    value1 = str(value1).split(".")
    value1 = value1[0]
    band1Value = int(value1[0])
    band2Value = int(value1[1])
    band3Value = int(value1[2])
    band4Value = exp
    band5Value = toleranceColor
    band1 = colorcode[band1Value]
    band2 = colorcode[band2Value]
    band3 = colorcode[band3Value]
    band4 = colorcode[band4Value]
    band5 = colorcode[band5Value]
    bands = (band1,band2,band3,band4,band5)
    print(bands)
    return bands

# A value is a string, representing the un-normalized resistor value
# ->
# This function takes a value and returns a normalized value and an exponent
def getWholeValue(value):
	exp={"f":-15,"p":-12,"n":-9,"u":-6,"m":-3,"":0,"k":3,"M":6,"G":9,"T":12,"P":15}
	modifier=value[-1]
	if modifier.isalpha():
		value=value[0:-1]
	else:
		modifier=""
	value=int(float(value)*10**exp[modifier])
	return value, exp[modifier]

if __name__ == "__main__":
    # Default test value
    resistorValue="170k"
    resistorData = getWholeValue(resistorValue)
    getFiveBands(resistorData[0],resistorData[1])
