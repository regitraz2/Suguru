from tkinter import *
from case import Case
from group import Group
from errors import *
from tools import *


class Grille:
	#constructeur grille aleatoire
	def __init__(self, window, menu):
		#attributs
		self.menu = menu
		self.__window = window #fenetre dans laquelle est la grille
		self.__n = 0 #taille de la grille
		self.__selected = None #case selectionnée
		self.__matrice = [] #matrices des cases
		self.__list_group = [] #liste des groupe
		self.__listError = listErrors()

		self.create_frame()

		#devra généré une grille aléatoire

		self.pack_frame()


	#constructeur grille a partir d'un fichier de config
	def __init__(self, window, menu, cfg):
		#attributs
		self.menu = menu
		self.__window = window #fenetre dans laquelle est la grille
		self.__n = 0 #taille de la grille
		self.__selected = None #case selectionnée
		self.__matrice = [] #matrices des cases
		self.__list_group = [] #liste des groupe
		self.__listError = listErrors()

		self.create_frame()

		self.load_config(cfg) #charge la grille selectionné dans les options
		self.btn_retour() # pour retourner au menu
		self.load_down_pad() #charge le pad pour entrer les chiffres dans la grille
		self.btn_regles() #affiche les règles
		self.btn_solve() # boutton pour résoudre la grille


		self.pack_frame() #l'affiche

#region Chargement de la config
	#charge une grille a partir d'un fichier de config
	def load_config(self, cfg):
		print("grille chargée : ")
		affiche1dim(cfg)

		self.create_config(cfg, len(cfg)) #charge et place les widget (cases)

		self.drawGroups()


	#charge et place les widget dans la grille
	def create_config(self, grid, n):
		self.__n = n
		for i in range(self.__n):
			sgrid = [] #initialise une ligne
			for j in range(self.__n):
				num = grid[i][j][0] #chifre de la case
				numGrp = grid[i][j][1] #numero du groupe

				if num > 0:
					estModifiable = False # on est dans une config précréer, alors on ne veut pas modifier les case qui on un numero
				else:
					estModifiable = True
					num = "" #pas de numero pour les autres cases

				# creation de la case
				case = Case(self.__frame, "btn{}{}".format(i, j), num, estModifiable, i, j, self)

				# placement de la case
				case.canvas.grid(row=i, column=j)

				# on ajoute la case dans la ligne
				sgrid.append(case)

				#on met la case dans son groupe
				self.addInGroup(case, numGrp)

			self.__matrice.append(sgrid) #ajout de la ligne dans la grille
#endregion

#region Gestion groupes
	#ajoute une case dans un groupe1
	def addInGroup(self, case, numGrp):
		nom = "groupe{}".format(numGrp)

		#si le groupe existe deja, ajoute la case dedans
		for x in self.__list_group:
			if x.getNom() == nom:
				x.ajout(case)
				case.setGrp(x)
				return #arrete la fonction

		#crée un groupe, y ajoute la case et l'ajoute dans la liste des groupes
		grp = Group(nom)
		grp.ajout(case)
		case.setGrp(grp)
		self.__list_group.append(grp)


	#Dessine les bordure des groupes
	def drawGroups(self):
		for i in range(self.__n):
			for j in range(self.__n):
				if self.__matrice[i][j].getNom() != self.__matrice[i][j-1].getNom():# si ce n'est pas deux fois la meme case
					#definit les border de la case
					if i+1 < self.__n:#si on est dans la grille on fait le test
						if self.__matrice[i][j].getGrp() == self.__matrice[i+1][j].getGrp():
							self.__matrice[i][j].setBdb(0)

					if i-1 >= 0:#si on est dans la grille
						if self.__matrice[i][j].getGrp() == self.__matrice[i-1][j].getGrp():
							self.__matrice[i][j].setBdt(0)

					if j+1 < self.__n:#si on est dans la grille
						if self.__matrice[i][j].getGrp() == self.__matrice[i][j+1].getGrp():
							self.__matrice[i][j].setBdr(0)

					if j-1 >= 0:#si on est dans la grille
						if self.__matrice[i][j].getGrp() == self.__matrice[i][j-1].getGrp():
							self.__matrice[i][j].setBdl(0)

					self.__matrice[i][j].drawBorder() #dessine les border comme selectionné ci dessus
	#endregion

#region Gestion des erreur
	#cherche des erreurs autour de la cae selectionnée
	def checkErrors(self):
		#position de la case selectionnée dans la matrice, sert a  trouver facilement les cases adjascentes
		#et ainsi la case matrice[i][j] est la meme que la case selected, ce qui m'a donné moins de travail
		# quand j'ai changer de facon de gérer les erreurs
		i = self.__selected.getI()
		j = self.__selected.getJ()

		#pour les cases cote a cote
		#teste les 8 case a coté de celle selectionnée et les colore si elles ont le meme numero
		if self.__matrice[i][j].getNum() != "":

			# supprime les erreurs d'adjascences du numero de la case selectionnée (il peut y en avoir plusieurs)
			# en gros actualise la liste des erreurs d'adjascence
			self.__listError.deleteAdjError(self.__selected)

			if i+1 < self.__n:
				if self.__matrice[i][j].getNum() == self.__matrice[i+1][j].getNum():
					self.__listError.createError(self.__selected, self.__matrice[i+1][j])

			if j+1 < self.__n :
				if self.__matrice[i][j].getNum() == self.__matrice[i][j+1].getNum():
					self.__listError.createError(self.__matrice[i][j], self.__matrice[i][j+1])

			if i-1 >= 0 :
				if self.__matrice[i][j].getNum() == self.__matrice[i-1][j].getNum():
					self.__listError.createError(self.__matrice[i][j], self.__matrice[i-1][j])

			if j-1 >= 0 :
				if self.__matrice[i][j].getNum() == self.__matrice[i][j-1].getNum():
					self.__listError.createError(self.__matrice[i][j], self.__matrice[i][j-1])

			#pour les diagonales
			if i+1 < self.__n and j+1 < self.__n :
				if self.__matrice[i][j].getNum() == self.__matrice[i+1][j+1].getNum() :
					self.__listError.createError(self.__matrice[i][j], self.__matrice[i+1][j+1])

			if i+1 < self.__n and j-1 >= 0 :
				if self.__matrice[i][j].getNum() == self.__matrice[i+1][j-1].getNum() :
					self.__listError.createError(self.__matrice[i][j], self.__matrice[i+1][j-1])

			if i-1 >= 0 and j+1 < self.__n :
				if self.__matrice[i][j].getNum() == self.__matrice[i-1][j+1].getNum() :
					self.__listError.createError(self.__matrice[i][j], self.__matrice[i-1][j+1])

			if i-1 >= 0 and j-1 >= 0 :
				if self.__matrice[i][j].getNum() == self.__matrice[i-1][j-1].getNum() :
					self.__listError.createError(self.__matrice[i][j], self.__matrice[i-1][j-1])

			# pour les groupes
			# les groupes ne contiennent que des cases avec des numeros,
			# donc si la case selectionnée n'en a pas nous ne testons pas les erreurs de groupe car il n'y aurais aucune correspondance des numéros
			grp = self.__selected.getGrp() #le groupe dans lequel est la case selectionnée
			caseErr = grp.isGroupError(self.__selected)  # cf definition de isGroupError

			#si il y a des erreur dans caseErr, créer une erreur si elle n'existe pas, sinon nettoie tout le groupe des erreur en lien avec la case selectionnée
			if len(caseErr) > 0 :
				for err in caseErr:
					self.__listError.createError(self.__matrice[i][j], err, grp.getNom())
			else :
				self.__listError.deleteGrpError(self.__selected, grp.getNom())

			self.__listError.deleteOutErr(self.__matrice[i][j])
			#si le numero entré dépasse le max du groupe, et si il n'y a aucune autre erreur (elles ont la priorité)
			if(self.__selected.getErr() == False and  int(self.__selected.getNum()) > self.__selected.getGrp().getNbElem()):
				self.__listError.createError(self.__matrice[i][j], "")


	#endregion

#region Victoire
	#renvoie True si la victoire est acquise et dessine un gros VCTOIRE
	def victory(self):
		if(self.__listError.getNb() == 0 and self.remplie()): #si le grille est remplie et qu'il n'y a pas d'erreur : on gagne
			self.create_label_victory()
		else:
			return False

	#renvoie vraie si toutes les cases sont remplies par un chiffre
	def remplie(self):
		for i in range(self.__n):
			for j in range(self.__n):
				if self.__matrice[i][j].getNum() == "":
					return False
		return True


	#le label affiché lors de la victiore
	def create_label_victory(self):
		self.fram_victory = Frame()
		Label(self.fram_victory, text = "VICTOIRE", font = ("Courrier", 40), fg = "green").pack()
		self.fram_victory.place(relx = 0.22, rely = 0.4)

	#endregion

#region Affichage des règles
	def btn_solve(self) :
		self.btn_solve = Button(self.__window, text = "Résoudre brute", font = ("Courrier", 20), fg = '#b62546', command = self.solve)
		self.btn_solve.place(relx = 0.32, y = 5, width = 150, height = 40)

	def solve(self):
		self.__cellulesModifiables = []
		for i in range(self.__n):
			for j in range(self.__n):
				c = self.__matrice[i][j]
				if (c.getEstModif()):
					self.__cellulesModifiables.append([c,0,c.getGrp().getNbElem()])
		k = 0
		while (not self.victory()) and (k < len(self.__cellulesModifiables)):
			CURRENT = self.__cellulesModifiables[k]
			self.setSelected(CURRENT[0])
			if (CURRENT[1] < CURRENT[2]):
				CURRENT[1] =  CURRENT[1]+1
				self.__cellulesModifiables[k] = CURRENT
				self.__selected.changeVal(CURRENT[1])
				if (self.__listError.getNb() == 0):
					k = k + 1
			else:
				CURRENT[1] = 0
				self.__cellulesModifiables[k] = CURRENT
				self.__selected.changeVal(0)
				self.__selected.changeVal("")
				k = k - 1

	def btn_regles(self) :
		self.btn_back = Button(self.__window, text = "Règles", font = ("Courrier", 20), fg = '#b62546', command = self.open_regle)
		self.btn_back.place(relx = 0.75, y = 5, width = 100, height = 40)

	def open_regle(self):
		self.frame_regle = Frame(width=400, height=420, bg="#ecffd7")
		self.frame_regle.place(relx=0.5, rely=0.5, anchor=CENTER)

		photo = PhotoImage(file = "image/croix.png")
		photo = photo.subsample(30) #redimensionnement de l'image
		btn_close = Button(self.frame_regle, image=photo, command=self.destroy_regle)
		btn_close.image = photo #si on se passe de cette ligne le garbage collector detruit l'image (car on est en local)
		btn_close.place(relx=0.95, rely=0.05, anchor=CENTER)

		self.print_regles()

	def print_regles(self):
		titre = Label(self.frame_regle, text="Règles", font=("Courrier", 40), bg="#ecffd7")
		titre.place(relx=0.5, y=30, anchor=CENTER)

		r1 = Label(self.frame_regle, text="Une grille contient des régions de taille variant entre 1 et 5 cases", font=("Courrier", 14), wraplength=300, bg="#ecffd7")
		r1.place(relx=0.5, y=90, anchor=CENTER)

		r2 = Label(self.frame_regle, text="Chaques région doit contenir tout les chiffre de 1 à n, n étant la taille de la région", font=("Courrier", 14), wraplength=300, bg="#ecffd7")
		r2.place(relx=0.5, y=160, anchor=CENTER)

		r3 = Label(self.frame_regle, text = "Deux case adjacentes ne doivent pas contenir le même chiffre, cela inclu les diagonales", font=("Courrier", 14), wraplength=300, bg = "#ecffd7")
		r3.place(relx = 0.5, y = 240, anchor = CENTER)

		r4 = Label(self.frame_regle, text = "En rouge : les erreurs d'adjacence", font=("Courrier", 11), wraplength=300, bg = "#ecffd7")
		r4.place(relx = 0.5, y = 300, anchor = CENTER)

		r5 = Label(self.frame_regle, text = "En orange : les doublons dans une région", font=("Courrier", 11), wraplength=300, bg = "#ecffd7")
		r5.place(relx = 0.5, y = 330, anchor = CENTER)

		r6 = Label(self.frame_regle, text = "En bleu : les cases dont le numero dépasse le max de la région (ex: une region de 3 cases ne peut contenir de numéro > 3)", font=("Courrier", 11), wraplength=300, bg = "#ecffd7")
		r6.place(relx = 0.5, y = 375, anchor = CENTER)

	def destroy_regle(self):
		self.frame_regle.destroy()
	#endregion

#region Gestion des frames
	#créer une frame
	def create_frame(self) :
		self.__frame = Frame(self.__window, bd=0)


	# empaquetage d'une frame
	def pack_frame(self) :
		self.__frame.pack(expand = YES, side = "top")
	#endregion

#region --------------Autres---------------
	#modifie le parametre __selected de la classe grille (c'est ce qui gère la séléction de cases)
	def setSelected(self, obj):
		#on remet a default uniquement si il n'y a pas d'erreur sur cette case
		if self.__selected is not None:
			if self.__selected.getErr() == False:
				self.__selected.draw("default")
			elif self.__selected.getErr() == "group":
				self.__selected.draw("group")
			elif self.__selected.getErr() == "adjascence":
				self.__selected.draw("adjascence")
			elif self.__selected.getErr() == "out":
				self.__selected.draw("out")

		self.__selected = obj #selectionne la case
		self.checkErrors()
		self.__selected.bgYellow() #met la couleur a jaune

	def getSelected(self):
		return self.__selected

	def load_menu(self):
		try: #si on a gagné, detruit le message de victoire
			self.fram_victory.destroy()
		except:
			pass
		#detruit toute la grille
		self.frame2.destroy()
		self.btn_back.destroy()
		self.btn_solve.destroy()
		self.__frame.destroy()
		#affiche le menu
		self.menu.load_menu()


	#affiche les 5 boutons permettant de changer la valeur d'une case
	def load_down_pad(self):
		self.frame2 = Frame(self.__window)
		try:
			for i in range(5):
				Button(self.frame2, text="{}".format(i+1), width=5, height=2, command=lambda j=i+1: self.changeVal(j)).grid(row=0, column=i)
			Button(self.frame2, text="", width=5, height=2, command=lambda j="": self.changeVal(j)).grid(row=0, column=5)
		except:
			pass

		self.frame2.place(relx=0.5, rely=0.90, anchor=CENTER)

	# si une case est selectionnée, on change son numero
	def changeVal(self, j):
		if self.__selected != None:
			self.__selected.changeVal(j)


	def btn_retour(self) :
		self.btn_back = Button(self.__window, text = "Menu", font = ("Courrier", 20), fg = '#b62546', command = self.load_menu)
		self.btn_back.place(x = 5, y = 5, width = 80, height = 40)
#endregion