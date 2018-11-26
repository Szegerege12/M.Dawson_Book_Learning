# Program słuzacy do realizacji zamowien w restauracji
# Oparty na GUI

from tkinter import *

class Application(Frame):
    """Aplikacja oparta na GUI która wyświetla
    menu restauracji oraz pozwala na złożenie
    zamówienia przez uzytkownika"""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Tworzy widzety do ramki"""
        Label(self,
              text = "Przyjmnowanie zamowien restauracja XXX",
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)
        Label(self,
              text = "Danie",
              ).grid(row = 1, column = 0, sticky = W)
        Label(self,
              text = "Cena",
              ).grid(row = 1, column = 1, sticky = W)

        products = ["stek","pizza","kebab","kurczak","kawa","herbata"]
        row  = 2
        for product in products:
            Label(self,
                  text = product,
                  ).grid(row = row, column = 0, sticky = W)
            row += 1

        prices = [12,16,10,8,4,4]
        self.price_1 = IntVar()
        Checkbutton(self,
                    text = "12",
                    variable = self.price_1,
                    onvalue = 12
                    ).grid(row =2, column = 1, sticky = W)

        self.price_2 = IntVar()
        Checkbutton(self,
                    text="16",
                    variable=self.price_2,
                    onvalue=12
                    ).grid(row=3, column=1, sticky=W)

        self.price_3 = IntVar()
        Checkbutton(self,
                    text="10",
                    variable=self.price_3,
                    onvalue=10
                    ).grid(row=4, column=1, sticky=W)

        self.price_4 = IntVar()
        Checkbutton(self,
                    text="8",
                    variable=self.price_4,
                    onvalue=8
                    ).grid(row=5, column=1, sticky=W)

        self.price_5 = IntVar()
        Checkbutton(self,
                    text="4",
                    variable=self.price_5,
                    onvalue=4
                    ).grid(row=6, column=1, sticky=W)

        self.price_6 = IntVar()
        Checkbutton(self,
                    text="4",
                    variable=self.price_6,
                    onvalue=4
                    ).grid(row=7, column=1, sticky=W)


        Button(self,
               text = "Złóż zamówienie",
               command = self.place_order
               ).grid(row =8, column = 0, sticky = W)
        self.order_text = Text(self, width = 5, height = 1, wrap = WORD)
        self.order_text.grid(row = 9, column = 1,  sticky = W)
        Label(self,
              text = "Koszt Twojego zamówienia to:",
              ).grid(row =9, column = 0, sticky = W)

    def place_order(self):
        """Zsumuj ceny i wyswietl rachunek"""
        price = 0
        if self.price_1.get():
            price += 12
        if self.price_2.get():
            price += 16
        if self.price_3.get():
            price += 10
        if self.price_4.get():
            price += 8
        if self.price_5.get():
            price += 4
        if self.price_6.get():
            price += 4


        self.order_text.delete(0.0, END)
        self.order_text.insert(0.0, str(price) +str("zł"))




root = Tk()
root.title("Zamow produkty")
app = Application(root)
root.mainloop()