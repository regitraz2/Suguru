from classeCase import *

class SG:
	
	ListeSG = []
	NbrSousGroupe = 0

	def __init__(self, etat, taille, listecase):
		self.etat = etat
		self.taille = taille
		self.listecase = listecase
		SG.NbrSousGroupe += 1
		SG.ListeSG.append(self)
		for case in self.listecase:
			if bool(case.const):
				case.poss = [int(case.val)]
			else : case.poss = [int(i) for i in range(1,int(self.taille)+1)]
			case.groupe = self
