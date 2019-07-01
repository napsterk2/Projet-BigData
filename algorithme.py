import random
from pays import *
from circuit import *

class algorithme:
    elites = []      
        
    def __init__(self, pays):          
        self.pays= pays
        
    #Génére aléatoire n (paramètre taille) circuit dans le pays de l'agorithme
    #Renvoie celui a la distance la plus courte
    def tournoiAleatoire (self, taille):
        circuitListTemp = []
        for i in range (0,taille):
            
            circuitListTemp.append(Circuit(i,self.pays.villes))            
            
            print(circuitListTemp[i].calculateDistance())                
            
            #On met a jour si necessaire la liste des élites
            if  self.getBigestElite() != 0 and (circuitListTemp[i].calculateDistance() < self.getBigestElite()):
                indexInsert=ii=0                
                while(ii<10 and self.elites[ii] != None):
                    if self.elites[ii].calculateDistance() >circuitListTemp[i].calculateDistance():
                        indexInsert = ii            
                    ii += 1                                
                self.elites.insert(indexInsert,circuitListTemp[i])                
                del self.elites[-1] 
                print("nouvel elite\n")
            elif self.getBigestElite() == 0:
                self.elites.append(circuitListTemp[i])
                print("nouvel elite\n")      
                
        
            if i == 0:
               bestCircuitTournoi=circuitListTemp[i]
            else :
                if circuitListTemp[i].calculateDistance() < bestCircuitTournoi.calculateDistance():
                    bestCircuitTournoi=circuitListTemp[i]
                    
        print("meilleur circuit :")
        print (bestCircuitTournoi.calculateDistance())
        return bestCircuitTournoi
                    
    #renvoie l'élite au parcours le plus long
    def getBigestElite (self):
        #la méthode renvoie zéro si l'array n'est pas remplie
        if len(self.elites) < 10:
            return 0
        bigestElite = 0
        for i in range (10):
            if self.elites[i].calculateDistance() >bigestElite :
                bigestElite = self.elites[i].calculateDistance()
        return bigestElite

                
                
                