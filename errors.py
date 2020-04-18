from error import Error

#Ce code peut sembler avoir une haute complexité, mais comme nous travaillon sur de petits tableaux la plupart
# du temps (a moins que l'utilisateur fasse exprè de déclencher plein d'erreur)
#cela reste bien moin gourmand en ressources que la premiere facon de gérer les erreurs
class listErrors:
	def __init__(self):
		#listes de toutes les erreurs
		self.__AdjErr = []
		self.__GrpErr = []

		#sert a determiner la victoire
		self.__nbError = 0

	#créer une erreur si elle n'existe pas deja
	def createError(self, case1, case2, group=""):
		#si une erreur sur ces deux cases existe deja, on ne fait rien
		for err in self.__AdjErr:
			if err.getCase1().getNom() == case1.getNom() and err.getCase2().getNom() == case2.getNom():
				return #arrete la fonction
		if group != "": #onne teste dans le tableau groupe que si c'est une erreur de groupe
			for err in self.__GrpErr:
				if err.getCase1().getNom() == case1.getNom() or err.getCase2().getNom() == case2.getNom():
					return #arrete la fonction

		#il y a seulement deux type d'erreurs, si on laisse la valeur par defaut c'est une erreur d'adjascence
		if group == "":
			typeErreur = "adjascence"
		else:
			typeErreur = "group"

		#création de l'erreur
		err = Error(typeErreur, group)
		err.add(case1, case2)

		#ajout de l'erreur dans le tableau aproprié
		self.__nbError += 1
		if group == "":
			self.__AdjErr.append(err)
		else:
			self.__GrpErr.append(err)
		print(self.__nbError)
		print("listGrp : ")
		for err in self.__GrpErr : err.print()
		print("listAdj : ")
		for err in self.__AdjErr : err.print()


	#supprime toutes les erreur de self.__AdjErr qui contiennent case
	def deleteAdjError(self, case):
		#supprime toute les erreurs d'adjascence contenant case
		tmp = []
		for err in self.__AdjErr:
			if err.getCase1().getNom() == case.getNom() or err.getCase2().getNom() == case.getNom():
				#si notre case n'a pas le meme num que l'erreur, on supprime
				if case.getNum() != err.getNumCase1() and case.getNum() != err.getNumCase2():
					#on ajout l'erreur dans une liste d'erreur que l'on supprimera plus tard
					tmp.append(err)

		#on supprime
		for err in tmp:
			self.delete(self.__AdjErr, err)


		self.recolore()#actualisation graphique

	#supprime toute les erreurs de groupe qui contienne case
	def deleteGrpError(self, case, grp):
		tmp = []
		for err in self.__GrpErr:
			if grp == err.getGrp():
				if err.getCase1().getNom() == case.getNom() or err.getCase2().getNom() == case.getNom():
					# si notre case n'a pas le meme num que l'erreur, on supprime
					if case.getNum() != err.getNumCase1() and case.getNum() != err.getNumCase2():
						tmp.append(err)
		#on supprime
		for err in tmp:
			self.delete(self.__GrpErr, err)

		self.recolore() #actualisation graphique


	#supprime l'erreur err du tableau tab
	def delete(self, tab, err):
		# on peut de nouveau recolorie la case
		err.getCase1().setErr(False)
		err.getCase2().setErr(False)

		# recolore en gris
		err.getCase1().draw("default")
		err.getCase2().draw("default")

		tab.remove(err)
		self.__nbError -= 1

		print(self.__nbError)
		print("listGrp : ")
		for err in self.__GrpErr : err.print()
		print("listAdj : ")
		for err in self.__AdjErr : err.print()


	#actualise les couleurs des erreurs (pour etre plus precis, recolore toutes les cases qui ont été supprimer
	# d'une autre erreur que celles restantes dans la tableau, et qui on donc leur parametre hasErr a False
	def recolore(self):
		#recolore les erreurs de groupe en orange
		for err in self.__GrpErr:
			if err.getCase1().getErr() == False:
				err.getCase1().draw("group")
			if err.getCase2().getErr() == False :
				err.getCase2().draw("group")

		#recolore les d'adjascence en rouge
		for err in self.__AdjErr:
			if err.getCase1().getErr() == False:
				err.getCase1().draw("adjascence")
			if err.getCase2().getErr() == False :
				err.getCase2().draw("adjascence")

	def getNb(self):
		return self.__nbError