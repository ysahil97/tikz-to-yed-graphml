import tkinter
from tkinter import ttk, StringVar, Label, Entry, LEFT, W, Text, END
from tkinter.filedialog import askopenfilename, askdirectory
import os
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
        print("Converting file")
        print("InputFile : ", self.get_input_file_name())
        print("Output Directory : ", self.get_output_directory())
        print("Scale : ", self.getScale())
        pass

if __name__ == '__main__':
    window = tkinter.Tk()
    window.geometry("1000x500")

    rows = 0
    while rows < 50:
        window.rowconfigure(rows, weight=2)
        window.columnconfigure(rows,weight=2)
        rows += 1

    gui = GUI(window, )
    window.mainloop()