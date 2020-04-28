import numpy as np
from classeSG import *

################ Grille  ##############

grille = np.zeros((7,4), dtype=int)

grille.itemset(1,4)
grille.itemset(3,3)
grille.itemset(5,5)
grille.itemset(7,4)
grille.itemset(9,3)
grille.itemset(10,1)
grille.itemset(11,5)
grille.itemset(22,5)
grille.itemset(25,1)

################ Grille Solution ##############

Sgrille = np.zeros((7, 4), dtype=int)

Sgrille.itemset(0,2)
Sgrille.itemset(1,4)
Sgrille.itemset(2,1)
Sgrille.itemset(3,3)
Sgrille.itemset(4,1)
Sgrille.itemset(5,5)
Sgrille.itemset(6,2)
Sgrille.itemset(7,4)
Sgrille.itemset(8,4)
Sgrille.itemset(9,3)
Sgrille.itemset(10,1)
Sgrille.itemset(11,5)
Sgrille.itemset(12,1)
Sgrille.itemset(13,2)
Sgrille.itemset(14,6)
Sgrille.itemset(15,3)
Sgrille.itemset(16,3)
Sgrille.itemset(17,4)
Sgrille.itemset(18,1)
Sgrille.itemset(19,2)
Sgrille.itemset(20,2)
Sgrille.itemset(21,6)
Sgrille.itemset(22,5)
Sgrille.itemset(23,3)
Sgrille.itemset(24,3)
Sgrille.itemset(25,1)
Sgrille.itemset(26,2)
Sgrille.itemset(27,1)

######## GRILLE 1 ##############

C1=Case(0,0,0)
C2=Case(4,0,1)
C3=Case(0,0,2)
C4=Case(3,0,3)
C5=Case(0,1,0)
C6=Case(5,1,1)
C7=Case(0,1,2)
C8=Case(4,1,3)
C9=Case(0,2,0)
C10=Case(3,2,1)
C11=Case(1,2,2)
C12=Case(5,2,3)
C13=Case(0,3,0)
C14=Case(0,3,1)
C15=Case(0,3,2)
C16=Case(0,3,3)
C17=Case(0,4,0)
C18=Case(0,4,1)
C19=Case(0,4,2)
C20=Case(0,4,3)
C21=Case(0,5,0)
C22=Case(0,5,1)
C23=Case(5,5,2)
C24=Case(0,5,3)
C25=Case(0,6,0)
C26=Case(1,6,1)
C27=Case(0,6,2)
C28=Case(0,6,3)

SG1=SG(False, 5, [C1,C2,C3,C4,C6]) 
SG2=SG(False, 1, [C5])
SG3=SG(False, 3, [C7,C10,C11])
SG4=SG(False, 6, [C8,C12,C14,C15,C16,C19])
SG5=SG(False, 4, [C9,C13,C17,C21])
SG6=SG(False, 6, [C18,C22,C23,C25,C26,C27])
SG7=SG(False, 3, [C20,C24,C28])


#def Const(x,y):
#	if (int(x)==0 and int(y)==1) or (int(x)==6 and int(y)==1) or (int(x)==1 and int(y)==1) or (int(x)==2 and int(y)==1) or (int(x)==2 and int(y)==2) or (int(x)==2 and int(y)==3) or (int(x)==1 and int(y)==3) or (int(x)==0 and int(y)==3) or (int(x)==5 and int(y)==2):
#		return True
#	else : return False