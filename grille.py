from tkinter import *
from case import Case
from group import Group
from errors import *
from tools import *
from config import *


class Grille:
    # constructeur grille a partir d'un fichier de config

    def __init__(self, window, menu, cfg):
        # attributs
        self.menu = menu
        self.__window = window  # fenetre dans laquelle est la grille
        self.__n = 0  # Nombre de lignes
        self.__m = 0  # Nombre de colonnes
        self.__solved = False  # Bloque la grille quand on gagne
        self.__selected = None  # case selectionnée
        self.__matrice = []  # matrices des cases
        self.__list_group = []  # liste des groupe
        self.__listError = listErrors()

        self.create_frame()

        self.btn_retour()  # pour retourner au menu
        self.btn_regles()  # affiche les règles
        self.btn_solve()  # boutton pour résoudre la grille
        self.btn_solveInt()  # boutton pour résoudre la grille Int
        self.btn_Save()  # boutton pour résoudre la grille Int

        self.popup_load(cfg)

        self.pack_frame()  # l'affiche

# region Chargement de la config / sauvegarde
    def popup_load(self, cfg):
        self.frame_load = Frame(width=100, height=40, bg="#ecffd7")
        self.frame_load.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.btn_yes = Button(self.frame_load, text = "Continuer", font = ("Courrier", 20), fg = '#b62546', command = self.load)
        self.btn_yes.grid(row=0, column=0)
        self.btn_no = Button(self.frame_load, text = "Nouvelle", font = ("Courrier", 20), fg = '#b62546', command = lambda : self.load_config(cfg))
        self.btn_no.grid(row=0, column=1)


    def btn_Save(self):
           self.btn_save = Button(self.__window, text = "Save", font = ("Courrier", 20), fg = '#b62546', command = self.save)
           self.btn_save.place(relx = 0.862, y = 65, width = 100, height = 40, anchor = CENTER)

    def save(self):
        if not self.__solved:
            grille = ""
            for i in range(self.__n) :
                sgrid = ""
                for j in range(self.__m) :
                    case = self.__matrice[i][j]
                    num = case.getNum()
                    if num == "":
                        num = 0
                    grp = case.getGrp().getNom()
                    grp = grp[6:] # enleve "groupe" au debut du nom du groupe
                    sgrid += "{}:{}:{}, ".format(num, grp, case.getEstModif())
                grille += sgrid + "\n"

            file = open("save.txt", "w")
            file.write(grille)
            file.close()
        else: #sinon on ecrit rien
            file = open("save.txt", "w")
            file.write("")
            file.close()


    def load(self):
        file = open("save.txt", "r")
        grille = file.readlines()
        file.close()
        if grille == []: # rien n'est sauvegarder
            return

        for i in range(len(grille)):
            grille[i] = grille[i].strip()

        grid = []
        for i in range(len(grille)):
            sgrid = []
            truc = None
            truc = grille[i].split(",")
            del truc[-1] #le dernier element est '', on le supprime
            machin = None
            for j in range(len(truc)):
                machin = truc[j].split(":")
                machin[0] = int(machin[0])
                machin[1] = int(machin[1])
                machin[2] = True if machin[2] == 'True' else False
                sgrid.append(machin)
            grid.append(sgrid)

        print("grille (précédement sauvegardée) chargée : ")
        affiche1dim(grid)
        self.__n = len(grid)
        self.__m = len(grid[0])

        for i in range(self.__n) :
            sgrid = []  # initialise une ligne
            for j in range(self.__m) :
                num = grid[i][j][0]  # chifre de la case
                numGrp = grid[i][j][1]  # numero du groupe
                estModif = grid[i][j][2] # si la case est modifiable ou non

                if num == 0:
                    num = ""

                # creation de la case
                case = Case(self.__frame, "btn{}{}".format(i, j), num, estModif, i, j, self)

                # placement de la case
                case.canvas.grid(row = i, column = j)

                # on ajoute la case dans la ligne
                sgrid.append(case)

                # on met la case dans son groupe
                self.addInGroup(case, numGrp)

            self.__matrice.append(sgrid)
            # ajout de la ligne dans la grille

        self.__max = max(grp.getNbElem() for grp in self.__list_group)

        try:
            self.frame_load.destroy()
        except:
            pass

        self.drawGroups()
        self.load_down_pad()  # charge le pad pour entrer les chiffres dans la grille

        for i in range(self.__n):
            for j in range(self.__m):
                self.__selected = self.__matrice[i][j]
                self.checkErrors()


    # charge une grille a partir d'un fichier de config
    def load_config(self, cfg):
        self.frame_load.destroy()
        #print("grille chargée : ")
        #affiche1dim(cfg)

        # charge et place les widget (cases)
        self.create_config(cfg, len(cfg), len(cfg[0]))

        self.load_down_pad()  # charge le pad pour entrer les chiffres dans la grille
        self.drawGroups()

    # charge et place les widget dans la grille

    def create_config(self, grid, n, m):
        self.__n = n
        self.__m = m
        for i in range(self.__n):
            sgrid = []  # initialise une ligne
            for j in range(self.__m):
                num = grid[i][j][0]  # chifre de la case
                numGrp = grid[i][j][1]  # numero du groupe

                if num > 0:
                    # on est dans une config précréer, alors on ne veut pas modifier les case qui on un numero
                    estModifiable = False
                else:
                    estModifiable = True
                    num = ""  # pas de numero pour les autres cases

                # creation de la case
                case = Case(self.__frame, "btn{}{}".format(i, j), num, estModifiable, i, j, self)

                # placement de la case
                case.canvas.grid(row=i, column=j)

                # on ajoute la case dans la ligne
                sgrid.append(case)

                # on met la case dans son groupe
                self.addInGroup(case, numGrp)

            self.__matrice.append(sgrid)
            # ajout de la ligne dans la grille
        self.__max = max(grp.getNbElem() for grp in self.__list_group)
# endregion

# region Gestion groupes
    # ajoute une case dans un groupe1
    def addInGroup(self, case, numGrp):
        nom = "groupe{}".format(numGrp)

        # si le groupe existe deja, ajoute la case dedans
        for x in self.__list_group:
            if x.getNom() == nom:
                x.ajout(case)
                case.setGrp(x)
                return  # arrete la fonction

        # crée un groupe, y ajoute la case et l'ajoute dans la liste des groupes
        grp = Group(nom)
        grp.ajout(case)
        case.setGrp(grp)
        self.__list_group.append(grp)

    # Dessine les bordure des groupes

    def drawGroups(self):
        for i in range(self.__n):
            for j in range(self.__m):
                # definit les border de la case
                if i+1 < self.__n:  # si on est dans la grille on fait le test
                    if self.__matrice[i][j].getGrp() == self.__matrice[i+1][j].getGrp():
                        self.__matrice[i][j].setBdb(0)

                if i-1 >= 0:  # si on est dans la grille
                    if self.__matrice[i][j].getGrp() == self.__matrice[i-1][j].getGrp():
                        self.__matrice[i][j].setBdt(0)

                if j+1 < self.__m:  # si on est dans la grille
                    if self.__matrice[i][j].getGrp() == self.__matrice[i][j+1].getGrp():
                        self.__matrice[i][j].setBdr(0)

                if j-1 >= 0:  # si on est dans la grille
                    if self.__matrice[i][j].getGrp() == self.__matrice[i][j-1].getGrp():
                        self.__matrice[i][j].setBdl(0)

                # dessine les border comme selectionné ci dessus
                self.__matrice[i][j].drawBorder()
    # endregion

# region Gestion des erreur
    # cherche des erreurs autour de la cae selectionnée
    def checkErrors(self):
        # position de la case selectionnée dans la matrice, sert a  trouver facilement les cases adjascentes
        # et ainsi la case matrice[i][j] est la meme que la case selected, ce qui m'a donné moins de travail
        # quand j'ai changer de facon de gérer les erreurs
        i = self.__selected.getI()
        j = self.__selected.getJ()

        # supprime les erreurs d'adjascences du numero de la case selectionnée (il peut y en avoir plusieurs)
        # en gros actualise la liste des erreurs d'adjascence
        self.__listError.deleteAdjError(self.__selected)
        self.__listError.deleteOutErr(self.__matrice[i][j])

        # pour les cases cote a cote
        # teste les 8 case a coté de celle selectionnée et les colore si elles ont le meme numero
        if self.__matrice[i][j].getNum() != "":
            if i+1 < self.__n:
                if self.__matrice[i][j].getNum() == self.__matrice[i+1][j].getNum():
                    self.__listError.createError(
                        self.__selected, self.__matrice[i+1][j])

            if j+1 < self.__m:
                if self.__matrice[i][j].getNum() == self.__matrice[i][j+1].getNum():
                    self.__listError.createError(
                        self.__matrice[i][j], self.__matrice[i][j+1])

            if i-1 >= 0:
                if self.__matrice[i][j].getNum() == self.__matrice[i-1][j].getNum():
                    self.__listError.createError(
                        self.__matrice[i][j], self.__matrice[i-1][j])

            if j-1 >= 0:
                if self.__matrice[i][j].getNum() == self.__matrice[i][j-1].getNum():
                    self.__listError.createError(
                        self.__matrice[i][j], self.__matrice[i][j-1])

            # pour les diagonales
            if i+1 < self.__n and j+1 < self.__m:
                if self.__matrice[i][j].getNum() == self.__matrice[i+1][j+1].getNum():
                    self.__listError.createError(
                        self.__matrice[i][j], self.__matrice[i+1][j+1])

            if i+1 < self.__n and j-1 >= 0:
                if self.__matrice[i][j].getNum() == self.__matrice[i+1][j-1].getNum():
                    self.__listError.createError(
                        self.__matrice[i][j], self.__matrice[i+1][j-1])

            if i-1 >= 0 and j+1 < self.__m:
                if self.__matrice[i][j].getNum() == self.__matrice[i-1][j+1].getNum():
                    self.__listError.createError(
                        self.__matrice[i][j], self.__matrice[i-1][j+1])

            if i-1 >= 0 and j-1 >= 0:
                if self.__matrice[i][j].getNum() == self.__matrice[i-1][j-1].getNum():
                    self.__listError.createError(
                        self.__matrice[i][j], self.__matrice[i-1][j-1])

            # si le numero entré dépasse le max du groupe, et si il n'y a aucune autre erreur (elles ont la priorité)
            if(self.__selected.getErr() == False and int(self.__selected.getNum()) > self.__selected.getGrp().getNbElem()):
                self.__listError.createError(self.__matrice[i][j], "")

        # pour les groupes
        # les groupes ne contiennent que des cases avec des numeros,
        # donc si la case selectionnée n'en a pas nous ne testons pas les erreurs de groupe car il n'y aurais aucune correspondance des numéros
        grp = self.__selected.getGrp()  # le groupe dans lequel est la case selectionnée
        # cf definition de isGroupError
        caseErr = grp.isGroupError(self.__selected)

        # si il y a des erreur dans caseErr, créer une erreur si elle n'existe pas, sinon nettoie tout le groupe des erreur en lien avec la case selectionnée
        if len(caseErr) > 0 and self.__selected.getNum() != "":
            for err in caseErr:
                self.__listError.createError(
                    self.__matrice[i][j], err, grp.getNom())
        else:
            self.__listError.deleteGrpError(self.__selected, grp.getNom())

    # endregion

# region Victoire
    # renvoie True si la victoire est acquise et dessine un gros VCTOIRE

    def victory(self):
        # si le grille est remplie et qu'il n'y a pas d'erreur : on gagne
        if(self.__listError.getNb() == 0 and self.remplie()):
            self.create_label_victory()
            self.__solved = True
        else:
            return False

    # renvoie vraie si toutes les cases sont remplies par un chiffre
    def remplie(self):
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__matrice[i][j].getNum() == "":
                    return False
        return True

    # le label affiché lors de la victiore

    def create_label_victory(self):
        self.fram_victory = Frame()
        Label(self.fram_victory, text="VICTOIRE",
              font=("Courrier", 40), fg="green").pack()
        self.fram_victory.place(relx=0.22, rely=0.4)

    # endregion

# region Algo Resolutions
    def btn_solve(self):
        self.btn_solve = Button(self.__window, text="Résoudre brute", font=(
            "Courrier", 20), fg='#b62546', command=self.solve)
        self.btn_solve.place(relx=0.5, y=25, width=200,
                             height=40, anchor=CENTER)

    def btn_solveInt(self):
        self.btn_solveInt = Button(self.__window, text="Résoudre Int", font=(
            "Courrier", 20), fg='#b62546', command=self.solveInt)
        self.btn_solveInt.place(
            relx=0.5, y=65, width=200, height=40, anchor=CENTER)

########################################################### Fonctions Resolution Int #####################################################################

    def Existe(self, x, y):
        if int(x) < 0 or int(x) > (int(self.__n)-1) or int(y) < 0 or int(y) > (int(self.__m)-1):
            return False
        return True

    # retourne la case en fonction de deux coordonnées
    def getCase(self, x, y):
        for ssg in self.__list_group:
            for case in ssg.getListe():
                if int(case.getI()) == int(x) and int(case.getJ()) == int(y):
                    return case

    # liste de cases voisines
    def casevoisine(self, case):
        x = int(case.getI())
        y = int(case.getJ())

        listecv = []

        if bool(self.Existe((x-1), (y-1))):
            listecv.append(self.getCase((x-1), (y-1)))

        if bool(self.Existe((x), (y-1))):
            listecv.append(self.getCase((x), (y-1)))

        if bool(self.Existe((x+1), (y-1))):
            listecv.append(self.getCase((x+1), (y-1)))

        if bool(self.Existe((x-1), (y))):
            listecv.append(self.getCase((x-1), (y)))

        if bool(self.Existe((x+1), (y))):
            listecv.append(self.getCase((x+1), (y)))

        if bool(self.Existe((x-1), (y+1))):
            listecv.append(self.getCase((x-1), (y+1)))

        if bool(self.Existe((x), (y+1))):
            listecv.append(self.getCase((x), (y+1)))

        if bool(self.Existe((x+1), (y+1))):
            listecv.append(self.getCase((x+1), (y+1)))

        return listecv

    # controle

    def controle(self):
        for ssg in self.__list_group:
            n = 0
            for case in ssg.getListe():
                self.setSelected(case)
                if self.__selected.getNum() == "":
                    if len(self.__selected.getPoss()) == 1:
                        self.__selected.changeVal(
                            int(self.__selected.getPoss()[0]))
                    else:
                        cv = self.casevoisine(self.__selected)
                        for caseg in ssg.getListe():
                            if self.__selected != caseg and (caseg not in cv):
                                cv.append(caseg)
                        for casev in cv:
                            if casev.getNum() != "":
                                if int(casev.getNum()) in self.__selected.getPoss():
                                    l = self.__selected.getPoss()
                                    l.remove(int(casev.getNum()))
                                    self.__selected.setPoss(l)

                else:
                    cv = self.casevoisine(self.__selected)
                    for caseg in ssg.getListe():
                        if caseg != self.__selected and caseg not in cv:
                            cv.append(caseg)
                    for casev in cv:
                        if int(self.__selected.getNum()) in casev.getPoss():
                            l = casev.getPoss()
                            l.remove(int(self.__selected.getNum()))
                            casev.setPoss(l)
                    n += 1
            if n == int(ssg.getNbElem()):
                ssg.setEtat(True)

    # Techiques de resoltion

    def fullblock(self, ssg):
        for case in ssg.getListe():
            self.setSelected(case)
            if self.__selected.getNum() == "" and len(self.__selected.getPoss()) == 1:
                self.__selected.changeVal(int(self.__selected.getPoss()[0]))

    def unique(self, ssg):
        for case in ssg.getListe():
            self.setSelected(case)
            if self.__selected.getNum() == "":
                for p in self.__selected.getPoss():
                    if int(ssg.nbpossLSG(p)) == 1:
                        self.__selected.setPoss([int(p)])
                        self.__selected.changeVal(int(p))
                        break

    def crown(self, ssg):
        for case in ssg.getListe():
            self.setSelected(case)
            if self.__selected.getNum() == "":
                cv = self.casevoisine(self.__selected)
                for caseg in ssg.getListe():
                    if caseg != self.__selected and (caseg not in cv):
                        cv.append(caseg)
                for c in cv:
                    if c.getNum() != "" and (int(c.getNum()) in self.__selected.getPoss()):
                        l = self.__selected.getPoss()
                        l.remove(int(c.getNum()))
                        self.__selected.setPoss(l)

    def Round234(self, ssg):
        for case in ssg.getListe():
            self.setSelected(case)
            if self.__selected.getNum() == "":
                for p in self.__selected.getPoss():
                    cv = self.casevoisine(self.__selected)
                    for cctr in cv:
                        if cctr in ssg.getListe():
                            cv.remove(cctr)
                    for c in cv:
                        voisine = []
                        pasvoisine = []
                        for v in c.getGrp().getListe():
                            if v in cv:
                                voisine.append(v)
                            else:
                                if p in v.getPoss():
                                    break
                                else:
                                    pasvoisine.append(v)
                        if len(voisine) > 1 and (int(len(voisine))+int(len(pasvoisine))) == int(c.getGrp().getNbElem()):
                            x = 0
                            for voi in voisine:
                                if p in voi.getPoss():
                                    x = x+1
                            if x > 1 and p in self.__selected.getPoss():
                                l = self.__selected.getPoss()
                                l.remove(int(p))
                                self.__selected.setPoss(l)

    def SimpleNakedPair(self, ssg):
        pair = []
        otr = []
        for case in ssg.getListe():
            if len(case.getPoss()) == 2:
                pair.append(case)
            else:
                otr.append(case)
        if len(pair) == 2 and int(pair[0].getPoss()[0]) == int(pair[1].getPoss()[0]) and int(pair[0].getPoss()[1]) == int(pair[1].getPoss()[1]):
            for case in otr:
                self.setSelected(case)
                if self.__selected.getNum() == "":
                    for p in self.__selected.getPoss():
                        if int(p) == int(pair[0].getPoss()[0]) or int(p) == int(pair[0].getPoss()[1]):
                            l = self.__selected.getPoss()
                            l.remove(int(p))
                            self.__selected.setPoss(l)

    def SimpleHiddenPair(self, ssg):
        for case in ssg.getListe():
            self.setSelected(case)
            pair = []
            numerospair = []
            if self.__selected.getNum() == "":
                for p in self.__selected.getPoss():
                    if int(ssg.nbpossLSG(p)) == 2 and p not in numerospair:
                        numerospair.append(p)
                if len(numerospair) == 2:
                    for casev in ssg.getListe():
                        if int(numerospair[0]) in casev.getPoss() and int(numerospair[1]) in casev.getPoss() and casev not in pair:
                            pair.append(casev)
                    if len(pair) == 2:
                        for c in pair:
                            for q in c.getPoss():
                                if q not in numerospair:
                                    l = c.getPoss()
                                    l.remove(int(q))
                                    c.setPoss(l)

    def NakedSingle(self, ssg):
        for case in ssg.getListe():
            self.setSelected(case)
            if len(self.__selected.getPoss()) == 1 and self.__selected.getNum() == "":
                self.__selected.changeVal(int(self.__selected.getPoss()[0]))

    def HiddenSingle(self, ssg):
        for i in range(1, int(ssg.getNbElem())+1):
            if int(ssg.nbpossLSG(int(i))) == 1:
                for case in ssg.getListe():
                    self.setSelected(case)
                    if self.__selected.getNum() == "":
                        if int(i) in self.__selected.getPoss():
                            self.__selected.changeVal(int(i))
                            self.__selected.setPoss([int(i)])

    def NakedPairB(self, ssg):
        for case in ssg.getListe():
            self.setSelected(case)
            if len(self.__selected.getPoss()) == 2 and self.__selected.getNum() == "":
                cv = self.casevoisine(self.__selected)
                for casev in cv:
                    if len(casev.getPoss()) == 2 and int(casev.getPoss()[0]) == int(self.__selected.getPoss()[0]) and int(casev.getPoss()[1]) == int(self.__selected.getPoss()[1]) and casev.getGrp() != self.__selected.getGrp():
                        cv2 = self.casevoisine(casev)
                        for v in cv:
                            if v != casev and v in cv2:
                                for p in v.getPoss():
                                    if int(p) in self.__selected.getPoss():
                                        l = v.getPoss()
                                        l.remove(int(p))
                                        v.setPoss(l)

    def SameValueCells(self, ssg):
        for case in ssg.getListe():
            if case.getNum() == "":
                cv = self.casevoisine(case)
                for w in cv:
                    if w.getGrp() == case.getGrp():
                        cv.remove(w)
                for casev in cv:
                    voisine = []
                    pasvoisine = []
                    for v in casev.getGrp().getListe():
                        if v in cv:
                            voisine.append(v)
                        else:
                            pasvoisine.append(v)
                    if (len(voisine)+len(pasvoisine)) == int(casev.getGrp().getNbElem()) and len(pasvoisine) == 1:
                        n = 0
                        for p in case.getPoss():
                            if p in pasvoisine[0].getPoss():
                                n += 1
                        if n == len(case.getPoss()):
                            pasvoisine[0].setPoss(case.getPoss())

    def XYWing(self, ssg):
        for case in ssg.getListe():
            self.setSelected(case)
            if len(self.__selected.getPoss()) == 2 and self.__selected.getNum() == "":
                cv = self.casevoisine(self.__selected)
                serres = []
                for casev in cv:
                    if len(casev.getPoss()) == 2 and casev not in cv:
                        serres.append(casev)
                for v in serres:
                    p = int(v.getPoss()[0])
                    q = int(v.getPoss()[1])
                    for v2 in serres:
                        if v2 != v:
                            if (p in self.__selected.getPoss() and q in v2.getPoss()) or (q in self.__selected.getPoss() and p in v2.getPoss()):
                                cvv1 = self.casevoisine(v)
                                cvv2 = self.casevoisine(v2)
                                for e in cvv1:
                                    if e in cvv2:
                                        if (p in self.__selected.getPoss() and q in v2.getPoss()) and q in e.getPoss():
                                            l = e.getPoss()
                                            l.remove(int(q))
                                            e.setPoss(l)
                                        if p in e.getPoss() and (q in self.__selected.getPoss() and p in v2.getPoss()):
                                            l = e.getPoss()
                                            l.remove(int(p))
                                            e.setPoss(l)

        ######################################## Prog de résolution #############################################
    def solveInt(self):

        for gp in self.__list_group:
            for case in gp.getListe():
                self.setSelected(case)
                if bool(self.__selected.getEstModif()):
                    self.__selected.setPoss(
                        [int(i) for i in range(1, int(gp.getNbElem())+1)])
                else:
                    self.__selected.setPoss([int(self.__selected.getNum())])

        while not self.__solved:
            for ssg in self.__list_group:
                if not bool(ssg.getEtat()):
                    self.controle()
                    if bool(ssg.getEtat()):
                        continue
                    self.fullblock(ssg)
                    if bool(ssg.getEtat()):
                        continue
                    self.controle()
                    if bool(ssg.getEtat()):
                        continue
                    self.unique(ssg)
                    if bool(ssg.getEtat()):
                        continue
                    self.controle()
                    if bool(ssg.getEtat()):
                        continue
                    self.crown(ssg)
                    if bool(ssg.getEtat()):
                        continue
                    self.controle()
                    if bool(ssg.getEtat()):
                        continue
                    self.Round234(ssg)
                    if bool(ssg.getEtat()):
                        continue
                    self.controle()
                    if bool(ssg.getEtat()):
                        continue
                    self.SimpleNakedPair(ssg)
                    if bool(ssg.getEtat()):
                        continue
                    self.controle()
                    if bool(ssg.getEtat()):
                        continue
                    self.SimpleHiddenPair(ssg)
                    if bool(ssg.getEtat()):
                        continue
                    self.controle()
                    if bool(ssg.getEtat()):
                        continue
                    self.NakedSingle(ssg)
                    if bool(ssg.getEtat()):
                        continue
                    self.controle()
                    if bool(ssg.getEtat()):
                        continue
                    self.HiddenSingle(ssg)
                    if bool(ssg.getEtat()):
                        continue
                    self.controle()
                    if bool(ssg.getEtat()):
                        continue
                    self.NakedPairB(ssg)
                    if bool(ssg.getEtat()):
                        continue
                    self.controle()
                    if bool(ssg.getEtat()):
                        continue
                    self.SameValueCells(ssg)
                    if bool(ssg.getEtat()):
                        continue
                    self.controle()
                    if bool(ssg.getEtat()):
                        continue
                    self.XYWing(ssg)
                    if bool(ssg.getEtat()):
                        continue
                    self.controle()

    def solve(self):
        self.__cellulesModifiables = []
        length = 0
        for i in range(self.__n):
            for j in range(self.__m):
                c = self.__matrice[i][j]
                if (c.getEstModif()):
                    self.__cellulesModifiables.append(
                        [c, 0, c.getGrp().getNbElem()])
                    length += 1
        k = 0
        while (not self.__solved and k < length):
            CURRENT = self.__cellulesModifiables[k]
            self.setSelected(CURRENT[0])
            if (CURRENT[1] < CURRENT[2]):
                CURRENT[1] += 1
                self.__cellulesModifiables[k] = CURRENT
                self.__selected.changeVal(CURRENT[1])
                if (self.__listError.getNb() == 0):
                    k = k + 1
            else:
                CURRENT[1] = 0
                self.__cellulesModifiables[k] = CURRENT
                self.__selected.changeVal("")
                k = k - 1
# endregion

# region Affichage des règles
    def btn_regles(self):
        self.btn_regles = Button(self.__window, text="Règles", font=(
            "Courrier", 20), fg='#b62546', command=self.open_regle)
        self.btn_regles.place(relx=0.75, y=5, width=100, height=40)

    def open_regle(self):
        self.frame_regle = Frame(width=400, height=420, bg="#ecffd7")
        self.frame_regle.place(relx=0.5, rely=0.5, anchor=CENTER)

        photo = PhotoImage(file="image/croix.png")
        photo = photo.subsample(30)  # redimensionnement de l'image
        btn_close = Button(self.frame_regle, image=photo,
                           command=self.destroy_regle)
        # si on se passe de cette ligne le garbage collector detruit l'image (car on est en local)
        btn_close.image = photo
        btn_close.place(relx=0.95, rely=0.05, anchor=CENTER)

        self.print_regles()

    def print_regles(self):
        titre = Label(self.frame_regle, text="Règles",
                      font=("Courrier", 40), bg="#ecffd7")
        titre.place(relx=0.5, y=30, anchor=CENTER)

        r1 = Label(self.frame_regle, text="Une grille contient des régions de taille variant entre 1 et 5 cases", font=(
            "Courrier", 14), wraplength=300, bg="#ecffd7")
        r1.place(relx=0.5, y=90, anchor=CENTER)

        r2 = Label(self.frame_regle, text="Chaques région doit contenir tout les chiffre de 1 à n, n étant la taille de la région", font=(
            "Courrier", 14), wraplength=300, bg="#ecffd7")
        r2.place(relx=0.5, y=160, anchor=CENTER)

        r3 = Label(self.frame_regle, text="Deux case adjacentes ne doivent pas contenir le même chiffre, cela inclu les diagonales", font=(
            "Courrier", 14), wraplength=300, bg="#ecffd7")
        r3.place(relx=0.5, y=240, anchor=CENTER)

        r4 = Label(self.frame_regle, text="En rouge : les erreurs d'adjacence", font=(
            "Courrier", 11), wraplength=300, bg="#ecffd7")
        r4.place(relx=0.5, y=300, anchor=CENTER)

        r5 = Label(self.frame_regle, text="En orange : les doublons dans une région", font=(
            "Courrier", 11), wraplength=300, bg="#ecffd7")
        r5.place(relx=0.5, y=330, anchor=CENTER)

        r6 = Label(self.frame_regle, text="En bleu : les cases dont le numero dépasse le max de la région (ex: une region de 3 cases ne peut contenir de numéro > 3)", font=(
            "Courrier", 11), wraplength=300, bg="#ecffd7")
        r6.place(relx=0.5, y=375, anchor=CENTER)

    def destroy_regle(self):
        self.frame_regle.destroy()
    # endregion

# region Gestion des frames
    # créer une frame
    def create_frame(self):
        self.__frame = Frame(self.__window, bd=0)

    # empaquetage d'une frame

    def pack_frame(self):
        self.__frame.pack(expand=YES, side="top")
    # endregion

# region --------------Autres---------------
    # modifie le parametre __selected de la classe grille (c'est ce qui gère la séléction de cases)
    def setSelected(self, obj):
        # on remet a default uniquement si il n'y a pas d'erreur sur cette case
        if self.__selected is not None:
            if self.__selected.getErr() == False:
                self.__selected.draw("default")
            elif self.__selected.getErr() == "group":
                self.__selected.draw("group")
            elif self.__selected.getErr() == "adjascence":
                self.__selected.draw("adjascence")
            elif self.__selected.getErr() == "out":
                self.__selected.draw("out")

        self.__selected = obj  # selectionne la case
        self.__selected.bgYellow()  # met la couleur a jaune

    def getSelected(self):
        return self.__selected

    def getSolved(self):
        return self.__solved

    def load_menu(self):
        try:  # si on a gagné, detruit le message de victoire
            self.fram_victory.destroy()
        except:
            pass
        # detruit toute la grille
        self.frame2.destroy()
        self.btn_back.destroy()
        self.btn_solve.destroy()
        self.btn_regles.destroy()
        self.btn_solveInt.destroy()
        self.btn_save.destroy()
        self.__frame.destroy()
        # affiche le menu
        self.menu.load_menu()

    # affiche les 5 boutons permettant de changer la valeur d'une case

    def load_down_pad(self):
        self.frame2 = Frame(self.__window)
        try:
            for i in range(self.__max):
                Button(self.frame2, text="{}".format(i+1), width=self.__max, height=2,
                       command=lambda j=i+1: self.changeVal(j)).grid(row=0, column=i)
            Button(self.frame2, text="", width=self.__max, height=2,
                   command=lambda j="": self.changeVal(j)).grid(row=0, column=self.__max)
        except:
            pass

        self.frame2.place(relx=0.5, rely=0.90, anchor=CENTER)

    # si une case est selectionnée, on change son numero
    def changeVal(self, j):
        if self.__selected != None:
            self.__selected.changeVal(j)

    def btn_retour(self):
        self.btn_back = Button(self.__window, text="Menu", font=(
            "Courrier", 20), fg='#b62546', command=self.load_menu)
        self.btn_back.place(x=5, y=5, width=80, height=40)
        # endregion
