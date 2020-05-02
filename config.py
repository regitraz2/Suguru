import random


def getConfig():
    name = getCurentGame()

    if (name == "None"):
        name = getRandomGame()

    file = open("config.cfg", "r")  # on ouvre l'acces en lecture

    # récupere une liste contenant toutes les lignes du fichier de config
    lines = file.readlines()
    length = len(lines)  # compte le nombre de lignes
    file.close()  # on ferme l'acces en lecture

    # recherche de la config specifié dans le fichier (jusqu'a la fin du fichier)
    k = 0
    lines[k] = lines[k].rstrip()
    while k < length and lines[k] != name:
        k += 1
        lines[k] = lines[k].rstrip()  # enleve les \r\n ou \n a la fin

    # renvoie la grille au format tableau 3 dimension, avec pour chaque case un couple [num_case, num-groupe]
    return configFormat(lines, k)


def getCurentGame():
    file = open("opt.cfg", "r")  # on ouvre l'acces en lecture
    lines = file.readlines()  # récupere une liste contenant toutes les lignes du fichier
    file.close()  # on ferme l'acces en lecture

    length = len(lines)  # compte le nombre de lignes

    for i in range(length):  # pour chaque ligne
        # si le texte avant le = de la ligne vaut "config"
        if lines[i][0] != "#" and lines[i].split("=")[0] == "config":
            # on met le nom de la config selectionnée dans name
            return lines[i].split("=")[1].rstrip()


# met la config choisie sous forme exploitable / enleve les caracteres inutiles / isoles les x:y (cf fichier de config)
# cad qu'on a un tableau 3 dimension, avec pour chaque case (qui compose les 2 premiere dim de notre tableau)
# un couple [num_case, num-groupe] (3eme dim)
def configFormat(lines, k):
    grid = []
    i = 1  # k est l'indice dans lines du nom de la config, donc la grille commence a la ligne d'apres
    while(lines[k+i] != "\n"):  # une ligne vide signe la fin de la grille
        l = len(lines[k+i])  # nombre de caractere d'une ligne
        sgrid = []  # une ligne de la matrice
        for j in range(l):
            # pour chaque ':' trouver on regarde ce qu'il y a a gauche et a droite
            if lines[k+i][j] == ":":
                toappend = getGrpNum(lines[k+i], j-1)
                # on créer un tableau avec, en 0 le chiffre de la case, en 1 le numero du groupe et en 2 un booleen si on charge une grille
                toappend = toappend.split(":")

                # convertit le tableau en int
                toappend[0] = int(toappend[0])
                toappend[1] = int(toappend[1])

                sgrid.append(toappend)  # on met ce tableau dans une ligne
        grid.append(sgrid)  # on ajoute la ligne a la matrice
        i += 1
    return grid


# renvoie la chaine de caractere x:y, en prenant en compte que y peut etre > 9 (+ de un chiffre)
def getGrpNum(line, j):
    res = ""
    while line[j] != ",":  # jusqu'au prochain "," recupere tout
        res += line[j]
        j += 1
    return res


def getRandomGame():
    file = open("opt.cfg", "r")  # on ouvre l'acces en lecture
    lines = file.readlines()  # récupere une liste contenant toutes les lignes du fichier
    file.close()  # on ferme l'acces en lecture

    length = len(lines)  # compte le nombre de lignes

    for i in range(length):  # pour chaque ligne
        # si le texte avant le = de la ligne vaut "level"
        if lines[i][0] != "#" and lines[i].split("=")[0] == "level":
            # on met le nom du level selectionnée dans lvl
            lvl = lines[i].split("=")[1].rstrip()
            break

    file = open("config.cfg", "r")  # on ouvre l'acces en lecture

    # récupere une liste contenant toutes les lignes du fichier de config
    lines = file.readlines()
    length = len(lines)  # compte le nombre de lignes
    file.close()  # on ferme l'acces en lecture

    # recherche de le level specifié dans le fichier (jusqu'a la fin du fichier)
    k = 0
    lines[k] = lines[k].rstrip()
    while lines[k] != lvl and k < length:
        k += 1
        lines[k] = lines[k].rstrip()  # enleve les \r\n ou \n a la fin

    configs = []
    while k < length and lines[k+1][0:3] != "lvl":
        k += 1
        if lines[k][0] != "#" and lines[k][0:3] == "cfg":
            configs.append(lines[k].rstrip())

    return random.choice(configs)
