from tkinter import *
from rdb import Rdb


class Level:
    def __init__(self, window, menu):
        self.window = window  # la fenetre dans laquelle seront afficher les options
        self.rdb_list = []  # liste des radiobutton
        self.menu = menu

        self.frame = Frame()
        self.frame.pack(expand=YES, side=TOP)

        # par default, on affiche les options
        self.load_lvl()

    # charge l'affichage des option

    def load_lvl(self):
        self.label_title()
        self.btn_retour()
        self.create_rdBtn_group()

    # créer un groupe de radiobouton
    def create_rdBtn_group(self):
        # on precharge les radiobutton
        file = open("config.cfg", "r")
        lines = file.readlines()
        file.close()
        length = len(lines)

        # on créer un radiobutton pour la generation automatique
        k = 1  # correspond au numero du radiobutton créer
        for i in range(length):  # pour chaque lignes
            # si la ligne comence par cfg
            if lines[i][0:3] == "lvl":
                # on créer un radiobutton
                self.create_radioBtn("Niveau "+str(k), "lvl"+str(k))
                k += 1

        # on definit le bouton selectionné
        file = open("opt.cfg", "r")

        for line in file:
            # coupe la chaine de caractere en deux
            if line[0] != "#" and line.split("=")[0] == "level":
                lvl = line.split("=")[1].rstrip()
                for x in self.rdb_list:
                    if x.lvl == lvl:
                        x.select()
        file.close()

    # créer un radiobouton

    def create_radioBtn(self, name, lvl):
        # sur click appele la fonction write_opt_lvl() qui réécrit le fichier opt.cfg avec la nouvelle config
        rdb = Rdb(name, None, lvl, self.frame)

        self.rdb_list.append(rdb)  # on l'ajoute dans la liste des radiobutton

    # affiche le titre

    def label_title(self):
        label_title = Label(self.frame, text="NIVEAUX",
                            font=("Courrier", 40), fg='#563535')
        label_title.pack(anchor=N)

    # recharge le menu
    def btn_retour(self):
        self.btn_back = Button(self.window, text="Grilles", font=(
            "Courrier", 20), fg='#b62546', command=self.load_menu)
        self.btn_back.place(relx=0.5, rely=0.9, width=200, height=40, anchor=CENTER)


    def load_menu(self):
        self.btn_back.destroy()
        self.frame.destroy()
        self.menu.load_option()
