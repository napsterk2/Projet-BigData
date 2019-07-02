from pays import *
from circuit import *
#################################################
from algoGenetique import *
from algoTournoi import *
from graph import *

#
#from algorithme import *
#

#################################################


p1 = Pays("pays1")
    
print ("Entrez le nombre de ville souhaités pour le pays (Optimalement le nombre de villes doit etre inferieur à 5000 ou 9000 au max)")
nombreVilles = int(input())
    
if nombreVilles > 9000:
    print("Le nombre de villes doit etre inferieur à 9000")
    print("")
    main()
else:
    
    p1.createPays(nombreVilles)
            
for x in p1.villes:
    print(x.name, x.x, x.y)
                    
                    
                    
circuitList = []
                
print ("Entrez le nombre de circuits souhaités")
nombreCircuits = int(input())

for x in range(nombreCircuits):
                    
#################################################
#    circuitList.append(Circuit("circuit"+str(x), p1.pays))
#
    circuitList.append(Circuit("circuit"+str(x), p1.villes))
#################################################
                    
#    for y in circuitList[x].circuit:
#                
#        print(y.name)
                
    circuitList[x].calculateDistance()


################################################

#print("\n")
#algo = algorithme(p1)
#algo.tournoiAleatoire(20)

################################################              


circuitList.sort(key=lambda x: x.total, reverse=True)

for x in circuitList:
    
    print(x.name, x.total)

algoGenetique1 = AlgoGenetique("algoGenetique1")
algoGenetique1.algoGenetique(circuitList)

algoTournoi1 = AlgoTournoi("algoTournoi1")
algoTournoi1.algoTournoi(p1)

    
g = Graph("graph")
print("\nCircuit le moins optimisé :")
g.createGraph(circuitList[0].circuit)
print("Circuit le plus optimisé :")
g.createGraph(circuitList[len(circuitList)-1].circuit)
    
