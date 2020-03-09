from tkinter import *
from rdb import Rdb
from menu import Menu

class Options:
	def __init__(self, window, menu):
		self.window = window #la fenetre dans laquelle seront afficher les options
		self.rdb_list = [] #liste des radiobutton
		self.menu = menu

		self.frame = Frame()
		self.frame.pack(expand=YES, side = TOP)

		#par default, on affiche les options
		self.load_opt()


	#charge l'affichage des option
	def load_opt(self):
		self.label_title()
		self.btn_retour()
		self.create_rdBtn_group(1)

	#créer un groupe de radiobouton
	def create_rdBtn_group(self, num):
		#on precharge les radiobutton
		file = open("config.cfg", "r")
		lines = file.readlines()
		file.close()
		length = len(lines)

		# on créer un radiobutton pour la generation automatique
		self.create_radioBtn("Générer", "None")
		k = 1 #correspond au numero du radiobutton créer
		for i in range(length): #pour chaque lignes
			if lines[i][0] == "c" and lines[i][1] == "f" and lines[i][2] == "g": #si la ligne comence par cfg
				self.create_radioBtn("Config "+str(k), "cfg"+str(k)) #on créer un radiobutton
				k += 1

		#on definit le bouton selectionné
		file = open("opt.cfg", "r")

		for line in file:
			if line[0] != "#" and line.split("=")[0] == "config":#coupe la chaine de caractere en deux
				cfg = line.split("=")[1].rstrip()
				for x in self.rdb_list:
					if x.cfg == cfg:
						x.select()
		file.close()


	#créer un radiobouton
	def create_radioBtn(self, name, cfg):
		#sur click appele la fonction write_opt_cfg() qui réécrit le fichier opt.cfg avec la nouvelle config
		rdb = Rdb(name, cfg, self.frame)

		self.rdb_list.append(rdb) #on l'ajoute dans la liste des radiobutton


	#affiche le titre
	def label_title(self):
		label_title = Label(self.frame, text = "OPTIONS", font = ("Courrier", 40), fg = '#563535')
		label_title.pack(anchor=N)

	#recharge le menu
	def btn_retour(self) :
		self.btn_back = Button(self.window, text = "Menu", font = ("Courrier", 20), fg = '#b62546', command = self.load_menu)
		self.btn_back.place(x = 5, y = 5, width = 80, height = 40)


	def load_menu(self):
		self.btn_back.destroy()
		self.frame.destroy()
		self.menu.load_menu()