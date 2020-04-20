class Group:
	def __init__(self, nom):
		#attributs
		self.__nom = nom #nom du groupe
		self.__list = [] #liste des case du groupe
		self.__nbElem = 0

	#ajoute un element et increment le nombre d'elements
	#pas de suppression car les groupes ne change pas au cour de la partie
	def ajout(self, elem):
		self.__list.append(elem)
		self.__nbElem += 1


	#renvoie toutes les cases concerné du groupe si il y a un doublon
	def isGroupError(self, case):
		res = []
		for elem in self.__list:
			if elem.getNum() == case.getNum() and elem.getNom() != case.getNom():
				res.append(elem)
		return res


	#méthodes d'accés
	def getNom(self):
		return self.__nom
	def getListe(self):
		return self.__list
	def getNbElem(self):

		return len(self.__list)