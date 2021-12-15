import tkinter as tk
from tkinter import  N, W, E
from tkinter import messagebox

import tkinterdnd2
from tkinterdnd2 import *

import glob
from os import path, makedirs
from PyPDF2 import PdfFileReader, PdfFileWriter


class Pdf:
    def __init__(self):
        self.vystup = "./OUT/"
        self.overit_strukturu(self.vystup)

    def overit_strukturu(self, vystup):
        """
        Ověří adresář pro výstup -> vytvoří ho
        """
        if not path.exists(vystup): 
            makedirs(vystup)



    def pdf_soubory_IN(self, vstup):
        """
        Načte z cesty pouze soubory PDF
        """
        vstup = vstup + "/"
        soubory_typu_pdf = glob.glob(path.join(vstup, "*.pdf"))
        opravene_cesty = []
        for soubor in soubory_typu_pdf:
            soubor = soubor.replace("\\", "/")
            opravene_cesty.append(soubor)
        return soubory_typu_pdf


    def sluc(self, seznam: list, vystup: str):
        sloucene_pdf = PdfFileWriter()

        for soubor in seznam:
            pdf = PdfFileReader(soubor)
            pocet_stranek = pdf.getNumPages() 
            for vsechny_stranky_pdf in range(pocet_stranek):
                sloucene_pdf.addPage(pdf.getPage(vsechny_stranky_pdf))
        output = vystup + "slouceno.pdf"
        with open(output, 'wb') as output_pdf:
            sloucene_pdf.write(output_pdf)

class PdfGUI(tk.Frame):
    def __init__(self, parent, pdf):
        super().__init__(parent)
        self.parent = parent
        self.pdf = pdf
        self.parent.title("Pyladies - sloučení PDF souborů")
        self.entry_width = 80
        self.vytvor_plochu()

    def vytvor_plochu(self):
        self.nadpis = tk.LabelFrame(root, text="Do bílého pole přetáhni složku se soubory.", font="Arial 12")
        self.nadpis.grid(row=1, column=0)
        self.mez = tk.Label(self.nadpis, text="")
        self.mez.grid(row=1, column=0)

        self.sloucit = tk.Button(self.nadpis, text="Součit PDF", command=self.sloucit_pdf, font="Arial 12", width=self.entry_width)
        self.sloucit.grid(row=2, column=0, sticky=W)
        
        self.entry_sv = tk.StringVar()
        self.pole_Entry = tk.Entry(self.nadpis,textvar=self.entry_sv, width=self.entry_width, font="Arial 12")
        self.pole_Entry.grid(row=3, column=0)
 
        self.pole_Entry.drop_target_register(DND_FILES)
        self.pole_Entry.dnd_bind('<<Drop>>', self.drop)
        


    def sloucit_pdf(self):
        soubory = self.pole_Entry.get()
        soubory = pdf.pdf_soubory_IN(soubory)
        pdf.sluc(soubory, self.pdf.vystup)
        self.entry_sv.set("")
        messagebox.showwarning("HOTOVO", "Ve složce OUT najdeš sloučený PDF soubor")

    def drop(self, event):
        self.data = event.data.replace("}", "").replace("{", "")
        self.entry_sv.set(self.data)

if __name__ == '__main__':
    root = tkinterdnd2.Tk()
    pdf = Pdf()
    app = PdfGUI(root, pdf)
    app.mainloop()