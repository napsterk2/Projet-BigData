
from random import randint
print(randint(0, 9))

print ("Entrez la taille de la matrice")
taille = input()

taille = int(taille)

test = "   "

#print (test)

adj = ([])

matrixArray = []

for x in range(taille):
    
    for x in range(taille):
        
        matrixArray.append(randint(0, 9))
        
    adj.append(matrixArray)
    matrixArray = []

#adj = ([[0, 1, 1, 0, 0, 0],
#        [1, 0, 0, 1, 0, 0],
#        [1, 0, 0, 0, 1, 0],
#        [0, 1, 0, 0, 1, 0],
#        [0, 0, 1, 1, 1, 1],
#        [0, 0, 0, 0, 1, 0]])

increment = 0
for i in adj:
    increment = increment + 1
    
    test = test +"X"+str(increment)+" "
    

print(test)

increment = 0
for i in adj:
    increment = increment + 1
    
    print("X"+str(increment),i)
    #print (adj[i])