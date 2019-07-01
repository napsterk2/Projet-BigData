from pays import *
from circuit import *
from algorithme import *




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
                
for x in range(10):
                    
    circuitList.append(Circuit("circuit", p1.villes))
                    
    for y in circuitList[x].circuit:
                
        print(y.name)
                
    circuitList[x].calculateDistance()

print("\n")
algo = algorithme (p1)
algo.tournoiAleatoire(20)
                    
  