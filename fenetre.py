from tkinter import *
from grille import Grille



class Fenetre :
	def __init__(self) :
		# création de la fenetre
		self.create_window()

		# par default : le menu
		self.load_menu()


	def create_window(self) :
		self.window = Tk() #fenetre

		#quelques parametres
		self.window.title("Suguru")
		self.window.minsize(450, 600)
		self.window.maxsize(620, 600)
		self.window.geometry("450x600")
		self.window.iconbitmap("image/logo.ico")

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


	#créer une frame
	def create_frame(self) :
		self.frame = Frame(self.window, bg = 'forestgreen')


	# empaquetage d'une frame
	def pack_frame(self) :
		self.frame.pack(expand = YES, side = "top")


	#affiche le menu
	def load_menu(self) :
		#recréer/efface une frame si il y en a deja une, en créer une sinon
		try :
			self.frame.destroy()
			self.create_frame()
		except AttributeError :
			self.create_frame()

		#detruit le bouton de retour au menu si il existe
		try:
			self.btn_back.destroy()
		except:
			pass

		#detruit la grille si elle existe
		try:
			self.grille.getFrame().destroy()
		except:
			pass

		self.create_menu()
		self.pack_frame() #affiche la frame/le menu


	#affiche les options
	def load_option(self) :
		#recréer/efface une frame si il y en a deja une, en créer une sinon
		try :
			self.frame.destroy()
			self.create_frame()
		except AttributeError :
			self.create_frame()

		self.create_option()
		self.pack_frame() #affiche la frame/les options


	#créer les widget du menu
	def create_menu(self) :
		self.title()
		self.btn_jouer()
		self.btn_opt()
		self.btn_quitter()


	#créer les widget des options
	def create_option(self):
		self.btn_retour()


	#charge une grille selon une option ou aleatoirement
	def create_grid(self):
		self.frame.destroy()
		self.btn_retour()

		#reste a implementer les options
		#créer une grille selon une config ou non
		cfg = "cfg2"
		if cfg:
			self.grille = Grille(self.window, cfg)
		else:
			self.grille = Grille(self.window)


	#liste et création des widgets utilisé
	def title(self) :
		label_title = Label(self.frame, text = "SUGURU", font = ("Courrier", 40), bg = 'forestgreen', fg = '#563535')
		label_title.pack()


	def btn_opt(self) :
		btn_opt = Button(self.frame, text = "options", font = ("Courrier", 25), fg = '#b62546', command = self.load_option)
		btn_opt.pack(pady = 25, padx = 10, fill = 'both')


	def btn_jouer(self) :
		btn_jouer = Button(self.frame, text = "Jouer", font = ("Courrier", 25), fg = '#b62546', command = self.create_grid)
		btn_jouer.pack(pady = 25, padx = 10, fill = 'both')


	def btn_quitter(self) :
		btn_quit = Button(self.frame, text = "Quitter", font = ("Courrier", 25), fg = '#b62546', command = self.window.quit)
		btn_quit.pack(pady = 25, padx = 10, fill = 'both')


	def btn_retour(self) :
		self.btn_back = Button(self.window, text = "Menu", font = ("Courrier", 20), fg = '#b62546', command = self.load_menu)
		self.btn_back.place(x=5, y=5, width=80, height=40)
