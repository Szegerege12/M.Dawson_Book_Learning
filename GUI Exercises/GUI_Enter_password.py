from tkinter import *

class Application(Frame):
    """Aplikacja oparta na GUI z trzema przyciskami"""
    def __init__(self, master):
        """Inicjalizuj ramkę"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Utwórz widżety typu Button, Text i Entry"""
        self.inst_lbl = Label(self, text = "Wprowadz hasło")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.pw_lbl = Label(self, text = "Hasło:")
        self.pw_lbl.grid(row = 1, column = 0 , sticky = W)
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 1, column = 1, sticky = W)
        # przycisk akceptuj
        self.submit_button = Button(self, text = "Akceptuj", command = self.reveal)
        self.submit_button.grid(row = 2, column = 0, sticky = W)
        # widzet text do wyswietlania komunikatu
        self.secret_text = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_text.grid(row = 3, column = 0, columnspan = 2, sticky = W)


    def reveal(self):
        """Wyświetl kominukat zależny od poprawności hasła"""
        contenst = self.pw_ent.get()
        if contenst == "sektet":
            message = "Podane hasło jest prawidłowe"
        else:
            message = "Podane hasło jest nieprawidłowe"

        self.secret_text.delete(0.0, END)
        self.secret_text.insert(0.0, message)

# czesc głowna
root = Tk()
root.title("Program z hasłem")
root.geometry("300x150")

app = Application(root)

root.mainloop()