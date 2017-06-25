'''
Resistor Picture Generator

Used for the Cal Poly IEEE Student Branch Store
to display resistor value pictures

Usage:

python resistorPicture.py file.csv
make sure you have imageExport as a directory

By: Dominic Gaiero
'''


# ==========================================
# Import Libraries
# ==========================================


from PIL import Image, ImageDraw, ImageFont
import os
import csv
import sys


# ==========================================
# Define Debug Variable
# ==========================================


DEBUG_ID = 1


# ==========================================
# Format resistor data
# ==========================================


def getResistorData(resistorValue, resistorTolerance, numBands, resistorColors):
    resistance = resistorValue
    tolerance = resistorTolerance
    resistorData = [[resistorValue, numBands, tolerance], resistorColors]
    debug(resistorData)
    return resistorData


# ==========================================
# generate picture based on resistor data
# ==========================================


def generatePicture(resistorData):
    resistorFont = ImageFont.truetype("formata.ttf", 133)
    resistorSymbolFont = ImageFont.truetype("cb.ttf", 300)
    bands = [((0, 0), (0, 100), (100, 100), (100, 0)),
             ((0, 100), (0, 200), (100, 200), (100, 100)),
             ((0, 200), (0, 300), (100, 300), (100, 200)),
             ((0, 300), (0, 400), (100, 400), (100, 300)),
             ((0, 400), (0, 5000), (100, 500), (100, 400))]

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

    im = Image.new('RGB', (500, 500), background)
    draw = ImageDraw.Draw(im)
    textWidth = draw.textsize(resistorData[0][0], font=resistorFont)
    textLocation = 300 - textWidth[0] // 2
    draw.text((textLocation, 336),
              resistorData[0][0], ieeeBlue, font=resistorFont)
    resistorTextWidth = draw.textsize("Y", font=resistorSymbolFont)
    resistorTextLocation = 300 - textWidth[0] // 2
    draw.text((resistorTextLocation, 50), "Y",
              ieeeBlue, font=resistorSymbolFont)
    # draw = ImageDraw.Draw(resistorSymbol)
    for i in range(5):
        draw.polygon(bands[i], fill=resistorColors[resistorData[1][i]])
    imageName = "res-{}".format(resistorData[0][0])
    cwd = os.getcwd()
    saveLocation = "{}\\imageExport\\{}.gif".format(cwd, imageName)
    im.save(saveLocation)


# ==========================================
# Turn debug mode on or off
# ==========================================


def debug(message):
    if DEBUG_ID == 0:
        return()
    elif DEBUG_ID == 1:
        print(message)


# ==========================================
# read and parse csv file
# ==========================================


def main():
    csvLocation = sys.argv[1]
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
            generatePicture(resistorData)
    finally:
        f.close()


# ==========================================
# Run main
# ==========================================
if __name__ == "__main__":
    main()
