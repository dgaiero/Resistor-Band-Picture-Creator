# Resistor-Band-Picture-Creator

## NOTE: Work in Progress

#### Created by Dominic Gaiero for CP IEEE website

### Description:

This program outputs an image of a resistor's color bands. It takes input from a CSV files and outputs .gif images.

### Usage:

To run the program, use:

```
python main.py
```
For more information, see `exampleVal.csv`

If you want to use the executable, there is one in the `build > exe.win-amd64-3.5` directory. It is named `CPIEEE_RESISTOR.exe`. The script was frozen with cx_freeze.

To use, select a CSV file formatted as follows:
```
Resistor Value (normal),tolerence (in %),Number of bands
```

Then, select any diretory to output the pictures.
