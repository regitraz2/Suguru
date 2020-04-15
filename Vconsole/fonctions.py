from grilles import *



#test l'existence d'une case		
def Existe(x,y):
	if int(x)<0 or int(x)>=7 or int(y)<0 or int(y)>=4 :
		return False 
	else : return True 


#renvoi faux si un voisin est egale 
def EgalVoisin(a,b,y):
	if bool(Existe((int(a)-1),(int(b)-1))):
		if int(grille.item((int(a)-1),(int(b)-1)))==int(y):
			return False
	if bool(Existe((int(a)-1),(int(b)))):
		if int(grille.item((int(a)-1),(int(b))))==int(y):
			return False
	if bool(Existe((int(a)-1),(int(b)+1))):
		if int(grille.item((int(a)-1),(int(b)+1)))==int(y):
			return False
	if bool(Existe((int(a)),(int(b)-1))):
		if int(grille.item((int(a)),(int(b)-1)))==int(y):
			return False
	if bool(Existe((int(a)),(int(b)+1))):
		if int(grille.item((int(a)),(int(b)+1)))==int(y):
			return False
	if bool(Existe((int(a)+1),(int(b)-1))):
		if int(grille.item((int(a)+1),(int(b)-1)))==int(y):
			return False
	if bool(Existe((int(a)+1),(int(b)))):
		if int(grille.item((int(a)+1),(int(b))))==int(y):
			return False
	if bool(Existe((int(a)+1),(int(b)+1))):
		if int(grille.item((int(a)+1),(int(b)+1)))==int(y):
			return False
	return True

#empeche la modification d'une constante
def Const(x,y):
	if (int(x)==0 and int(y)==1) or (int(x)==6 and int(y)==1) or (int(x)==1 and int(y)==1) or (int(x)==2 and int(y)==1) or (int(x)==2 and int(y)==2) or (int(x)==2 and int(y)==3) or (int(x)==1 and int(y)==3) or (int(x)==0 and int(y)==3) or (int(x)==5 and int(y)==2):
		return True
	else : return False



############################################################################################################################################
	#retourne la case en fonction de deux coordonnées
	def getCase(x,y):
		for sg in SG.ListeSG:
			for case in sg:
				if int(case.x)==int(x) and int(case.y)==int(y):
					return case

#liste de cases voisines
	def casevoisine(case):
		
		cv=list()
		if bool(Existe((int(case.x)-1),(int(case.y)-1))):
			cv.append(getCase((int(case.x)-1),(int(case.y)-1)))		
		if bool(Existe((int(case.x)),(int(case.y)-1))):
			cv.append(getCase((int(case.x)),(int(case.y)-1)))		
		if bool(Existe((int(case.x)+1),(int(case.y)-1))):
			cv.append(getCase((int(case.x)+1),(int(case.y)-1)))				
		if bool(Existe((int(case.x)-1),(int(case.y)))):
			cv.append(getCase((int(case.x)-1),(int(case.y))))			
		if bool(Existe((int(case.x)+1),(int(case.y)))):
			cv.append(getCase((int(case.x)+1),(int(case.y))))			
		if bool(Existe((int(case.x)-1),(int(case.y)+1))):
			cv.append(getCase((int(case.x)-1),(int(case.y)+1)))			
		if bool(Existe((int(case.x)),(int(case.y)+1))):
			cv.append(getCase((int(case.x)),(int(case.y)+1)))				
		if bool(Existe((int(case.x)+1),(int(case.y)+1))):
			cv.append(getCase((int(case.x)+1),(int(case.y)+1)))		
		return cv
	
	#Nombre d'occurence d'un possiblité parmi une liste
	def nbpossLSG(SG,x):
		n = 0
		for case in SG.getListeCase() :
			n+=int(case.getposs().count(x))
		return n

	#Techiques de resoltion
	
	def fullblock(SG):
		for case in SC.getListeCase() :
			if len(case.getposs())==1 and int(case.getVal())!=int(case.getposs()[0]):
				case.val=case.getposs()[0]

	def unique(SG):
		for case in SC.getListeCase() :
			for p in case.getposs():
				if int(nbpossLSG(SG,p))==1:
					case.val=p
					case.rmvreste(p)

	def crown(case):
		cv = casevoisine(case)
		for c in cv:
			if int(c.val) != 0:
				if case.poss.count(c.val)>0:
					case.poss.remove(c.val)

	def Round234(case):

		for p in case.poss :
			cv = casevoisine(case)
			for c in cv:
				if c.groupe == case.groupe:
					cv.remove(c)
				
			for c in cv :
				voisine = []
				pas_voisine = []
				for v in c.groupe :					
						if v in cv:
							voisine.append(v)
						if v not in cv :
							if p in v.poss :
								break
							else: pas_voisine.append(v)
				
				if len(voisine)>1 :
					x=0
					for c in voisine :
						if p in c.poss :
							x+=1
					if x>1:
						case.poss.remove(p)
						break


	def	SimpleNakedPair(SG):
		pair=[]
		otr=[]
		for case in SG.listecase:
			if len(case.poss)==2 :
				pair.append(case)
			else : otr.append(case)

		if len(pair)==2 and pair[0].poss[0]==pair[1].poss[0] and pair[0].poss[1]==pair[1].poss[1]:
			for case in otr:
				for p in case.poss:
					if int(p)==int(pair[0].poss[0]) or int(p)==int(pair[0].poss[1]):
						case.poss.remove(p)

	def SimpleHiddenPair(SG): # a voir plu tard pour le cas ou il y a plus d'une pair par groupe
		pair=[]
		numerospair=[]
		for i in range(1,int(SG.taille)+1):
			if int(nbpossLSG(SG,i))==2:
				numerospair.append(i)
				for case in SG.listecase:
					for p in case.poss:
						if int(p)==i and case not in pair :
							pair.append(case)

		if len(pair)==2:
			for case in pair:
				for p in case.poss:
					if p not in numerospair:
						case.poss.remove(p)

	def NakedSingle(SG):
		for case in SG.listecase:
			if len(cass.poss)==1 and int(case.val)==0 :
				case.val=cass.poss[0]

	def HiddenSingle(SG):
		for i in range(1,int(SG.taille)+1):
			if int(nbpossLSG(SG,i))== 1:
				for case in SG.listecase:
					if i in case.poss:
						case.rmvreste(i)
						case.val=i
				
	def NakedPairB(SG):
		for case in SG.listecase:
			if len(case.poss)==2:
				cv = casevoisine(case)
				for casev in cv:
					if len(casev.poss)==2 and int(casev.poss[0])==int(case.poss[0]) and int(casev.poss[1])==int(case.poss[1]) and case.groupe != case.groupe:
						cv2 = casevoisine(casev)
						for v in cv :
							if v != casev and v in cv2 :
								for p in v.poss:
									if p in case.poss:
										v.remove(p)



