import os
import sys
import logging
from tikz2graphml.parseTikz import ParseTikz
import tkinter
from tkinter import ttk, StringVar, Label, Entry, LEFT, W, Text, END, messagebox
from tkinter.filedialog import askopenfilename, askdirectory

logger = logging.getLogger()

class Gui:
    def __init__(self, window):
        # 'StringVar()' is used to get the instance of input field
        self.inputFileNameVar = StringVar()
        self.outputDirectoryVar = StringVar(value=str(os.path.join(os.getcwd(), 'output')))
        self.scaleVar = StringVar(value='100')
        window.title("Tikz to GraphML convertor")

        startRow = 0

        Label(window ,text = "TikZ to GraphML",font=("Helvetica", 30), width=100).grid(row = startRow, column = 0, sticky=W, ipadx=25, ipady=2,columnspan=10)
        startRow+=1

        # Define Input File Field which is obtained by choosing a file from browsing the file explorer
        Label(window ,text = "Input File Name : ", justify=LEFT).grid(row = startRow,column = 0, sticky=W, ipadx=10, ipady=2)
        ttk.Button(window, text = "Choose File", command = lambda: self.set_input_file_name()).grid(row = startRow,column=3, ipadx=10, ipady=2, padx=10)
        ttk.Entry(window, textvariable = self.inputFileNameVar, width = 70).grid( row = startRow, column = 1, ipadx=1, ipady=2)

        # Define Output Directory to save all the files to that folder
        # (Default) saves it in same directory as input file
        startRow+=1
        Label(window ,text = "Output File Directory : ", justify=LEFT).grid(row = startRow,column = 0, sticky=W, ipadx=10, ipady=2)
        ttk.Button(window, text = "Choose File", command = lambda: self.set_output_directory()).grid(row = startRow,column=3, ipadx=10, ipady=2, padx=10)
        ttk.Entry(window, textvariable = self.outputDirectoryVar, width = 70).grid( row = startRow, column = 1, ipadx=1, ipady=2)

        # Add a scale field to convert resulting graphml files into resonable graphs
        startRow+=1
        Label(window ,text = "Scale : ", justify=LEFT).grid(row = startRow,column = 0, sticky=W, ipadx=10, ipady=2)
        ttk.Entry(window, textvariable = self.scaleVar, width = 70).grid(row = startRow, column = 1, ipadx=1, ipady=2)

        # Convert Tikz files to GraphML files by a button!
        startRow+=1
        ttk.Button(window, text = "Convert", command = lambda: self.convertFile()).grid(row = 20,column = 3, ipadx=1, ipady=1)

    # Set the user inputs on inputFilename and outputDirectoryVar
    def set_input_file_name(self):
        self.inputFileNameVar.set(askopenfilename())
        path, filename = os.path.split(self.inputFileNameVar.get())

    # Set output directory path
    def set_output_directory(self):
        self.outputDirectoryVar.set(askdirectory())

    def get_input_file_name(self):
        return self.inputFileNameVar.get()

    def get_output_directory(self):
        return self.outputDirectoryVar.get()

    def getScale(self):
        return self.scaleVar.get()

    # Main conversion module which tries to convert tikz graphs in graphml
    # format which is stored in specified output directory
    def convertFile(self):
        logger.debug("Converting file")
        logger.debug("InputFile : {}".format(self.get_input_file_name()))
        logger.debug("Output Directory : {}".format(self.get_output_directory()))
        logger.debug("Scale : {}".format(self.getScale()))

        if(not os.path.isfile(self.get_input_file_name())):
            messagebox.showerror("tikz to graphml", "Entered File is Incorrect")
            return

        if not os.path.exists(self.get_output_directory()):
            os.makedirs(self.get_output_directory())

        if(not os.path.isdir(self.get_output_directory())):
            messagebox.showerror("tikz to graphml", "Entered Directory is Incorrect")
            return

        prefix = self.get_input_file_name()
        prefix.replace("\\","/")    # To support os.path.basename in windows systems
        prefix = os.path.basename(os.path.splitext(prefix)[0])

        ParseTikz().run(float(self.getScale()),
            self.get_input_file_name(),
            prefix,
            self.get_output_directory())

        messagebox.showinfo("tikz to graphml", "Conversion Successfull\nFiles stored in {}".format(self.get_output_directory()))
