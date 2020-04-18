from tkinter import *

class Case:
	def __init__(self, frame, nom, num, estModifiable, i, j, grille):
		#attributs
		self.grille = grille #grille dans laquelle est la case, sert a definir la case selectionné lors du click
		self.__num = StringVar() #chaine de caractere dynamique (quand la var change, le texte du bouton aussi)
		self.__grp = None #groupe dans lequel est la case (sera defini plus tard)
		self.__estModifiable = estModifiable #dit si la case est modifiable
		self.__nom = nom #nom de la case
		self.setNum(num) #on met la valeur de num dans __num

		#permet de changer la couleur uniquement si il n'y a pas d'erreur, lors de la suppression d'une erreur ce parametre change
		#peprmet aussi de faire une sorte de file de priorité des erreur : un erreur de groupe est affiche si il n'y a pas d'erreur d'adjascence
		self.__hasError = False

		#indice de cette case dans la matrice, sert lors de l'optimisation des erreurs
		self.__i = i
		self.__j = j

		#sert a dessiner les bordures
		self.__border_right = 1
		self.__border_left = 1
		self.__border_top = 1
		self.__border_bottom = 1


		#deux bouton differents selon si il est modifiable ou non
		# on créer le canvas (bd=-2 car le canvas Tkinter a un border a 2 par default) puis le bouton dedans
		self.canvas = Canvas(frame, relief = FLAT, width = 54, height = 50, bd = -2) #on le grid dans la classe grille, idem pour la frame
		self.rect_id = self.canvas.create_rectangle(0, 0, 54, 50) #un rectangle sert de background car la propriété background du canvas efface les border

		if self.__estModifiable:
			self.btn = Button(self.canvas, textvariable = self.__num, height = 2, width = 5, relief = "flat", command=lambda :self.grille.setSelected(self))
		else:
			self.btn = Button(self.canvas, textvariable = self.__num, height = 2, width = 5, relief = "flat", state=DISABLED, disabledforeground="black")

		self.draw("default") #colore la case de la bonne couleur

		self.btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)  #on centre le bouton dans le canvas



#region Backgrounds et couleurs
	#change la couleur de fond de la case
	def bgRed(self):
		self.btn.configure(bg="#ff5c5c")
		self.canvas.itemconfigure(self.rect_id, fill="#ff5c5c")
	def bgDarkRed(self):
		self.btn.configure(bg="#9c321b")
		self.canvas.itemconfigure(self.rect_id, fill="#9c321b")
	def bgOrange(self):
		self.btn.configure(bg="orange")
		self.canvas.itemconfigure(self.rect_id, fill="orange")
	def bgDarkOrange(self):
		self.btn.configure(bg="darkorange3")
		self.canvas.itemconfigure(self.rect_id, fill="darkorange3")
	def bgYellow(self):
		self.btn.configure(bg = "#fffa87")
		self.canvas.itemconfigure(self.rect_id, fill="#fffa87")
	def bgLightGray(self):
		self.btn.configure(bg="#d6d6d6")
		self.canvas.itemconfigure(self.rect_id, fill="#d6d6d6")
	def bgGray(self):
		self.btn.configure(bg="gray70")
		self.canvas.itemconfigure(self.rect_id, fill="gray70")

	#choisit la couleur du background en fonction de self.__hasError
	def draw(self, type) :
		if type == "default" and self.__hasError == False: #si il n'y a pas d'erreur
			if self.__estModifiable :
				self.bgLightGray()
			else :
				self.bgGray()

		elif type == "adjascence" :
			self.__hasError = "adjascence"
			if self.__estModifiable :
				self.bgRed()
			else :
				self.bgDarkRed()

		elif type == "group" :
			if self.__hasError != "adjascence": #priorité aux erreurs d'adjascence
				self.__hasError = "group"

				if self.__estModifiable :
					self.bgOrange()
				else :
					self.bgDarkOrange()

#endregion et couleurs

#region Dessin des bordure de la case
	#dessine les bordure, 0 = petite bordure, 1 = grosse bordure
	#ce systeme dessine les grosse bordure apres (ajoute un genre de priorité) ce qui rend la grille plus jolie
	def drawBorder(self):
		if self.__border_right == 1:
			self.bbdr()
		if self.__border_left == 1:
			self.bbdl()
		if self.__border_top == 1:
			self.bbdt()
		if self.__border_bottom == 1:
			self.bbdb()


	#bbd = big border, ensuite il y a 4 direction : t = top, b = bottom, l = left et r = right
	#dessine de grosse bordure (pour delimiter les groupes)
	def bbdt(self) :
		self.canvas.create_line(0, 1, 54, 1, width = 2, joinstyle="bevel", capstyle="round")
	def bbdb(self) :
		self.canvas.create_line(0, 49, 54, 49, width = 2, joinstyle="bevel", capstyle="round")
	def bbdr(self) :
		self.canvas.create_line(53, 0, 53, 54, width = 2, joinstyle="bevel", capstyle="round")
	def bbdl(self) :
		self.canvas.create_line(1, 0, 1, 54, width = 2, joinstyle="bevel", capstyle="round")
#endregion


#region Méthodes d'accès
	def setNum(self, num):
		self.__num.set(num)
	def setGrp(self, grp):
		self.__grp = grp
	def setNom(self, nom):
		self.__nom = nom
	def setBdr(self, val):
		self.__border_right = val
	def setBdl(self, val):
		self.__border_left = val
	def setBdt(self, val):
		self.__border_top = val
	def setBdb(self, val):
		self.__border_bottom = val
	def setErr(self, val):
		self.__hasError = val

	def getNum(self):
		return self.__num.get()
	def getNom(self):
		return self.__nom
	def getGrp(self):
		return self.__grp
	def getEstModif(self):
		return self.__estModifiable
	def getI(self):
		return self.__i
	def getJ(self):
		return self.__j
	def getErr(self):
		return self.__hasError
#endregion


#region Autre
	#modifie la valeur de num (celle qui est affiché sur le bouton)
	def changeVal(self, num):
		self.setNum(num)
		self.grille.victory()
		self.grille.checkErrors()
#endregion