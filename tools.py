#affiche un tableau en une dimension
def affiche1dim(tab1dim):
	n = len(tab1dim)
	for i in range(n):
		print(tab1dim[i], end= "\n")

#affiche un tableau en deux dimension
def affiche2dim(tab2dim):
	n = len(tab2dim)
	m = len(tab2dim[0])
	for i in range(n):
		for j in range(m):
			print(tab2dim[i], end= ", ")
		print("\n")
