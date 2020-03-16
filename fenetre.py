from tkinter import *
from menu import Menu


class Fenetre :
	def __init__(self) :
		# création de la fenetre
		self.create_window()

		# par default : le menu
		Menu(self.window)


	def create_window(self) :
		self.window = Tk() #fenetre

		#quelques parametres
		self.window.title("Suguru")
		self.window.minsize(450, 600)
		self.window.maxsize(620, 600)
		self.window.geometry("450x600")

		self.window.update() # actualise la fenetre, cela permet d'utiliser la taille de la fenetre inscrite ci-dessu par la suite

		# tailles de la fenetre
		windowWidth = self.window.winfo_width()
		windowHeight = self.window.winfo_height()

		# calcul des coordonnée pour que la fenetre soit centrée
		positionRight = int(self.window.winfo_screenwidth() / 2 - windowWidth / 2)
		positionDown = int(self.window.winfo_screenheight() / 2 - windowHeight / 2)

		# Positionnement au centre de l'ecran
		self.window.geometry("+{}+{}".format(positionRight, positionDown))

		# image de background
		self.bg_image = PhotoImage(file = 'image/bg.png')
		label_background = Label(image = self.bg_image)
		label_background.place(x = 0, y = 0, relwidth = 1, relheight = 1)

