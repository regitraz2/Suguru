from classeSG import *

class Case:
	
	NbrCase = 0
	
	def __init__(self, val, x, y, sc):
		self.val = val
		self.x = x
		self.y = y
		self.groupe = sc #sous groupe auquel il appartient
		self.poss = range(1,int(sc.taille)+1)
		self.const = Const(self.x, self.y)
		Case.NbrCase +=1

#	def getAbs(self):
#		return self.x
	
#	def getOrd(self):
#		return self.y

#	def getVal(self):
#		return self.val
	
#	def getEtat(self):
#		return self.const

	#return un liste composée des possiblités de chaque cases
#	def getposs(self):
#		return self.poss

#	def getGroupe(self):
#		return self.groupe
	#efface des possibilités toutes les valeurs differentes de p
	
	def rmvreste(self,p):
		for i in self.poss:
			if i != p :
				self.poss.remove(i)