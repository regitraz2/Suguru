from tkinter import *
import time

class Case:
	def __init__(self, frame, nom, num, estModifiable, i, j, grille):
		#attributs
		self.__num = StringVar() #chaine de caractere dynamique (quand la var change, le texte du bouton aussi)
		self.grille = grille
		self.__estModifiable = estModifiable
		self.__nom = nom
		self.__posX = i
		self.__posY = j
		self.setNum(num)

		#deux bouton differents selon si il est modifiable ou non
		if self.__estModifiable:
			self.btn = Button(frame, textvariable = self.__num, height = 2, width = 5, relief = "ridge", bg= "lightgray", command=lambda :self.grille.setSelected(self))
		else:
			self.btn = Button(frame, textvariable = self.__num, height = 2, width = 5, relief = "ridge", bg="gray70", state=DISABLED, disabledforeground="black")

	#change la couleur de fond de la case
	def bgRed(self):
		self.btn.configure(bg="#ff5c5c")
	def bgOrange(self):
		self.btn.configure(bg="orange")
	def bgYellow(self):
		self.btn.configure(bg = "#fffa87")
	def bgLightGray(self):
		self.btn.configure(bg="lightgray")
	def bgGray(self):
		self.btn.configure(bg="gray70")

	def changeVal(self, num):
		self.setNum(num)
		self.grille.victory()


	#Méthodes d'accès
	def setNum(self, num):
		self.__num.set(num)
	def getNum(self):
		return self.__num.get()
	def setNom(self, nom):
		self.__nom = nom
	def getNom(self):
		return self.__nom
	def getEstModif(self):
		return self.__estModifiable
