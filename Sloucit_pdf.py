import tkinter as tk
from tkinter import W
from tkinter import messagebox

import glob
from os import path, makedirs
from PyPDF2 import PdfFileReader, PdfFileWriter


class Pdf:
    def __init__(self):
        ...


class PdfGUI(tk.Frame):
    def __init__(self, parent, pdf):
        super().__init__(parent)
        self.parent = parent
        self.pdf = pdf
        self.parent.title("Pyladies - sloučení PDF souborů")



if __name__ == '__main__':
    root = tk.Tk()
    pdf = Pdf()
    app = PdfGUI(root, pdf)
    app.mainloop()