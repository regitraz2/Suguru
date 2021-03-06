class Group:
	def __init__(self, nom):
		#attributs
		self.__nom = nom #nom du groupe
		self.__listCases = [] #liste des case du groupe
		self.__nbElem = 0
		self.__etat = 0
	#ajoute un element et increment le nombre d'elements
	#pas de suppression car les groupes ne change pas au cour de la partie
	def ajout(self, elem):
		self.__listCases.append(elem)
		self.__nbElem += 1

	#renvoie toutes les cases concerné du groupe si il y a un doublon
	def isGroupError(self, case):
		res = []
		for elem in self.__listCases:
			if elem.getNum() == case.getNum() and elem.getNom() != case.getNom():
				res.append(elem)
		return res


	#méthodes d'accés
	def getNom(self):
		return self.__nom
	def getListe(self):
		return self.__listCases
	def getNbElem(self):
		return len(self.__listCases)
	def getEtat(self):
		return self.__etat

	def setEtat(self,etat):
		self.__etat = etat

	#Nombre d'occurence d'un possiblité parmi une liste
	def nbpossLSG(self,x):
		n = 0
		for case in self.getListe() :
			if int(x) in case.getPoss():
				n=n+1
		return n