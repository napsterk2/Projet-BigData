from pays import *


print ("Entrez la taille de la matrice")
nombreVilles = input()

p1 = Pays("pays1")
p1.createPays(nombreVilles)

for x in p1.pays:
    print(x.name, x.x, x.y)
