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
        self.villes = []  	
    
        nombreVilles = int(nombreVilles)       
        
        for x in range(nombreVilles):            
            nomVille = "Ville"+str(x)                    
            repeat = True
            
            while repeat == True:                
                again = False            
                abscisse = randint(0, 99)
                ordonee = randint(0, 99)
                
                if len(self.villes) > 0:                
                    for x in self.villes:                        
                        if (x.x == abscisse) and (x.y == ordonee):
                            again = True
                            print("--------------------------"+str(abscisse)+" "+str(ordonee))
                            break
                        
                    if again == False:
                        break
                    
                else:
                    break           
            
            self.villes.append(Ville(nomVille, abscisse, ordonee))
        
      





