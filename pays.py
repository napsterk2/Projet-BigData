from ville import *
from random import randint

class CreatePays:
    
    
    def get_x(self):
        return self.name

    def set_x(self, x):
        self.name = x
    
    
    def __init__(self, name, nombreVilles):
        self.name = name
        
        self.nombreVilles = nombreVilles
        
    
        nombreVilles = int(nombreVilles)
        
        
        
        
        
        for x in range(nombreVilles):
            
            self.append(CreateVille("Tamere", 10, 50))
        
      

ville2 = CreateVille("Tamere", 10, 50)

print ("Entrez la taille de la matrice (attention + d'1 minute d'attente apres 500) ")
nombreVilles = input()

p1 = CreatePays("pays1", nombreVilles)


