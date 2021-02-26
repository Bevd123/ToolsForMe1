import tkinter as tk
import os
import pygetwindow as gw

root = tk.Tk()

root.geometry("480x480")

eingabefeld_wert = tk.StringVar()
eingabefeld = tk.Entry(root, textvariable=eingabefeld_wert)

def open1():
    os.system("start C:/Users/Raphi/PycharmProjects/Hub/UnterProgramme/SkaatKarten.py")
    exit()

def open2():
    os.system("/Users/Raphi/PycharmProjects/Hub/UnterProgramme/test.py")
    exit()


schaltf1 = tk.Button(root, text="Öffne Skat-Karten", command=open1)
schaltf1.grid(row=2, column=1)
schaltf2 = tk.Button(root, text="Öffne Datenlöscher", command=open2)
schaltf2.grid(row=1, column=3)


root.mainloop()
