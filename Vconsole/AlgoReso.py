from fonctions import *


Jeu_lance = True

while Jeu_lance:

    if bool(SG1.etat) and bool(SG2.etat) and bool(SG3.etat) and bool(SG4.etat) and bool(SG5.etat) and bool(SG6.etat) and bool(SG7.etat) :
        Jeu_lance= False
        print("grille complete")
        continue

    for case in Case.ListeCase:
        if int(case.val) != 0:
            cv = casevoisine(case)
            for caseg in case.groupe.listecase:
                if caseg != case and caseg not in cv:
                    cv.append(caseg)
            for casev in cv:
                if int(case.val) in casev.poss:
                    casev.poss.remove(int(case.val))

    for ssg in SG.ListeSG:
        if bool(ssg.etat)==False:
            controle()
            if bool(ssg.etat):
                continue
            fullblock(ssg)
            if bool(ssg.etat):
                continue
            controle()
            if bool(ssg.etat):
                continue
            unique(ssg)
            if bool(ssg.etat):
                continue
            controle()
            if bool(ssg.etat):
                continue
            crown(ssg)
            if bool(ssg.etat):
                continue
            controle()
            if bool(ssg.etat):
                continue
            Round234(ssg)
            if bool(ssg.etat):
                continue
            controle()
            if bool(ssg.etat):
                continue
            SimpleNakedPair(ssg)
            if bool(ssg.etat):
                continue
            controle()
            if bool(ssg.etat):
                continue
            SimpleHiddenPair(ssg)
            if bool(ssg.etat):
                continue
            controle()
            if bool(ssg.etat):
                continue
            NakedSingle(ssg)
            if bool(ssg.etat):
                continue
            controle()
            if bool(ssg.etat):
                continue
            HiddenSingle(ssg)
            if bool(ssg.etat):
                continue
            controle()
            if bool(ssg.etat):
                continue
            NakedPairB(ssg)
            if bool(ssg.etat):
                continue
            controle()
            if bool(ssg.etat):
                continue
            SameValueCells(ssg)
            if bool(ssg.etat):
                continue
            controle()
            if bool(ssg.etat):
                continue
            XYWing(ssg)
            if bool(ssg.etat):
                continue
            controle()
                
    
        
if Jeu_lance == False:
    for i in range(6):
        for j in range(6):
            c = getCase(i,j)
            grille.itemset((i,j),int(c.val))
    print(grille)