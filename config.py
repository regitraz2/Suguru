def getConfig() :
	name = getCurentGame()

	file = open("config.cfg", "r")  # on ouvre l'acces en lecture

	lines = file.readlines()  # récupere une liste contenant toutes les lignes du fichier de config
	length = len(lines)  # compte le nombre de lignes
	file.close()  # on ferme l'acces en lecture

	# recherche de la config specifié dans le fichier (jusqu'a la fin du fichier)
	k = 0
	lines[k] = lines[k].rstrip()
	while lines[k] != name and k < length :
		k += 1
		lines[k] = lines[k].rstrip()  # enleve les \r\n ou \n a la fin

	# renvoie la grille au format tableau 3 dimension, avec pour chaque case un couple [num_case, num-groupe]
	return configFormat(lines, k)


def getCurentGame():
	file = open("opt.cfg", "r")  # on ouvre l'acces en lecture
	lines = file.readlines()  # récupere une liste contenant toutes les lignes du fichier
	file.close()  # on ferme l'acces en lecture

	length = len(lines)  # compte le nombre de lignes

	for i in range(length) :  # pour chaque ligne
		if lines[i][0] != "#" and lines[i].split("=")[0] == "config" :  # si le texte avant le = de la ligne vaut "config"
			return lines[i].split("=")[1].rstrip()  # on met le nom de la config selectionnée dans name


#met la config choisie sous forme exploitable / enleve les caracteres inutiles / isoles les x:y (cf fichier de config)
# cad qu'on a un tableau 3 dimension, avec pour chaque case (qui compose les 2 premiere dim de notre tableau)
# un couple [num_case, num-groupe] (3eme dim)
def configFormat(lines, k):
	grid = []
	i = 1 # k est l'indice dans lines du nom de la config, donc la grille commence a la ligne d'apres
	while(lines[k+i] != "\n"): #une ligne vide signe la fin de la grille
		l = len(lines[k+i]) #nombre de caractere d'une ligne
		sgrid = [] #une ligne de la matrice
		for j in range(l):
			if lines[k+i][j] ==":": #pour chaque ':' trouver on regarde ce qu'il y a a gauche et a droite
				toappend = getGrpNum(lines[k+i], j-1)
				toappend = toappend.split(":") #on créer un tableau avec, en 0 le chiffre de la case, en 1 le numero du groupe

				# convertit le tableau en int
				for z in range(2):
					toappend[z] = int(toappend[z])
				sgrid.append(toappend) #on met ce tableau dans une ligne
		grid.append(sgrid) #on ajoute la ligne a la matrice
		i+=1
	return grid


#renvoie la chaine de caractere x:y, en prenant en compte que y peut etre > 9 (+ de un chiffre)
def getGrpNum(line, j):
	res = ""
	while line[j] != ",": #jusqu'au prochain "," recupere tout
		res += line[j]
		j+=1
	return res

