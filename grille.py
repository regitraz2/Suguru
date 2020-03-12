from tkinter import *
from case import Case
from group import Group


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

		self.create_frame()

		self.load_config(cfg) #charge la grille selectionné dans les options
		self.btn_retour() # pour retourner au menu
		self.load_change_grid() #charge le pad pour entrer les chiffres dans la grille

		self.pack_frame() #l'affiche


	#charge une grille a partir d'un fichier de config
	def load_config(self, name):
		file = open("config.cfg", "r")

		lines = file.readlines() #récupere une liste contenant toutes les lignes du fichier de config
		length = len(lines) #compte le nombre de lignes
		file.close() #on ferme l'acces en lecture

		#recherche de la config specifié dans le fichier (jusqu'a la fin du fichier)
		k = 0
		lines[k] = lines[k].rstrip()
		while lines[k] != name and k < length:
			k += 1
			lines[k] = lines[k].rstrip() #enleve les \r\n ou \n a la fin

		k += 1  #avance d'une ligne

		n = int(lines[k][0]) # n = taille de la grille
		self.__n = n #on iscrit la taille comme parametre de la grille

		k += 1  #avance d'une ligne

		# rappel :  dans x:y, x est le numero affiché dans une case, et y le numero du groupe
		grid = self.configFormat(lines, k, n) #grille de taille n de couple x:y

		self.create_config(grid, n) #charge et place les widget

		self.drawGroups()


	#met la config choisie sous forme exploitable / enleve les caracteres inutiles / isoles les x:y (cf fichier de config)
	def configFormat(self, lines, k, n):
		grid = []
		l = len(lines[k])-1 #nombre de caractere d'une ligne -1
		for i in range(n):
			sgrid = [] #une ligne de la matrice
			for j in range(l):
				if lines[k+i][j] ==":": #pour chaque ':' trouver on regarde ce qu'il y a a gauche et a droite
					sgrid.append(lines[k+i][j-1]+lines[k+i][j]+lines[k+i][j+1]) #on met x:y dans une ligne
			grid.append(sgrid) #on ajoute la ligne a la matrice
		return grid


	#charge et place les widget dans la grille
	def create_config(self, grid, n):
		for i in range(n):
			sgrid = [] #initialise une ligne
			for j in range(n):
				num = int(grid[i][j][0]) #chifre de la case
				numGrp = int(grid[i][j][2]) #numero du groupe

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


	#colore en rouge les nombres identique et cote a cote et les doublon dans un groupe
	#de plus renvoie vrai si il n'y a aucune erreurs (cf victoire)
	def colorError(self):
		#reinitialise les couleurs avant de recolorier les erreurs
		for i in range(self.__n):
			for j in range(self.__n):
				if self.__matrice[i][j] == self.__selected: #on ne change pas le bg de la case selectionnée
					self.__matrice[i][j].bgYellow()
				else:#sinon on met la couleur de base de la case
					if self.__matrice[i][j].getEstModif():
						self.__matrice[i][j].bgLightGray()
					else:
						self.__matrice[i][j].bgGray()
				#deux couleur differente selon si la case est modifiable ou non

		res = True # res sert a determiner la victoire

		#pour les groupes
		for i in self.__list_group:
			if res is not False: # si res est a faux alors on y touche plus mais on termine le coloriage
				res = i.colorGroupError()
			else:
				i.colorGroupError()

		#pour les cases cote a cote
		for i in range(self.__n):
			for j in range(self.__n):
				#teste les 4 case a coté de celle au rang [i][j] et les colore si elles ont le meme numero
				if self.__matrice[i][j].getNum() != "":
					if i+1 < self.__n:
						if self.__matrice[i][j].getNum() == self.__matrice[i+1][j].getNum():
							self.__matrice[i][j].bgRed()
							self.__matrice[i+1][j].bgRed()
							if res is not False:
								res = False

					if j+1 < self.__n :
						if self.__matrice[i][j].getNum() == self.__matrice[i][j+1].getNum():
							self.__matrice[i][j].bgRed()
							self.__matrice[i][j+1].bgRed()
							if res is not False:
								res = False

					if i-1 >= 0 :
						if self.__matrice[i][j].getNum() == self.__matrice[i-1][j].getNum():
							self.__matrice[i][j].bgRed()
							self.__matrice[i-1][j].bgRed()
							if res is not False:
								res = False

					if j-1 >= 0 :
						if self.__matrice[i][j].getNum() == self.__matrice[i][j-1].getNum():
							self.__matrice[i][j].bgRed()
							self.__matrice[i][j-1].bgRed()
							if res is not False:
								res = False
		return res


	#dessine les groupes
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


	#modifie le parametre __selected de la classe grille
	def setSelected(self, obj):
		if self.__selected is not obj:
			self.__selected = obj #selectionne la case
			self.colorError() #colore les erreurs de toute la grille
			self.__selected.bgYellow() #met la couleur a jaune


	#renvoie vraie si toutes les cases sont remplies par un chiffre
	def remplie(self):
		for i in range(self.__n):
			for j in range(self.__n):
				if self.__matrice[i][j].getNum() == "":
					return False
		return True


	#affiche les boutons pour changer la valeur d'un bouton
	def load_change_grid(self):
		self.frame2 = Frame(self.__window)
		k = 0 #s'incremente jusqu'a 9
		for i in range(3):
			for j in range(3):
				k += 1
				Button(self.frame2, text="{}".format(k), width=5, height=2, command=lambda i=k: self.__selected.changeVal(i)).grid(row=i, column=j)

		self.frame2.place(relx=0.5, rely=0.85, anchor=CENTER)

	def btn_retour(self) :
		self.btn_back = Button(self.__window, text = "Menu", font = ("Courrier", 20), fg = '#b62546', command = self.load_menu)
		self.btn_back.place(x = 5, y = 5, width = 80, height = 40)


	#renvoie True si la victoire est acquise et dessine un gros VCTOIRE
	def victory(self):
		if(self.colorError() and self.remplie()): #si le grille est remplie et qu'il n'y a pas d'erreur : on gagne
			self.create_label_victory()
		else:
			return False


	def load_menu(self):
		try: #si on a gagné, detruit le message de victoire
			self.fram_victory.destroy()
		except:
			pass
		#detruit toute la grille
		self.frame2.destroy()
		self.btn_back.destroy()
		self.__frame.destroy()
		#affiche le menu
		self.menu.load_menu()


	#le label affiché lors de la victiore
	def create_label_victory(self):
		self.fram_victory = Frame()
		Label(self.fram_victory, text = "VICTOIRE", font = ("Courrier", 40), fg = "green").pack()
		self.fram_victory.place(relx = 0.22, rely = 0.4)

	#créer une frame
	def create_frame(self) :
		self.__frame = Frame(self.__window, bd=0)


	# empaquetage d'une frame
	def pack_frame(self) :
		self.__frame.pack(expand = YES, side = "top")
