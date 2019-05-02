import os
import argparse

from parseTikz import ParseTikz
import tkinter
from tkinter import ttk, StringVar, Label, Entry, LEFT, W, Text, END, messagebox
from tkinter.filedialog import askopenfilename, askdirectory
import logging

logging.basicConfig(format='%(levelname)-1s : [%(filename)s:%(lineno)d] %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

class GUI:
    def __init__(self, window): 
        # 'StringVar()' is used to get the instance of input field
        self.inputFileNameVar = StringVar()
        self.outputDirectoryVar = StringVar(value=os.getcwd())
        self.scaleVar = StringVar(value='100')
        window.title("Tikz to GraphML convertor")

        startRow = 0
        
        Label(window ,text = "TikZ to GraphML",font=("Helvetica", 30), width=100).grid(row = startRow, column = 0, sticky=W, ipadx=25, ipady=2,columnspan=10)
        startRow+=1

        Label(window ,text = "Input File Name : ", justify=LEFT).grid(row = startRow,column = 0, sticky=W, ipadx=25, ipady=2)
        ttk.Button(window, text = "Choose File", command = lambda: self.set_input_file_name()).grid(row = startRow,column=3, ipadx=10, ipady=2, padx=10)
        ttk.Entry(window, textvariable = self.inputFileNameVar, width = 70).grid( row = startRow, column = 1, ipadx=1, ipady=2)

        startRow+=1
        Label(window ,text = "Output File Directory : ", justify=LEFT).grid(row = startRow,column = 0, sticky=W, ipadx=25, ipady=2)
        ttk.Button(window, text = "Choose File", command = lambda: self.set_output_directory()).grid(row = startRow,column=3, ipadx=10, ipady=2, padx=10)
        ttk.Entry(window, textvariable = self.outputDirectoryVar, width = 70).grid( row = startRow, column = 1, ipadx=1, ipady=2)
        
        startRow+=1
        Label(window ,text = "Scale : ", justify=LEFT).grid(row = startRow,column = 0, sticky=W, ipadx=25, ipady=2)
        ttk.Entry(window, textvariable = self.scaleVar, width = 70).grid(row = startRow, column = 1, ipadx=1, ipady=2)
        
        startRow+=1
        ttk.Button(window, text = "Convert", command = lambda: self.convertFile()).grid(row = 20,column = 3, ipadx=1, ipady=1)

    def set_input_file_name(self):
        self.inputFileNameVar.set(askopenfilename())
        path, filename = os.path.split(self.inputFileNameVar.get())
        if(os.path.isdir(path)):
            self.outputDirectoryVar.set(path)

    def set_output_directory(self):
        self.outputDirectoryVar.set(askdirectory())

    def get_input_file_name(self): 
        return self.inputFileNameVar.get()

    def get_output_directory(self):
        return self.outputDirectoryVar.get()
    
    def getScale(self):
        return self.scaleVar.get()

    def convertFile(self):
        logger.debug("Converting file")
        logger.debug("InputFile : {}".format(self.get_input_file_name()))
        logger.debug("Output Directory : ".format(self.get_output_directory()))
        logger.debug("Scale : ".format(self.getScale()))

        if(not os.path.isfile(self.get_input_file_name())):
            messagebox.showerror("tikz to graphml", "Entered File is Incorrect")
            return
        
        if(not os.path.isdir(self.get_output_directory())):
            messagebox.showerror("tikz to graphml", "Entered Directory is Incorrect")
            return

        ParseTikz().run(float(self.getScale()), 1.0, self.get_input_file_name(), os.path.basename(os.path.splitext(self.get_input_file_name())[0]), self.get_output_directory())
        messagebox.showinfo("tikz to graphml", "Conversion Successfull\nFiles stored in {}".format(self.get_output_directory()))

if __name__ == '__main__':
    window = tkinter.Tk()
    window.geometry("1000x500")

    rows = 0
    while rows < 50:
        window.rowconfigure(rows, weight=2)
        window.columnconfigure(rows,weight=2)
        rows += 1

    gui = GUI(window)
    window.mainloop()

# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     # parser.add_argument("-h", "--help", type=int, help="Print this menu")
#     parser.add_argument("-v", "--verbosity", type=int, help="increase output verbosity", default=0)
#     parser.add_argument("-s", "--scale", default=200, type=float, help="Scaling Factor")
#     parser.add_argument("-i", "--input", type=str, help="Input file path", required=True)
#     parser.add_argument("-p", "--prefix", type=str, help="Output file Prefix")
#     parser.add_argument("-d", "--directory", default="./output", type=str, help="Output file directory")

#     args = parser.parse_args()

#     scalingFactor = args.scale
#     logLevel = args.verbosity
#     inputFileName = args.input
#     prefix = args.prefix
#     directory = args.directory

    