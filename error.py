

#Une erreur concerne 2 cases, il peut y avoir plusieurs erreurs d'adjascence sur la meme case
#mais pas une erreur de groupe et d'adjascence en meme temps, l'erreur d'adjascence a la priorité
class Error:
	def __init__(self, type, group=""):
		self.__type = type
		self.__group = group
		self.__case1 = None
		self.__case2 = None
		self.__numCase1 = ""
		self.__numCase2 = ""

	#on supprime l'erreur, recolore la case
	#le cas ou la case a plusieurs erreures est traité ailleur

	def add(self, case1, case2):
		self.__case1 = case1
		self.__case2 = case2

		if(case2 != ""):
			self.__numCase1 = case1.getNum()
			self.__numCase2 = case2.getNum()

			if(self.__group != ""): #cas d'erreur de groupe
				self.__case1.draw("group")
				self.__case2.draw("group")
			else: #cas d'erreur d'adjascence
				self.__case1.draw("adjascence")
				self.__case2.draw("adjascence")

		else: #cas erreur out (du max du groupe)
			self.__numCase1 = case1.getNum()
			self.__case1.draw("out")


	def print(self):
		print("err type : {}".format(self.__type))
		print(self.__case1.getNom(), end=", ")
		print(self.__case1.getNum(), end=", ")
		print(self.__numCase1)
		if (self.__case2 != ""): #cas erreur out (du max du groupe)
			print(self.__case2.getNom(), end=", ")
			print(self.__case2.getNum(), end=", ")
			print(self.__numCase2)


	def getType(self):
		return self.__type
	def getGrp(self):
		return self.__group
	def getCase1(self):
		return self.__case1
	def getCase2(self):
		return self.__case2
	def getNumCase1(self):
		return self.__numCase1
	def getNumCase2(self):
		return  self.__numCase2