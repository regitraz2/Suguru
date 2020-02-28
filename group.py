from case import Case

class Group:
	def __init__(self, nom):
		self.__nom = nom
		self.__list = []
		self.__nbelem = 0


	#ajoute un element et increment le nombre d'elements
	def ajout(self, elem):
		self.__list.append(elem)
		self.__nbelem += 1


	#colore les doublons d'un nombre dans le groupe
	def colorGroupError(self):
		for x in self.__list:
			for y in self.__list:
				if x != y and x.getNum() == y.getNum():
					x.bgRed()
					y.bgRed()


	#méthodes d'accés
	def getNom(self):
		return self.__nom
	def getListe(self):
		return self.__list
	def getNbElem(self):
		return self.__nbelem