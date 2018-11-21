from tkinter import *

class Application(Frame):
    """Aplikacja GUI"""
    def __init__(self, master):
        """inicjalizuj ramke"""
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Tworzy widgety w ramce"""
        # Utwórz etykiete z opisem
        Label(self,
              text = "Wybiersz swój ulubiony gatunek filmu:",
              ).grid(row = 0, column = 0, sticky = W)
        # utwórz etykiete z opisem
        Label(self,
              text = "Wybierz jedną opcję:",
              ).grid(row = 1, column = 0, sticky = W)

        # zmienna która reprezentuje ulubiony gatunek filmu
        self.favorite = StringVar()
        self.favorite.set(None)

        # utwórz przycisk opcji
        Radiobutton(self,
                    text = "komedia",
                    variable = self.favorite,
                    value = "komedia.",
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

        Radiobutton(self,
                    text="dramat",
                    variable=self.favorite,
                    value="dramat.",
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)

        Radiobutton(self,
                    text="romans",
                    variable=self.favorite,
                    value="romans.",
                    command=self.update_text
                    ).grid(row=4, column=0, sticky=W)

        # pole tekstowe do wyników
        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row =5, column = 0, columnspan = 3)


    def update_text(self):
        """Zaktualizuj pole tekstowe"""
        message = "Twoim ulubionym gatunkiem filmowym jest "
        message += self.favorite.get()

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)


root = Tk()
root.title("Wybor filmów dwa")
app = Application(root)

root.mainloop()