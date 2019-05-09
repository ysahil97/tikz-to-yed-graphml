import tkinter
import logging
from tikz2graphml.Gui import Gui

logging.basicConfig(format='%(levelname)-1s : [%(filename)s:%(lineno)d] %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def main():
    # Right now, we use GUI(default) to take in Tikz files and output
    # in specified directory
    window = tkinter.Tk()
    window.geometry("1000x500")

    rows = 0
    while rows < 50:
        window.rowconfigure(rows, weight=2)
        window.columnconfigure(rows, weight=2)
        rows += 1

    gui = Gui(window)
    window.mainloop()

if __name__ == '__main__':
    main()
