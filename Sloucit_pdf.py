import tkinter as tk
from tkinter import W
from tkinter import messagebox

import glob
from os import path, makedirs
from PyPDF2 import PdfFileReader, PdfFileWriter


class Pdf:
    def __init__(self):
        self.vstup = "./IN/"
        self.vystup = "./OUT/"
        self.overit_strukturu(self.vstup, self.vystup)

    def overit_strukturu(self, vstup, vystup):
        try:
            if not path.exists(vstup):
                makedirs(vstup)
            if not path.exists(vystup):
                makedirs(vystup)
        except PermissionError as e:
            messagebox.showwarning("ERROR", "Odmítný přístup!!")
            raise e

    def pdf_soubory_IN(self, vstup):
        soubory_typu_pdf = glob.glob(path.join(vstup, "*.pdf"))
        return soubory_typu_pdf

    def sluc(self, seznam, vystup):
        sloucit_pdf = PdfFileWriter()

        for soubor in seznam:
            pdf = PdfFileReader(soubor)
            pocet_stranek = pdf.getNumPages()
            for stranka in range(pocet_stranek):
                sloucit_pdf.addPage(pdf.getPage(stranka))
        output = vystup + "slouceno.pdf"
        with open(output, "wb") as output_pdf:
            sloucit_pdf.write(output_pdf)
        
        
class PdfGUI(tk.Frame):
    def __init__(self, parent, pdf):
        super().__init__(parent)
        self.parent = parent
        self.pdf = pdf
        self.parent.title("Pyladies - sloučení PDF souborů")
        self.vytvor_plochu()

    def vytvor_plochu(self):
        self.nadpis = tk.LabelFrame(root, text="Do adresáře IN vlož soubory ke sloučení.", font="Arial 16")
        self.nadpis.grid(row=0, column=0)
        self.sloucit = tk.Button(self.nadpis, text="Sloučit PDF", command=self.sloucit_pdf, font="Arial 16", width=80)
        self.sloucit.grid(row=1, column=0)

    def sloucit_pdf(self):
        soubory = pdf.pdf_soubory_IN(self.pdf.vstup)
        pdf.sluc(soubory, self.pdf.vystup)
        messagebox.showwarning("HOTOVO", "Ve složce OUT najdeš sloučený PDF soubor")
        


root = tk.Tk()
pdf = Pdf()
app = PdfGUI(root, pdf)
app.mainloop()
