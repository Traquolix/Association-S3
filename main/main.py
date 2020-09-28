from personnal_utils.utils import *
import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import date

from tkcalendar import DateEntry


window = Tk()
window.title("Welcome to TutorialsPoint")
window.geometry('400x400')
window.configure(background="white")


# -----------------

def click_into_calendar(event):
    top = tk.Toplevel(window)

    ttk.Label(top, text='Choisir la date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2, format="%d/%m/%Y")
    cal.format_date = "%d/%m/%Y"
    cal.pack(padx=10, pady=10)

def clicked():
    print("cc")


# -----------------


a = Label(window, text="Numéro du bon de commande : ").grid(row=0, column=0)
b = Label(window, text="Nom du destinataire : ").grid(row=1, column=0)
c = Label(window, text="Adresse du destinataire").grid(row=2, column=0)
d = Label(window, text="Date du jour").grid(row=3, column=0)
a1 = Entry(window).grid(row=0, column=1)
b1 = Entry(window).grid(row=1, column=1)
c1 = Entry(window).grid(row=2, column=1)


d1 = DateEntry(window, locale='fr_FR', date_pattern='dd/mm/y', width=12, background='grey',
               foreground='white', borderwidth=2)
# d1.insert(0, date.today().strftime("%d/%m/%Y"))
# d1.bind("<1>", click_into_calendar)
d1.grid(row=3, column=1)





# btn = ttk.Button(window, text="Submit", command=clicked).grid(row=4, column=1)


window.mainloop()
"""



def calendar():
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)


root = tk.Tk()
s = ttk.Style(root)
s.theme_use('clam')

ttk.Button(root, text='DateEntry', command=calendar).pack(padx=10, pady=10)

root.mainloop()

"""