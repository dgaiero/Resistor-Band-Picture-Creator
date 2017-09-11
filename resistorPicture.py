# Project: Resistor-Band-Picture-Creator
# Author: Dominic Gaiero
# File: resistorColor.py
# These functions generate the picture of the resistor

'''
Resistor Picture Generator

Used for the Cal Poly IEEE Student Branch Store
to display resistor value pictures

Usage:

python resistorPicture.py file.csv
make sure you have imageExport as a directory

By: Dominic Gaiero
'''

# Import Libraries
from PIL import Image, ImageDraw, ImageFont
import resistorColor
import os
import csv
import sys


# Define Debug Variable
DEBUG_ID = 0


# A resistorValue is an unsigned int, representing the normalized resistor value
# A resistorTolerance is a signed int, representing the resistor tolerance
# A numBands is an unsigned int, representing the number of resistor bands
# -> arraylist
# This function formats resistor data
def getResistorData(resistorValue, resistorTolerance, numBands):
    resistance = resistorValue
    tolerance = resistorTolerance
    resistorInfo = resistorColor.getWholeValue(resistorValue)
    if numBands == 4:
        resistorColors = resistorColor.getFourBands(
            resistorInfo[0], resistorTolerance)
    elif numBands == 5:
        resistorColors = resistorColor.getFiveBands(
            resistorInfo[0], resistorTolerance)
    resistorData = [[resistorValue, numBands, tolerance], resistorColors]
    debug(resistorData)
    return resistorData


# A resistorData is an arraylist, representing the resistor value, tolerance and number of bands
# A outputLocation is a string, representing the output directory
# A prefix is a str, representing the file prefix
# ->
# This functions generates the picture


def generatePicture(resistorData, outputLocation, multiplier, prefix="res-"):
    # Define fonts
    resistorFont = ImageFont.truetype("formata.otf", int(multiplier * 0.3))
    resistorSymbolFont = ImageFont.truetype("cb.ttf", int(multiplier * 0.8))
    ieee_custom_font = ImageFont.truetype("ieee_custom_font.ttf", int(multiplier * 0.8))
    # Define band coordinates
    bands = [((0, 0), (0, 0.2 * multiplier), (0.2 * multiplier, 0.2 * multiplier), (0.2 * multiplier, 0)),
             ((0.2 * multiplier, 0), (0.4 * multiplier, 0), (0.4 * multiplier,
                                                             0.2 * multiplier), (0.2 * multiplier, 0.2 * multiplier)),
             ((0.4 * multiplier, 0), (0.6 * multiplier, 0), (0.6 * multiplier,
                                                             0.2 * multiplier), (0.4 * multiplier, 0.2 * multiplier)),
             ((0.6 * multiplier, 0), (0.8 * multiplier, 0), (0.8 * multiplier,
                                                             0.2 * multiplier), (0.6 * multiplier, 0.2 * multiplier)),
             ((0.8 * multiplier, 0), (1 * multiplier, 0), (1 * multiplier, 0.2 * multiplier), (0.8 * multiplier, 0.2 * multiplier))]

    # Define color dictionary
    resistorColors = {
        'black': (0, 0, 0),
        'brown': (142, 40, 0),
        'red': (243, 1, 0),
        'orange': (235, 138, 57),
        'yellow': (243, 244, 2),
        'green': (0, 166, 66),
        'blue': (0, 101, 181),
        'violet': (141, 90, 243),
        'grey': (115, 115, 115),
        'white': (243, 243, 243),
        'gold': (207, 181, 60),
        'silver': (192, 192, 192),
        'none': (234, 234, 234),
    }
    ieeeBlue = (0, 102, 153)
    background = (234, 234, 234)

    # Drawing
    im = Image.new('RGB', (multiplier, multiplier),
                   background)  # Defines canvas
    draw = ImageDraw.Draw(im)
    resistorText = u"{}\u2126".format(resistorData[0][0])
    # ieee_logo = u"\uE804"
    # draw.text((0.3*multiplier, 0.3 * multiplier),ieee_logo, ieeeBlue, font=ieee_custom_font)
    textWidth = draw.textsize(resistorText, font=resistorFont)
    # print("({},{})".format(textWidth[0], 0.6*multiplier))
    textLocation = (multiplier - textWidth[0]) // 2
    draw.text((textLocation, 0.3 * multiplier),
              resistorText, ieeeBlue, font=resistorFont)
    resistorTextWidth = draw.textsize(".", font=resistorSymbolFont)
    # print(resistorTextWidth)
    resistorTextLocation = (multiplier - resistorTextWidth[0]) // 2
    # print("({},{})".format(resistorTextLocation[0], 0.4*float(multiplier)))
    draw.text((resistorTextLocation, 0.2 * multiplier), ".",
              ieeeBlue, font=resistorSymbolFont)
    # draw = ImageDraw.Draw(resistorSymbol)
    for i in range(5):
        draw.polygon(bands[i], fill=resistorColors[resistorData[1][i]])
    imageName = "{}{}".format(prefix, resistorData[0][0])
    saveLocation = "{}/{}.gif".format(outputLocation, imageName)
    im.save(saveLocation)
    if os.path.isfile(saveLocation):
        return (True, saveLocation)
    else:
        return False


# A message is a str, representing a debug message
# ->
# This function turns debug on/off
def debug(message):
    if DEBUG_ID == 0:
        return()
    elif DEBUG_ID == 1:
        print(message)

 # -> picture
# This function actually reads the csv data and runs the functions necessary to
# generate the output


def main():
    try:
        csvLocation = sys.argv[1]
        currentDir = os.getcwd()
        cwd = "{}\\imageExport".format(currentDir)
        f = open(csvLocation, "rt")
        try:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                resistorValue = row[0]
                resistorTolerance = float(row[1])
                numBands = row[2]
                resistorColors = row[3:8]
                resistorData = getResistorData(
                    resistorValue, resistorTolerance, numBands, resistorColors)
                generatePicture(resistorData, cwd, "resistor_")
        finally:
            f.close()
    except:  # Deals with bad input
        print("Usage: resistorPicture.py FILE.csv")
        sys.exit()


if __name__ == "__main__":
    main()
