from tkinter import filedialog
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from tkinter import scrolledtext as ScrolledText
import tkinter
import threading
import logging
import copy
from resistorPicture import *


class TextHandler(logging.Handler):
    """This class allows you to log to a Tkinter Text or ScrolledText widget"""

    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.text.configure(state='normal')
            self.text.insert(tkinter.END, msg + '\n')
            self.text.configure(state='disabled')
            # Autoscroll to the bottom
            self.text.yview(tkinter.END)
        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)


class configForm(tkinter.Tk):

    def __init__(self):
        '''
        Configuration
        Setup form
        Set form to non-resizable
        Set form title
        '''

        tkinter.Tk.__init__(self)

        self.resizable(0, 0)
        self.wm_title('Resistor Config')

        cwd = os.getcwd()
        iconLocation = "{}\\icon.ico".format(cwd)
        self.iconbitmap(r'{}'.format(iconLocation))

        self.frame1 = tkinter.Frame(self)
        # self.frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = "WS")
        self.frame1.pack(side="left", anchor="nw")
        self.frame2 = tkinter.Frame(self)
        self.frame2.pack(side="left")
        # self.frame2.grid(row = 3, column = 0, rowspan = 3, columnspan = 2, sticky = "ES")


        self.filePrefixLbl = tkinter.Label(self.frame1, text="File Prefix:")
        self.filePrefixLbl.grid(
            row=0, column=0, sticky='E', padx=5, pady=2)

        self.filePrefixTxt = tkinter.Entry(self.frame1)
        self.filePrefixTxt.grid(
            row=0, column=1, sticky="W", pady=3)

        self.selectInputCSV = tkinter.Button(
            self.frame1, text="CSV File Location", command=self.openCSV)
        self.selectInputCSV.grid(row=1, column=0, sticky='N', padx=5, pady=2)

        self.selectOutputDirectory = tkinter.Button(
            self.frame1, text="Output Directory", command=self.openDirectory)
        self.selectOutputDirectory.grid(
            row=1, column=1, sticky='NW', padx=5, pady=2)

        self.processFile = tkinter.Button(
            self.frame1, text="Process Files", command=self.processFiles)
        self.processFile.grid(row=3, column=0, sticky='WN', padx=5, pady=2)

        self.logText = ScrolledText.ScrolledText(self.frame2, state='disabled', width  = 145,)
        self.logText.configure(font='TkFixedFont')
        self.logText.grid(row=1, column=1, sticky='nesw', padx=5, pady=2)

        # Create textLogger
        text_handler = TextHandler(self.logText)

        # Add the handler to logger
        self.logger = logging.getLogger()
        self.logger.addHandler(text_handler)
        self.logger.warn(
            "Resistor Picture Generator\n--------------------------------\nCreated by Dominic Gaiero for the CP IEEE SB website\n--------------------------------\n")

    def openCSV(self):
        if messagebox.askyesno("Open CSV", "The CSV file should be formatted as follows\nvalue,tolerence,num. bands.\nIf this is true, click 'Yes'. Otherwise click 'No'."):
            self.filename = filedialog.askopenfilename(
                initialdir="/", title="Select file", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
            self.csvFileName = self.filename
            csvFile = ("CSV Location: {}".format(self.csvFileName))
            self.logger.warn("CSV Location: {}".format(self.csvFileName))
            self.csvTest()

    def openDirectory(self):
        # from tkinter.filedialog import askdirectory
        self.directoryLocation = askdirectory(
            parent=self, initialdir="/", title='Please select a directory')
        print(self.directoryLocation)
        self.logger.warn(("Directory Location: {}").format(
            self.directoryLocation))

    def processFiles(self):
        try:
            print(self.directoryLocation)
            print(self.filePrefixTxt.get())
        except AttributeError:
            messagebox.showerror(
                "Error", "Data entered is invalid. Try again.")
            self.logger.warn("Data entered is invalid. Try again.")
            print("Error")
            return
        csvLocation = self.csvFileName
        cwd = self.directoryLocation
        prefix = self.filePrefixTxt.get()
        f = open(csvLocation, "rt")
        try:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                resistorValue = row[0]
                resistorTolerance = float(row[1])
                numBands = row[2]
                resistorData = getResistorData(
                    resistorValue, resistorTolerance, numBands)
                self.logger.warn(
                    "--------------------------------\nGenerated data for:")
                self.logger.warn(
                    "|{:>8s}|{:>8s}|{:>8s}|{:>8s}|{:>8s}|{:>8s}|{:>8s}|".format("Value","Tolerence","Band 1","Band 2","Band 3","Band 4","Band 5")
                )
                self.logger.warn(
                    "|{:>8}|{:>8}%|{:>8}|{:>8}|{:>8}|{:>8}|{:>8}|".format(resistorData[0][0],resistorData[0][1],resistorData[1][0],resistorData[1][1],resistorData[1][2],resistorData[1][3],resistorData[1][4])
                )
                pictureStatus = generatePicture(resistorData, cwd, prefix)
                if pictureStatus[0]:
                    self.logger.warn("Wrote file: {}".format(pictureStatus[1]))
        finally:
            f.close()
        self.logger.warn("--------------------------------\n")
        self.logger.warn("Done\n")
        self.logger.warn("--------------------------------\n")
        if messagebox.askyesno("Open output folder", "Do you want to open the folder?"):
            os.startfile(cwd)

    def csvTest(self):
        f = open(self.csvFileName, "rt")
        header = f.readline()
        header=header.strip()
        # self.logger.warn("CSV Header:\n{}".format(header))
        headerMore = header.split(",")
        headerString = '|'
        # print(tuple(headerMore))
        for i in range(len(headerMore)):
            headerString+="{:>10s}|"
        headerString=headerString.strip()
        self.logger.warn(headerString.format(*tuple(headerMore)))
        line1 = f.readline().strip()
        line1More = line1.split(",")
        self.logger.warn(headerString.format(*tuple(line1More)))
        # self.logger.warn("CSV Line 1:\n{}".format(line1))
        self.logger.warn("--------------------------------\n")


if __name__ == '__main__':
    form = configForm()
    form.mainloop()
