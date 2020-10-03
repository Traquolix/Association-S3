from OrderFormGUI import *
from locals import *

class EventHandler:

    window = ""
    fields = []

    def __init__(self, window, fields):
        self.window = window
        self.fieldss = fields

    def click_into_calendar(event):
        top = tk.Toplevel(event.window)

        ttk.Label(top, text='Choisir la date').pack(padx=10, pady=10)

        cal = DateEntry(top, width=12, background='darkblue',
                        foreground='white', borderwidth=2, format="%d/%m/%Y")
        cal.format_date = "%d/%m/%Y"
        cal.pack(padx=10, pady=10)
