
from random import randint
import math


class Circuit:
    
    
    def get_x(self):
        return self.name

    def set_x(self, x):
        self.name = x
    
    
    def __init__(self, name, pays):
        self.name = name
        

        
        circuitTemp = pays.copy()
        self.circuit = []
        
        
        randomVille = 0
            
        self.circuit.append(circuitTemp[randomVille])
            
        circuitTemp.pop(randomVille)
        
        
        for ville in range(len(circuitTemp)):
        
            randomVille = randint(0, len(circuitTemp)-1)
            
            self.circuit.append(circuitTemp[randomVille])
            
            circuitTemp.pop(randomVille)
           
        
        self.circuit.append(self.circuit[0])
        
        
        
        
        
        
    def calculateDistance(self):
        
        self.total = 0
   
        
        for ville in range(len(self.circuit)-1):
            
        
            self.total = self.total + (math.sqrt((self.circuit[ville+1].x - self.circuit[ville].x)**2+(self.circuit[ville+1].y - self.circuit[ville].y)**2))
        
