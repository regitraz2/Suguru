from tkinter import *
from grille import Grille
from options import Options


class Menu:
	def __init__(self, window):
		self.window = window #la fenetre danslaquelle est le menu

		self.load_menu()


	# créer une frame
	def create_frame(self) :
		self.frame = Frame(self.window, bg = 'forestgreen')

	# empaquetage d'une frame
	def pack_frame(self) :
		self.frame.pack(expand = YES, side = "top")


	# affiche le menu
	def load_menu(self) :
		self.create_frame()
		self.create_menu()
		self.pack_frame()  # affiche la frame/le menu

	# affiche les options
	def load_option(self) :
		# recréer/efface une frame si il y en a deja une, en créer une sinon
		self.frame.destroy()

		self.option = Options(self.window, self)

	# créer les widget du menu
	def create_menu(self) :
		self.title()
		self.btn_jouer()
		self.btn_opt()
		self.btn_quitter()

	# charge une grille selon une option ou aleatoirement
	def create_grid(self) :
		self.frame.destroy()

		cfg = self.getConfig()
		if cfg != "None" :
			self.grille = Grille(self.window, self, cfg)  # charge une config

		else :
			# self.grille = Grille(self.window) #grille aléatoire
			pass


	# liste et création des widgets utilisé
	def title(self) :
		label_title = Label(self.frame, text = "SUGURU", font = ("Courrier", 40), bg = 'forestgreen', fg = '#563535')
		label_title.pack()

	def btn_opt(self) :
		btn_opt = Button(self.frame, text = "Options", font = ("Courrier", 25), fg = '#b62546', command = self.load_option)
		btn_opt.pack(pady = 25, padx = 10, fill = 'both')

	def btn_jouer(self) :
		btn_jouer = Button(self.frame, text = "Jouer", font = ("Courrier", 25), fg = '#b62546', command = self.create_grid)
		btn_jouer.pack(pady = 25, padx = 10, fill = 'both')

	def btn_quitter(self) :
		btn_quit = Button(self.frame, text = "Quitter", font = ("Courrier", 25), fg = '#b62546', command = self.window.quit)
		btn_quit.pack(pady = 25, padx = 10, fill = 'both')

	def btn_retour(self) :
		self.btn_back = Button(self.window, text = "Menu", font = ("Courrier", 20), fg = '#b62546', command = self.load_menu)
		self.btn_back.place(x = 5, y = 5, width = 80, height = 40)

	def getConfig(self) :
		file = open("opt.cfg", "r")  # on ouvre l'acces en lecture
		lines = file.readlines()  # récupere une liste contenant toutes les lignes du fichier
		file.close()  # on ferme l'acces en lecture

		length = len(lines)  # compte le nombre de lignes

		for i in range(length) :  # pour chaque ligne
			if lines[i][0] != "#" and lines[i].split("=")[0] == "config" :  # si la ligne avant le = est egal a "config"
				return lines[i].split("=")[1].rstrip()  # renvoie l'element a droite du =

