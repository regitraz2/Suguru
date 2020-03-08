from tkinter import *
import time

class Case:
	def __init__(self, frame, nom, num, estModifiable, i, j, grille):
		#attributs
		self.__num = StringVar() #chaine de caractere dynamique (quand la var change, le texte du bouton aussi)
		self.grille = grille
		self.__grp = None
		self.__estModifiable = estModifiable
		self.__nom = nom
		self.__posX = i
		self.__posY = j
		self.setNum(num)


		#deux bouton differents selon si il est modifiable ou non
		if self.__estModifiable:
			# on créer le canvas puis le bouton dedans
			self.canvas = Canvas(frame, relief = FLAT, width = 54, height = 50, bd = 0, bg="lightgray") #on le grid dans la classe grille, idem pour la frame
			self.btn = Button(self.canvas, textvariable = self.__num, height = 2, width = 5, relief = "flat", bg= "lightgray", command=lambda :self.grille.setSelected(self))
		else:
			self.canvas = Canvas(frame, relief = FLAT, width = 54, height = 50, bd = 0, bg="gray70") #on le grid dans la classe grille, idem pour la frame
			self.btn = Button(self.canvas, textvariable = self.__num, height = 2, width = 5, relief = "flat", bg="gray70", state=DISABLED, disabledforeground="black")

		self.btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)  #on centre le bouton dans le canvas

	#change la couleur de fond de la case
	def bgRed(self):
		self.btn.configure(bg="#ff5c5c")
		self.canvas.config(bg="#ff5c5c")
	def bgOrange(self):
		self.canvas.config(bg="orange")
		self.btn.configure(bg="orange")
	def bgYellow(self):
		self.btn.configure(bg = "#fffa87")
		self.canvas.config(bg="#fffa87")
	def bgLightGray(self):
		self.canvas.config(bg="lightgray")
		self.btn.configure(bg="lightgray")
	def bgGray(self):
		self.canvas.config(bg="gray70")
		self.btn.configure(bg="gray70")
	def bgBlue(self):
		self.canvas.config(bg="lightblue")
		self.btn.configure(bg="lightblue")


	#modifie la valeur de num (celle qui est affiché sur le bouton)
	def changeVal(self, num):
		self.setNum(num)
		self.grille.victory()


	#bbd = big border, ensuite il y a 4 direction : t = top, b = bottom, l = left et r = right
	#dessine de grosse bordure (pour delimiter les groupes)
	def bbdt(self) :
		self.canvas.create_line(0, 4, 58, 4, width = 5)
	def bbdb(self) :
		self.canvas.create_line(0, 50, 58, 50, width = 4)
	def bbdr(self) :
		self.canvas.create_line(54, 0, 54, 54, width = 4)
	def bbdl(self) :
		self.canvas.create_line(4, 0, 4, 54, width = 5)


	#dessine des bordure normales (pour delimiter les cases)
	def bdt(self) :
		self.canvas.create_line(0, 2, 58, 2, width = 4)
	def bdb(self) :
		self.canvas.create_line(0, 52, 54, 52, width = 4)
	def bdr(self) :
		self.canvas.create_line(56, 0, 56, 54, width = 4)
	def bdl(self) :
		self.canvas.create_line(2, 0, 2, 54, width = 4)


	#Méthodes d'accès
	def setNum(self, num):
		self.__num.set(num)
	def setGrp(self, grp):
		self.__grp = grp
	def getNum(self):
		return self.__num.get()
	def setNom(self, nom):
		self.__nom = nom
	def getNom(self):
		return self.__nom
	def getGrp(self):
		return self.__grp
	def getEstModif(self):
		return self.__estModifiable
