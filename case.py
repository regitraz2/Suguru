from tkinter import *


class Case:
	def __init__(self, frame, nom, num, estModifiable, i, j):
		self.__num = StringVar() #chaine de caractere dynamique (quand la var change, le texte du bouton aussi)

		self.__estModifiable = estModifiable
		self.__nom = nom
		self.__posX = i
		self.__posY = j
		self.setNum(num)

		#deux bouton differents selon si il est modifiable ou non
		if self.__estModifiable:
			self.btn = Button(frame, textvariable = self.__num, height = 2, width = 5, relief = "ridge", bg= "lightgray")
		else:
			self.btn = Button(frame, textvariable = self.__num, height = 2, width = 5, relief = "ridge", bg="gray70", state=DISABLED, disabledforeground="black")


	def bgRed(self):
		self.btn.configure(bg="#ff5c5c")

	def bgLightGray(self):
		self.btn.configure(bg="lightgray")


	#Méthodes d'accès
	def setNum(self, num):
		if num > 0 and self.__estModifiable is False: #tests sur la case (la verification du chiffre se fait dans les groupes)
			self.__num.set(num)
	def getNum(self):
		return self.__num.get()
	def setNom(self, nom):
		self.__nom = nom
	def getNom(self):
		return self.__nom
	def getEstModif(self):
		return self.__estModifiable