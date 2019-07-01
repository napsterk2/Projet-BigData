from ville import *
from random import randint

class Pays:
    
    
    def get_x(self):
        return self.name

    def set_x(self, x):
        self.name = x
    
    
    def __init__(self, name):
        self.name = name
        
        
        
        
        
    def createPays(self, nombreVilles):
        
        
        self.nombreVilles = nombreVilles
        
        self.pays = []  	
    
        nombreVilles = int(nombreVilles)       
        
        for x in range(nombreVilles):
            
            nomVille = "Ville"+str(x)
            
            
            repeat = True
            
            while repeat == True:
                
                again = False
            
                abscisse = randint(0, 99)
                ordonee = randint(0, 99)
                
                if len(self.pays) > 0:
                
                    for x in self.pays:
                        
                        if (x.x == abscisse) and (x.y == ordonee):
                            again = True
                            print("--------------------------"+str(abscisse)+" "+str(ordonee))
                            break
                        
                    if again == False:
                        break
                    
                else:
                    break
            
            
            self.pays.append(CreateVille(nomVille, abscisse, ordonee))
        
      








print ("Entrez la taille de la matrice (attention + d'1 minute d'attente apres 500) ")
nombreVilles = input()

p1 = Pays("pays1")
p1.createPays(nombreVilles)

for x in p1.pays:
    print(x.name, x.x, x.y)
