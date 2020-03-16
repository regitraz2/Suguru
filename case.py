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
			self.bgLightGray()
		else:
			self.btn = Button(self.canvas, textvariable = self.__num, height = 2, width = 5, relief = "flat", state=DISABLED, disabledforeground="black")
			self.bgGray()

		self.btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)  #on centre le bouton dans le canvas



	#modifie la valeur de num (celle qui est affiché sur le bouton)
	def changeVal(self, num):
		self.setNum(num)
		self.grille.victory()


#region Backgrounds
	#change la couleur de fond de la case
	def bgRed(self):
		self.btn.configure(bg="#ff5c5c")
		self.canvas.itemconfigure(self.rect_id, fill="#ff5c5c")
	def bgOrange(self):
		self.btn.configure(bg="orange")
		self.canvas.itemconfigure(self.rect_id, fill="orange")
	def bgYellow(self):
		self.btn.configure(bg = "#fffa87")
		self.canvas.itemconfigure(self.rect_id, fill="#fffa87")
	def bgLightGray(self):
		self.btn.configure(bg="lightgray")
		self.canvas.itemconfigure(self.rect_id, fill="lightgray")
	def bgGray(self):
		self.btn.configure(bg="gray70")
		self.canvas.itemconfigure(self.rect_id, fill="gray70")
	def bgBlue(self):
		self.btn.configure(bg="lightblue")
		self.canvas.itemconfigure(self.rect_id, fill="lightblue")
#endregion

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
