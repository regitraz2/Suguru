class Group:
	def __init__(self, nom):
		#attributs
		self.__nom = nom
		self.__list = []
		self.__nbelem = 0
		self.__estValide = False #dit si un groupe est correctement remplit


	#ajoute un element et increment le nombre d'elements
	def ajout(self, elem):
		self.__list.append(elem)
		self.__nbelem += 1


	#colore les doublons d'un nombre dans le groupe
	def colorGroupError(self):
		res = True #sert a determiner la victoire
		for x in self.__list:
			if x.getNum() > str(self.__nbelem): #si le numero est un chiffre dépassant le max du groupe
				x.bgBlue()
				if res is not False:
					res = False

			for y in self.__list:
				# "" est la valeur quand num n'est pas defini (cf setNum dans la classe case)
				if x.getNom() != y.getNom() and x.getNum() != "" and y.getNum() != "" and x.getNum() == y.getNum():
					x.bgOrange()
					y.bgOrange()
					if res is not False:
						res = False
		return res


	#méthodes d'accés
	def getNom(self):
		return self.__nom
	def getListe(self):
		return self.__list
	def getNbElem(self):
		return self.__nbelem