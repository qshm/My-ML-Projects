import tkinter as tk
import datetime as dt
from tkcalendar import Calendar, DateEntry
import re
import pandas as pd
from fpdf import FPDF


r = re.compile(r"^(?=.*?\d)\d*[.]?\d*$")

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Pilates Invoice Manager")

        tk.Label(text="Pick month of invoice (any day):").grid(row=0, column=0, sticky="E")

        # INITIATE DICTIONARY TO KEEP HOURS WORKED
        self.allentries = dict()


        self.cal = DateEntry(master, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern="dd/mm/yyyy")
        self.cal.set_date(dt.datetime.now())
        self.cal.grid(row=0, column=1, sticky="W")

        tk.Label(text="Day rate in £ (ex: 30.00) :").grid(row=1, column=0, sticky="E")

        # GET WEEKDAY AND WEEKEND RATES
        self.default_rate = 30
        self.default_rate_setter = tk.StringVar()
        self.default_rate_setter.set(str(self.default_rate))


        self.weekendrate = tk.Entry(textvariable=self.default_rate_setter)
        self.weekendrate.grid(row=1, column=1, sticky="W")
        # self.weekendrate.bind('<Key-Return>', self.print_contents)

        # # DISPLAY CURRENT DATE
        # self.w = tk.Entry(master, fg="white", bg="black", font=("helvetica", 12))
        # self.w.insert(0,f"{dt.datetime.now():%a, %b %d %Y}")
        # self.w.grid(row=2, column=1, sticky="E")

        # checkbox for weekend only display
        self.CheckVar1 = tk.IntVar()
        self.C1 = tk.Checkbutton(master, command=self.check_status, text="Display only Sundays", variable=self.CheckVar1, onvalue=1, offvalue=0)
        self.C1.grid(row=2, columnspan=2)

        # self.weekendmessage = tk.Label(text="All days will be displayed")
        # self.weekendmessage.grid(row=2, column=1, sticky="W")

        tk.Label(text="Enter number of hours worked: ").grid(row=3, columnspan=2)

        self.check_status()


        tk.Button(text ="Save", command = self.savetotals).grid()

        tk.Button(text="Export to PDF", command=self.export_topdf).grid()

        # self.contents = tk.StringVar()
        # OPTIONS = ["egg", "bunny", "chicken"]
        # self.contents.set(OPTIONS[0])  # default value
        # self.w = tk.OptionMenu(master, self.contents, *OPTIONS)
        # self.w.pack()

    def export_topdf(self):
        # pd.DataFrame.from_dict(data=self.allentries, orient='index').to_csv('dict_file.csv', header=False)

        # save FPDF() class into a
        # variable pdf
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size=15)

        pdf.rect(5.0, 5.0, 200.0,287.0)

        # create a cell
        pdf.cell(200, 10, txt="Eleni Theodoridou Pilates",
                 ln=1, align='C')

        invoice_month = self.cal.get_date().strftime("%B")

        # add another cell
        pdf.cell(200, 10, txt=f"Invoice for {invoice_month} {self.cal.get_date().year}",
                 ln=2, align='C')

        pdf.set_font("times", size=10)
        pdf.cell(75, 10, txt=f"Bill to:", border=0, ln=0, align='L')
        pdf.cell(75, 10, txt=f"Pepilates Limited", border=0, ln=1, align='L')
        pdf.cell(75, 10, txt=f"Date:", border=0, ln=0, align='L')
        pdf.cell(75, 10, txt=f"{dt.datetime.now():%d %b %Y}", border=0, ln=1, align='L')


        pdf.set_font("Arial", size=10)


        for day, entry in self.allentries.items():
            if entry > 0:
                pdf.cell(100, 10, txt=f"{day}", border = 1, ln=0, align='L')
                pdf.cell(50, 10, txt=f"£ {entry}", border = 1, ln=1, align='L')


        monthly_total = sum(self.allentries.values())
        pdf.cell(100, 10, txt=f"Monthly Total", border=1, ln=0, align='L')
        pdf.cell(50, 10, txt=f"£ {monthly_total}", border=1, ln=1, align='L')

        pdf.ln(5)
        pdf.cell(150, 10, txt=f"Please make payment to:", border=0, ln=1, align='L')
        pdf.cell(50, 10, txt=f"Account Name", border=0, ln=0, align='L')
        pdf.cell(50, 10, txt=f"Eleni Theodoridou", border=0, ln=1, align='L')
        pdf.cell(50, 10, txt=f"Bank", border=0, ln=0, align='L')
        pdf.cell(50, 10, txt=f"Lloyds Bank", border=0, ln=1, align='L')
        pdf.cell(50, 10, txt=f"Sort Code", border=0, ln=0, align='L')
        pdf.cell(50, 10, txt=f"30-94-21", border=0, ln=1, align='L')
        pdf.cell(50, 10, txt=f"Account No", border=0, ln=0, align='L')
        pdf.cell(50, 10, txt=f"32455260", border=0, ln=1, align='L')

        # save the pdf with name .pdf
        pdf.output(f"Invoice_{invoice_month}{self.cal.get_date().year}.pdf")


    def savetotals(self):

        self.default_rate = float(self.default_rate_setter.get())

        self.allentries = dict((day.cget("text"), float(entry.get()) * self.default_rate ) if r.match(entry.get()) else
               (day.cget("text"), 0 ) for day, entry in alldays)

        self.monthly_total = sum(self.allentries.values())

        print(self.monthly_total)

    def find_weekends(self, Sundayonly = False):
        year = self.cal.get_date().year
        month = self.cal.get_date().month
        first_day_of_month = dt.date(year,month,1)
        first_saturday_of_month = first_day_of_month + dt.timedelta(days=5 - first_day_of_month.weekday())
        first_sunday_of_month = first_saturday_of_month + dt.timedelta(days=1)

        if Sundayonly:
            while first_sunday_of_month.year == year and first_sunday_of_month.month == month:
                yield first_sunday_of_month
                first_sunday_of_month += dt.timedelta(days=7)

        else:
            while first_day_of_month.year == year and first_day_of_month.month == month:
                yield first_day_of_month
                first_day_of_month += dt.timedelta(days=1)


    def check_status(self):
        Sundayonly = bool(self.CheckVar1.get())
        global alldays

        if not Sundayonly:
            alldays = [(tk.Label(text=f"{d}"), tk.Entry()) for d in self.find_weekends(Sundayonly=False)]

            row = 4
            for label, entry in alldays:
                label.grid_remove()
                entry.grid_remove()
                label.grid(row=row, column=0, sticky="E")
                entry.grid(row=row, column=1, sticky="W")
                row += 1

        elif Sundayonly:
            for label, entry in alldays:
                label.grid_remove()
                entry.grid_remove()

            alldays = [(tk.Label(text=f"{d}"), tk.Entry()) for d in self.find_weekends(Sundayonly=True)]
            row = 4
            for label, entry in alldays:
                label.grid(row=row, column=0, sticky="E")
                entry.grid(row=row, column=1, sticky="W")
                row += 1





    def print_contents(self, event):
        x = float(self.weekendrate.get().partition(" ")[0])
        print("Hi. The current entry content and type are:",
              x, type(x))

root = tk.Tk()
myapp = App(root)
# root.geometry(('600x700+200+100'))


myapp.mainloop()