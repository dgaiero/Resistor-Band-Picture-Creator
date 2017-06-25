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

        self.filePrefixLbl = tkinter.Label(self, text="File Prefix:")
        self.filePrefixLbl.grid(
            row=0, column=0, sticky='W', padx=5, pady=2)

        self.filePrefixTxt = tkinter.Entry(self)
        self.filePrefixTxt.grid(
            row=0, column=1, columnspan=40, sticky="WE", pady=3)

        self.selectInputCSV = tkinter.Button(self, text="CSV File Location", command=self.openCSV)
        self.selectInputCSV.grid(row=1, column=0, sticky='W', padx=5, pady=2)

        self.selectOutputDirectory = tkinter.Button(self, text="Output Directory", command=self.openDirectory)
        self.selectOutputDirectory.grid(row=1, column=1, sticky='W', padx=5, pady=2)

        self.processFile = tkinter.Button(self, text="Process Files", command=self.processFiles)
        self.processFile.grid(row=2, column=1, sticky='W', padx=5, pady=2)

        self.logText = ScrolledText.ScrolledText(self, state='disabled')
        self.logText.configure(font='TkFixedFont')
        self.logText.grid(
            row=4, column=1, sticky='S', padx=5, pady=2)

            # Create textLogger
        text_handler = TextHandler(self.logText)

        # Add the handler to logger
        self.logger = logging.getLogger()
        self.logger.addHandler(text_handler)

    def openCSV(self):
        if messagebox.askyesno("Open CSV", "The CSV file should be formatted as follows\nvalue,tolerence,num. bands,band0,band1,band2,band3,band4.\nAll colors should be lowercase.\nIf this is true, click 'Yes'. Otherwise click 'No'."):
            self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
            self.csvFileName = self.filename
            csvFile = ("CSV Location: {}".format(self.csvFileName))
            self.logger.warn("CSV Location: {}".format(self.csvFileName))
    def openDirectory(self):
        # from tkinter.filedialog import askdirectory
        self.directoryLocation = askdirectory(parent=self,initialdir="/",title='Please select a directory')
        print(self.directoryLocation)
        self.logger.warn(("Directory Location: {}").format(self.directoryLocation))
    def processFiles(self):
        try:
            print(self.directoryLocation)
            print(self.filePrefixTxt.get())
        except AttributeError:
            messagebox.showerror("Error","Data entered is invalid. Try again.")
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
                resistorColors = row[3:8]
                resistorData = getResistorData(
                    resistorValue, resistorTolerance, numBands, resistorColors)
                self.logger.warn("--------------------------------\nGenerated data for {}".format(resistorData))
                pictureStatus = generatePicture(resistorData,cwd, prefix)
                if pictureStatus[0]:
                    self.logger.warn("Wrote file: {}".format(pictureStatus[1]))
        finally:
            f.close()
        if messagebox.askyesno("Open output folder", "Do you want to open the folder?"):
            os.startfile(cwd)


if __name__ == '__main__':
    form = configForm()
    form.mainloop()
