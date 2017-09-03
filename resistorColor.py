# Project: Resistor-Band-Picture-Creator
# Author: Dominic Gaiero
# File: resistorColor.py
# These functions return the color bands of the resistor


import math
# A value is an unsigned int, representing the resistor value (normalized at ohms)
# A exp is a signed int, representing the exponent of the resistor
# A tolerance is an unsigned int, representing the tolerance of the resistor
# ->
# This function takes a value, exp, and optional tolerance and returns a tuple with the color bands
def getFourBands(value,exp,tolerance=5):
    # Dictionary for color codes
    colorcode={-2:"silver", -1:"gold", 0:"black", 1:"brown", 2:"red", 3:"orange", 4:"yellow", 5:"green", 6:"blue", 7:"violet", 8:"grey", 9:"white", 10:"none"}
    valueNormalize = value/10**exp
    values = str(valueNormalize).split(".")
    # Sets tolerance color band
    if tolerance == 5:
        toleranceColor = -1
    elif tolerance == 10:
        toleranceColor = -2
    elif tolerance == 1:
        toleranceColor = 1
    if int(values[1]) == 0 and len(values[0]) != 1:
        lengthCode = len(values[0])
        if lengthCode == 3:
            band1Value = int(values[0][0])
            band2Value = int(values[0][1])
            band3Value = int(values[0][2])
            band4Value = exp
            band5Value = toleranceColor
            # band4Value = 10
        elif lengthCode == 2:
            band1Value = int(values[0][0])
            band2Value = int(values[0][1])
            band3Value = exp
            band4Value = toleranceColor
            band5Value = 10
            # band4Value = 10
    else:
        band1Value = int(values[0])
        if len(values[1]) == 1:
            band2Value = int(values[1])
            band3Value = exp-1
            band4Value = toleranceColor
            band5Value = 7
        elif len(values[1]) == 2:
            band2Value = int(values[1][0])
            band3Value = int(values[1][1])
            band4Value = exp-1
            band5Value = toleranceColor
    band1 = colorcode[band1Value]
    band2 = colorcode[band2Value]
    band3 = colorcode[band3Value]
    band4 = colorcode[band4Value]
    band5 = colorcode[band5Value]
    bands = (band1,band2,band3,band4,band5)
    print(bands)
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
