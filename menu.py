from tkinter import *
from grille import Grille
from options import Options
from levels import Level
from config import *


class Menu:
    def __init__(self, window):
        self.window = window  # la fenetre dans laquelle est le menu

        self.load_menu()

# region Gestion frame
    # créer une frame
    def create_frame(self):
        self.frame = Frame(self.window, bg='forestgreen')

    # empaquetage d'une frame
    def pack_frame(self):
        self.frame.pack(expand=YES, side="top")
    # endregion

# region Chargement et création des composants
    # affiche le menu
    def load_menu(self):
        self.create_frame()
        self.create_menu()
        self.pack_frame()  # affiche la frame/le menu

    # affiche les options
    def load_option(self):
        # recréer/efface une frame si il y en a deja une, en créer une sinon
        self.frame.destroy()

        self.lvl = Options(self.window, self)

    # affiche les options
    def load_lvl(self):
        # recréer/efface une frame si il y en a deja une, en créer une sinon
        self.frame.destroy()

        self.option = Level(self.window, self)

    # créer les widget du menu
    def create_menu(self):
        self.title()
        self.btn_jouer()
        self.btn_opt()
        self.btn_lvl()
        self.btn_quitter()

    # charge une grille selon une option ou aleatoirement
    def create_grid(self):
        self.frame.destroy()

        cfg = getConfig()
        if cfg != "None":
            self.grille = Grille(self.window, self, cfg)  # charge une config

        else:
            # self.grille = Grille(self.window) #grille aléatoire
            print("Pas encore Implémenter")

# endregion

# region widgets
    def title(self):  # liste et création des widgets utilisé
        label_title = Label(self.frame, text="SUGURU", font=(
            "Courrier", 40), bg='forestgreen', fg='#563535')
        label_title.pack()

    def btn_opt(self):
        btn_opt = Button(self.frame, text="Grilles", font=(
            "Courrier", 25), fg='#b62546', command=self.load_option)
        btn_opt.pack(pady=25, padx=10, fill='both')

    def btn_lvl(self):
        btn_lvl = Button(self.frame, text="Niveaux", font=(
            "Courrier", 25), fg='#b62546', command=self.load_lvl)
        btn_lvl.pack(pady=25, padx=10, fill='both')

    def btn_jouer(self):
        btn_jouer = Button(self.frame, text="Jouer", font=(
            "Courrier", 25), fg='#b62546', command=self.create_grid)
        btn_jouer.pack(pady=25, padx=10, fill='both')

    def btn_quitter(self):
        btn_quit = Button(self.frame, text="Quitter", font=(
            "Courrier", 25), fg='#b62546', command=self.window.quit)
        btn_quit.pack(pady=25, padx=10, fill='both')

    def btn_retour(self):
        self.btn_back = Button(self.window, text="Menu", font=(
            "Courrier", 20), fg='#b62546', command=self.load_menu)
        self.btn_back.place(x=5, y=5, width=80, height=40)
