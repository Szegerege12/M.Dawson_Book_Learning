# Wybór filmów
# Demonstruje pola wyboru

from tkinter import *

class Application(Frame):
    """Aplikacja gui słuząca do wybóru gatunku filmów."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Wybierz swoje ulubione gatunki filmów."
              ).grid(row = 0, column = 0, sticky = W)

        Label(self,
              text = "Zaznacz wszystkie które chciałbyś wybrać:"
              ).grid(row = 1, column = 0, sticky = W)

        self.likes_comedy = BooleanVar()
        Checkbutton(self,
                    text = "Komedia",
                    variable = self.likes_comedy,
                    command = self.update_text
                    ).grid(row = 2, column = 0, sticky = W)

        self.likes_drama = BooleanVar()
        Checkbutton(self,
                    text = "Dramat",
                    variable = self.likes_drama,
                    command = self.update_text
                    ).grid(row = 3, column = 0, sticky = W)

        self.likes_romance = BooleanVar()
        Checkbutton(self,
                    text = "Romans",
                    variable = self.likes_romance,
                    command = self.update_text
                    ).grid(row = 4, column = 0, sticky = W)

        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)


    def update_text(self):
        """aktualizuje checkbutton"""
        likes = ""

        if self.likes_comedy.get():
            likes += "Lubisz komedie.\n"

        if self.likes_drama.get():
            likes += "Lubisz Dramaty.\n"

        if self.likes_romance.get():
            likes += "Lubisz romanse.\n"

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)


root = Tk()
root.title("Wybór filmów")
app = Application(root)
root.mainloop()