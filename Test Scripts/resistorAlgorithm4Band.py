# 2 DECIMAL POINT
#9-3-17


def resistor4Band(value,numBands,tolerance):

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

if __name__ == "__main__":
    # Ask for user input of resistor value, number of bands, and tolerance value
    userInputResistorValue = float(input("Enter the resistor value: "))
    #userInputNumBands = int(input("Enter the number of bands: "))
    userInputNumBands = 4
    print ("Tolerance Values: 0.05% | 0.1% | 0.25% | 0.5% | 1% | 2% | 5% | 10% | 20%")
    #userInputToleranceValue = str(input("Enter the tolerance value: "))
    userInputToleranceValue = '5%'
    print(resistor4Band(userInputResistorValue,userInputNumBands,userInputToleranceValue))
