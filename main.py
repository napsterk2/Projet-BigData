from pays import *
from circuit import *

from algoGenetique import *
from algoTournoi import *
from graph import *



p1 = Pays("pays1")
    
print ("Entrez le nombre de ville souhaités pour le pays (Optimalement le nombre de villes doit etre inferieur à 5000 ou 9000 au max)")
nombreVilles = int(input())
    
if nombreVilles > 9000:
    print("Le nombre de villes doit etre inferieur à 9000")
    print("")
    main()
else:
    
    p1.createPays(nombreVilles)
            
              
                    
circuitList = []
                
print ("Entrez le nombre de circuits souhaités")
nombreCircuits = int(input())

for x in range(nombreCircuits):

    circuitList.append(Circuit("circuit"+str(x), p1.villes))

                
    circuitList[x].calculateDistance()
    
    


        


circuitList.sort(key=lambda x: x.total, reverse=True)


algoGenetique1 = AlgoGenetique("algoGenetique1")
algoGenetique1.algoGenetique(circuitList)



for x in range(10):
    
    print(x*10,"%")

    algoTournoi1 = AlgoTournoi("algoTournoi1")
    algoTournoi1.algoTournoi(p1)



    algoTournoi1.alterElite(algoGenetique1.meilleursCircuits)

    del algoTournoi1
    
print("Odre des villes pour l'algorithme le plus optimisé : ")

for x in algoGenetique1.meilleursCircuits[0].circuit:
    print(x.name)


g = Graph("graph")
print("\nCircuit le moins optimisé :")
g.createGraph(circuitList[0].circuit)
print("Circuit le plus optimisé :")
g.createGraph(circuitList[len(circuitList)-1].circuit)
print("Circuit le plus optimisé apres algo traitement:")
g.createGraph(algoGenetique1.meilleursCircuits[0].circuit)
    
