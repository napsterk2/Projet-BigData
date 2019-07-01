from random import randint

print ("Entrez la taille de la matrice")
taille = input()

taille = int(taille)

pointTable = []

for x in range(taille):
    
    pointTable.append([])
    
    pointTable[x].append(randint(0, 99))
    pointTable[x].append(randint(0, 99))
    
print(pointTable)