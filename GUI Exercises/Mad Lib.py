# Mad Lib
# Tworzy opowiadanie oparte na szczegółach wprowadzonych przez uzytkownika

from tkinter import *

class Application(Frame):
    """Aplikacja oparta na GUI która tworzy opowiadanie
    na podstawie informacji wprowadzonych przez użytkownika
    """
    def __init__(self, master):
        """Inicjalizuj ramke"""
        super(Application,self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Tworzy widgety potrzebne do ramki"""
        # utwórz etykiete z instrukcją
        Label(self,
              text = "Wprowadz informacje do nowego opowiadania",
              ).grid(row = 0, column = 0, columnspan =2, sticky = W)

        # utwórz etykiete i pole znakowe służąace do wpisania imienia osoby
        Label(self,
              text = "Osoba: ",
              ).grid(row = 1, column = 0, sticky = W)
        self.person_entry = Entry(self)
        self.person_entry.grid(row = 1, column = 1, sticky = W)

        # utwórz etykiete i pole znakowe słuzące do wpisania rzeczownika w liczbie mnogiej
        Label(self,
              text = "Podaj rzeczownik w liczbie mnogiej:",
              ).grid(row = 2, column = 0, sticky = W)
        self.noun_entry = Entry(self)
        self.noun_entry.grid(row = 2, column = 1, sticky = W)

        #utwóz etykiete i pole znakowe do wpisania czasownika
        Label(self,
              text = "Podaj czasownik",
              ).grid(row = 3 , column = 0, sticky = W)
        self.verb_entry = Entry(self)
        self.verb_entry.grid(row =3 , column = 1, sticky = W)

        #utwórz etykiete do pół wyboru przemiotników
        Label(self,
              text = "Przymiotniki:",
              ).grid(row = 4, column = 0, sticky = W)
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text = "naglace",
                    variable = self.is_itchy
                    ).grid(row = 4, column = 1, sticky = W)

        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text = "elektryzujace",
                    variable = self.is_electric
                    ).grid(row = 4, column = 2, sticky = W)

        self.is_joyus = BooleanVar()
        Checkbutton(self,
                    text = "radosne",
                    variable = self.is_joyus
                    ).grid(row = 4, column = 3, sticky = W)

        Label(self,
              text = "Czesci ciala:",
              ).grid(row = 5, column = 0, sticky = W)
        self.body_part = StringVar()
        self.body_part.set(None)
        body_parts = ["pepek","noga","nerka"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row = 5, column = column, sticky = W)
            column += 1

        # przycisk akceptacji danych
        Button(self,
               text = "Kliknij aby wyświetlic opowiadanie",
               command = self.tell_story
               ).grid(row = 6, column = 0, sticky = W)
        self.story_text = Text(self, width = 75, height = 10, wrap = WORD)
        self.story_text.grid(row = 7, column = 0, sticky = W)

    def tell_story(self):
        """Wpisz w pole tekstowe opowiadanie oparte na danych uzyttkownika"""
        # pobierz wartosci interfejsu gui
        person = self.person_entry.get()
        noun = self.noun_entry.get()
        verb = self.verb_entry.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "naglące"
        if self.is_joyus.get():
            adjectives += "radosne"
        if self.is_electric.get():
            adjectives += "elektryzujace"

        body_part = self.body_part.get()

        # create the story
        story = "Uzytkownik tego programu"
        story += person
        story += "chciał nauczyc się programowania"
        story += "jest on"
        story += noun
        story += adjectives
        story += verb
        story += body_part + "."

        self.story_text.delete(0.0, END)
        self.story_text.insert(0.0, story)

root = Tk()
root.title("Mad Lib")
app = Application(root)
root.mainloop()


