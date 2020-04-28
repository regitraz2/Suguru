from grille2 import *

#test l'existence d'une case		
def Existe(x,y):
	if int(x)<0 or int(x)>5 or int(y)<0 or int(y)>5 :
		return False 
	else : return True 

#retourne la case en fonction de deux coordonnées
def getCase(x,y):
	for ssg in SG.ListeSG:
		for case in ssg.listecase:
			if int(case.x)==int(x) and int(case.y)==int(y):
				return case

#liste de cases voisines
def casevoisine(case):
	x=int(case.x)
	y=int(case.y)

	listecv=[]
	
	if bool(Existe((x-1),(y-1))):
		listecv.append(getCase((x-1),(y-1)))		
	
	if bool(Existe((x),(y-1))):
		listecv.append(getCase((x),(y-1)))		
	
	if bool(Existe((x+1),(y-1))):
		listecv.append(getCase((x+1),(y-1)))				
	
	if bool(Existe((x-1),(y))):
		listecv.append(getCase((x-1),(y)))			
	
	if bool(Existe((x+1),(y))):
		listecv.append(getCase((x+1),(y)))			
	
	if bool(Existe((x-1),(y+1))):
		listecv.append(getCase((x-1),(y+1)))			
	
	if bool(Existe((x),(y+1))):
		listecv.append(getCase((x),(y+1)))				
	
	if bool(Existe((x+1),(y+1))):
		listecv.append(getCase((x+1),(y+1)))		
	
	return listecv
	
#Nombre d'occurence d'un possiblité parmi une liste
def nbpossLSG(ssg,x):
	n = 0
	for case in ssg.listecase :
		if int(x) in case.poss:
			n=n+1
	return n

#controle
def controle():	
	for ssg in SG.ListeSG:
		n=0
		for case in ssg.listecase:
			if int(case.val)==0:
				if len(case.poss)==1 :
					case.val=int(case.poss[0])
				else:
					cv = casevoisine(case)
					for caseg in case.groupe.listecase:
						if case != caseg and (caseg not in cv) :
							cv.append(caseg)
					for casev in cv:
						if int(casev.val) in case.poss:
							case.poss.remove(int(casev.val))
		
			else: n=n+1
		if n==int(ssg.taille):
			ssg.etat=True

	
#Techiques de resoltion

def fullblock(ssg):
	for case in ssg.listecase :
		if int(case.val)==0 and len(case.poss)==1 :
				case.val=int(case.poss[0])

def unique(ssg):
	for case in ssg.listecase :
		if int(case.val)==0:
			for p in case.poss:
				if int(nbpossLSG(ssg,p))==1:
					case.poss=[int(p)]
					case.val=int(p)
					break

def crown(ssg):
	for case in ssg.listecase:
		if int(case.val)==0:
			cv = casevoisine(case)
			for caseg in case.groupe.listecase:
				if caseg != case and (caseg not in cv):
					cv.append(caseg)
			for c in cv:
				if int(c.val) != 0 and int(case.poss.count(int(c.val)))==1:
						case.poss.remove(int(c.val))

def Round234(ssg):
	for case in ssg.listecase:
		if int(case.val)==0:
			for p in case.poss :
				cv = casevoisine(case)
				for cctr in cv:
					if cctr in case.groupe.listecase:
						cv.remove(cctr)
				
				for c in cv :
					voisine = []
					pasvoisine = []
					for v in c.groupe.listecase :					
						if v in cv:
							voisine.append(v)
						else :
							if p in v.poss :
								break
							else: 
								pasvoisine.append(v)
				
					if int(len(voisine))>1 and (int(len(voisine))+int(len(pasvoisine)))== int(c.groupe.taille):
						x=0
						for voi in voisine :
							if p in voi.poss :
								x=x+1
						if int(x)>1 and p in case.poss:
							case.poss.remove(int(p))

							 
def	SimpleNakedPair(ssg):
	pair=[]
	otr=[]
	for case in ssg.listecase:
		if len(case.poss)==2 :
			pair.append(case)
		else : otr.append(case)

	if len(pair)==2 and int(pair[0].poss[0])==int(pair[1].poss[0]) and int(pair[0].poss[1])==int(pair[1].poss[1]):
		for case in otr:
			if int(case.val)==0:
				for p in case.poss:
					if int(p)==int(pair[0].poss[0]) or int(p)==int(pair[0].poss[1]):
						case.poss.remove(int(p))

def SimpleHiddenPair(ssg): # a voir plu tard pour le cas ou il y a plus d'une pair par groupe
	for case in ssg.listecase:
		pair=[]
		numerospair=[]
		if int(case.val)==0 :
			for p in case.poss:
				if nbpossLSG(ssg,int(p))==2 and p not in numerospair:
					numerospair.append(p)
			if len(numerospair)==2:
				for casev in ssg.listecase:
					if int(numerospair[0]) in casev.poss and int(numerospair[1]) in casev.poss and casev not in pair :
						pair.append(casev)
				if len(pair)==2:
					for c in pair:
						for q in c.poss:
							if q not in numerospair:
								c.poss.remove(q)
							

def NakedSingle(ssg):
	for case in ssg.listecase:
		if len(case.poss)==1 and int(case.val)==0 :
			case.val=int(case.poss[0])

def HiddenSingle(ssg):
	for i in range(1,int(ssg.taille)+1):
		if int(nbpossLSG(ssg,int(i)))==1:
			for case in ssg.listecase:
				if int(case.val)==0:
					if int(i) in case.poss:
						case.val=int(i)
						case.rmvreste(int(i))
				
def NakedPairB(ssg):
	for case in ssg.listecase:
		if len(case.poss)==2 and int(case.val)==0:
			cv = casevoisine(case)
			for casev in cv:
				if len(casev.poss)==2 and int(casev.poss[0])==int(case.poss[0]) and int(casev.poss[1])==int(case.poss[1]) and casev.groupe != case.groupe:
					cv2 = casevoisine(casev)
					for v in cv :
						if v != casev and v in cv2 :
							for p in v.poss:
								if int(p) in case.poss:
									v.poss.remove(int(p)) 


def SameValueCells(ssg):
	for case in ssg.listecase:
		if int(case.val)==0:
			cv = casevoisine(case)
			voisine=[]
			pasvoisine=[]
			for casev in cv:
				if casev not in case.groupe.listecase :
					for v in casev.groupe.listecase:
						if v in cv :
							voisine.append(v)
						if v not in cv :
							pasvoisine.append(v)
					if len(voisine)==(int(casev.groupe.taille)-1) and len(pasvoisine)==1 :
						for p in pasvoisine[0].poss :
							if int(p) not in case.poss:
								pasvoisine[0].poss.remove(int(p))
					else :
						voisine=[]
						pasvoisine=[]

def XYWing(ssg):
	for case in ssg.listecase:
		if len(case.poss)==2 and int(case.val)==0 :
			cv = casevoisine(case)
			serres=[]
			for casev in cv:
				if len(casev.poss)==2 and casev not in cv:
					serres.append(casev)
			for v in serres :
				p = int(v.poss[0])
				q = int(v.poss[1])
				for v2 in serres:
					if v2 != v :
						if (p in case.poss and q in v2.poss) or (q in case.poss and p in v2.poss) :
							cvv1 = casevoisine(v)
							cvv2 = casevoisine(v2)
							for e in cvv1:
								if e in cvv2:
									if (p in case.poss and q in v2.poss) and q in e.poss:
										e.poss.remove(q)
									elif p in e.poss and (q in case.poss and p in v2.poss) :
										e.poss.remove(p)




