from tkinter import *
import time

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
			self.btn = Button(frame, textvariable = self.__num, height = 2, width = 5, relief = "ridge", bg= "lightgray", command=self.load_change_grid)
		else:
			self.btn = Button(frame, textvariable = self.__num, height = 2, width = 5, relief = "ridge", bg="gray70", state=DISABLED, disabledforeground="black")

	#change la couleur de fond de la case
	def bgRed(self):
		self.btn.configure(bg="#ff5c5c")

	def bgLightGray(self):
		self.btn.configure(bg="lightgray")

	#affiche les boutons pour changer la valeur d'un bouton
	def load_change_grid(self):
		self.frame2 = Frame()
		Button(self.frame2, text="1", width=5, height=2, command=lambda :self.setNum(1)).grid(row=0, column=0)
		Button(self.frame2, text="2", width=5, height=2, command=lambda :self.setNum(2)).grid(row=0, column=1)
		Button(self.frame2, text="3", width=5, height=2, command=lambda :self.setNum(3)).grid(row=0, column=2)
		Button(self.frame2, text="4", width=5, height=2, command=lambda :self.setNum(4)).grid(row=1, column=0)
		Button(self.frame2, text="5", width=5, height=2, command=lambda :self.setNum(5)).grid(row=1, column=1)
		Button(self.frame2, text="6", width=5, height=2, command=lambda :self.setNum(6)).grid(row=1, column=2)
		Button(self.frame2, text="7", width=5, height=2, command=lambda :self.setNum(7)).grid(row=2, column=0)
		Button(self.frame2, text="8", width=5, height=2, command=lambda :self.setNum(8)).grid(row=2, column=1)
		Button(self.frame2, text="9", width=5, height=2, command=lambda :self.setNum(9)).grid(row=2, column=2)
		self.frame2.place(relx=0.35, rely=0.75)

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
