# guess the number based on gui

from tkinter import *

class Application(Frame):
    """Aplikacja oparta na GUI w której użytkownik
    zgaduje nr wybrany przez komputer znajdujący się
    w danym przedziale liczb"""
    def __init__(self, master):
        """Inicjalizacja ramki"""
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Twórzy widgety użyte w aplikacji"""
        # etykieta z instrukcja
        Label(self,
              text = "Wprowadz liczbe z przedziału od 1 do 10",
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # etykieta pola i pole do wpisania liczby
        Label(self,
              text = "Liczba:",
              ).grid(row = 1, column = 0, sticky = W)
        self.number_entry = Entry(self)
        self.number_entry.grid(row =1, column =1, sticky = W)

        #przycisk zatwierdzajacy
        Button(self,
               text = "Zgadnij",
               command = self.check,
               ).grid(row =2, column = 0, sticky = W)
        self.answwer_text = Text(self, width = 20, height = 2, wrap = WORD)
        self.answwer_text.grid(row = 3, column = 0, sticky = W)

        # losowa liczba
        import random
        self.random_number = random.randint(1,5)


    def check(self):
        """Metoda sprawdzajaca odpowiedz"""
        if self.number_entry.get() > str(self.random_number):
            answer = "Liczba za duża"
        if self.number_entry.get() < str(self.random_number):
            answer = "Liczba za mała"
        if self.number_entry.get() == str(self.random_number):
            answer = "Liczba prawidlowa"

        # wpisywanie wyników do pola tekstowego
        self.answwer_text.delete(0.0, END)
        self.answwer_text.insert(0.0, answer)


# czesc glowna
root = Tk()
root.title("Guess the number")
app = Application(root)
root.mainloop()