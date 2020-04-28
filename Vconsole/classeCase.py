class Case:
	
	ListeCase = []
	NbrCase = 0
	
	def __init__(self, val, x, y):
		self.val = val
		self.x = x
		self.y = y
		self.groupe = None #sous groupe auquel il appartient
		self.poss = None
		self.const = Const(int(self.x), int(self.y))
		Case.NbrCase+=1
		Case.ListeCase.append(self)

#empeche la modification d'une constante
def Const(x,y):
	if (int(x)==0 and int(y)==1) or (int(x)==0 and int(y)==5) or (int(x)==2 and int(y)==0) or (int(x)==2 and int(y)==2) or (int(x)==2 and int(y)==5) or (int(x)==3 and int(y)==1) or (int(x)==5 and int(y)==3) or (int(x)==5 and int(y)==5):
		return True
	else : return False