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

		#sert a dessiner les bordures
		self.__border_right = 1
		self.__border_left = 1
		self.__border_top = 1
		self.__border_bottom = 1


		#deux bouton differents selon si il est modifiable ou non
		if self.__estModifiable:
			# on créer le canvas (bd=-2 car le canvas Tkinter a un border a 2 par default) puis le bouton dedans
			self.canvas = Canvas(frame, relief = FLAT, width = 54, height = 50, bd = -2, bg="lightgray") #on le grid dans la classe grille, idem pour la frame
			self.btn = Button(self.canvas, textvariable = self.__num, height = 2, width = 5, relief = "flat", bg= "lightgray", command=lambda :self.grille.setSelected(self))
		else:
			self.canvas = Canvas(frame, relief = FLAT, width = 54, height = 50, bd = -2, bg="gray70") #on le grid dans la classe grille, idem pour la frame
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


	#dessine les bordure, 0 = petite bordure, 1 = grosse bordure
	#ce systeme dessine les grosse bordure apres (ajoute un genre de priorité) ce qui rend la grille plus jolie
	def drawBorder(self):
		if self.__border_right == 0:
			self.bdr()
		if self.__border_left == 0:
			self.bdl()
		if self.__border_bottom == 0:
			self.bdb()
		if self.__border_top == 0:
			self.bdt()
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
		self.canvas.create_line(0, 1, 54, 1, width = 2)
	def bbdb(self) :
		self.canvas.create_line(0, 49, 54, 49, width = 2)
	def bbdr(self) :
		self.canvas.create_line(53, 0, 53, 54, width = 2)
	def bbdl(self) :
		self.canvas.create_line(1, 0, 1, 54, width = 2)


	#dessine des bordure normales (pour delimiter les cases)
	def bdt(self) :
		self.canvas.create_line(0, 1, 54, 1, width = 2, fill="#cfcfcf")
	def bdb(self) :
		self.canvas.create_line(0, 49, 54, 49, width = 2, fill="#cfcfcf")
	def bdr(self) :
		self.canvas.create_line(53, 0, 53, 54, width = 2, fill="#cfcfcf")
	def bdl(self) :
		self.canvas.create_line(1, 0, 1, 54, width = 2, fill="#cfcfcf")


	#Méthodes d'accès
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
	def getNum(self):
		return self.__num.get()
	def getNom(self):
		return self.__nom
	def getGrp(self):
		return self.__grp
	def getEstModif(self):
		return self.__estModifiable
