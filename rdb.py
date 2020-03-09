from tkinter import *

class Rdb:
	def __init__(self, name, cfg, frame):
		self.name = name
		self.cfg = cfg #on en a besoin pour retrouver le "bon" radiobutton et le selectionner par default
		self.rdb = Radiobutton(frame, text = name, variable = 1, value = cfg, width=50, command = self.write_opt_cfg)
		self.rdb.pack()


	def select(self):
		self.rdb.select()

	# écrit l'options choisie dans le fichier opt.cfg
	def write_opt_cfg(self) :
		file = open("opt.cfg", "r") #acces en lecture
		lines = file.readlines()
		length = len(lines)
		file.close()

		for i in range(length) : # on parcourt le fichier
			if lines[i][0] != "#" and lines[i].split("=")[0] == "config" :  # coupe la chaine de caractere en deux
				lines[i] = lines[i].split("=")[0]+"="+self.cfg  # ce qu'il y a avant le = + la nouvelle valeur

		file = open("opt.cfg", "w")
		file.write(''.join(lines)) #on reecrit le fichier
		file.close()  # on ferme l'acces en lecture
		return