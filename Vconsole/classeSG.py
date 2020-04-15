

class SG:
	
	ListeSG = []
	NbrSousGroupe = 0

	def __init__(self, etat=False, taille=0, listecase=[]):
		self.etat = etat
		self.taille = taille
		self.listecase = listecase
		SG.NbrSousGroupe += 1
		SG.ListeSG.append(self)


#	def getEtat(self):
#		return self.etat

#	def getTaille(self):
#		return self.taille

#	def getListeCase(self):
#		return self.listecase


	#ajoute une case a une sous-grille
	def ajoutCase(self, case):
		self.listecase.append(case)
		self.taille += 1 

	#cherche une case parmi une sous grille
	def chcase(self, cx, cy):
		for case in  self.listecase:
			if int(case.getAbs())==int(cx) and int(case.getOdr())==int(cy) :
				return True
		return False

	#retourne une case parmi une sous grille
	def rtncase(self, cx, cy):
		for case in  self.listecase:
			if int(case.getAbs())==int(cx) and int(case.getOdr())==int(cy) :
				return case

	#return true si sc est complet false sinon
	def actuEtat(self):
		p=range(1,int(self.taille))
		for case in self.listecase:
			if int(case.val)==0:
				self.etat=False
				return
			else :
				p.remove(int(case.val))
		if len(p)==0 :
			self.etat=True
		else : return
