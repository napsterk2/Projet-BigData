
from random import randint
import math


class Circuit:
    
    
    def get_x(self):
        return self.name

    def set_x(self, x):
        self.name = x
    
    
    def __init__(self, name, pays):
        self.name = name
        
        #self.circuit = []
        
        
        
    #def createCircuit(self, pays):
        
        
        
        print("cree circuit")
        
        circuitTemp = pays.copy()
        self.circuit = []
        
        for ville in range(len(circuitTemp)):
        
            randomVille = randint(0, len(circuitTemp)-1)
            
            self.circuit.append(circuitTemp[randomVille])
            
            circuitTemp.pop(randomVille)
           
            #print(pays[randomVille].name)
            
        #print(self.circuit)
        
        
        
        
        
        
        
        
    def calculateDistance(self):
        
        total = 0
        
        #print("calcul de la distance")
        
        for ville in range(len(self.circuit)-1):
            
        
            total = total + (math.sqrt((self.circuit[ville+1].x - self.circuit[ville].x)**2+(self.circuit[ville+1].y - self.circuit[ville].y)**2))
        
        #print(total)
        
        return total
      


