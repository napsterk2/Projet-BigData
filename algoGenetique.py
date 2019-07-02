from random import randint
import math
import copy
from graph import *

class AlgoGenetique:
    
    def get_x(self):
        return self.name

    def set_x(self, x):
        self.name = x    
    
    def __init__(self, name):
        self.name = name         
        
    def algoGenetique(self, circuitListe):   
        
        
        
        self.meilleursCircuits = []
        
        for x in range(5):
            
            self.meilleursCircuits.append(circuitListe[(len(circuitListe)-1)-x])

            
        self.algoGenetique1();
            
            
            
    def algoGenetique1(self):
        
        
        for elems in range(len(self.meilleursCircuits)):
        
            meilleurCircuitCurrent = copy.deepcopy(self.meilleursCircuits[elems])
            
            lastMeilleurCircuit = copy.deepcopy(meilleurCircuitCurrent)
            

            
            
            for x in range(100):
                
                randomIndex1 = randint(1, (len(meilleurCircuitCurrent.circuit)-2))
                
                randomIndex2 = randint(1, (len(meilleurCircuitCurrent.circuit)-2))
                
                while randomIndex2 == randomIndex1:
                    randomIndex2 = randint(1, (len(meilleurCircuitCurrent.circuit)-2))
                    
                
                villeIndex1 = meilleurCircuitCurrent.circuit[randomIndex1]
                
                villeIndex2 = meilleurCircuitCurrent.circuit[randomIndex2]
                
                meilleurCircuitCurrent.circuit[randomIndex1] = villeIndex2
                
                meilleurCircuitCurrent.circuit[randomIndex2] = villeIndex1
                
                
                total = 0
            
            
                for ville in range(len(meilleurCircuitCurrent.circuit)-1):
                
            
                    total = total + (math.sqrt((meilleurCircuitCurrent.circuit[ville+1].x - meilleurCircuitCurrent.circuit[ville].x)**2+(meilleurCircuitCurrent.circuit[ville+1].y - meilleurCircuitCurrent.circuit[ville].y)**2))
            
                meilleurCircuitCurrent.total = total
    

                    
                if meilleurCircuitCurrent.total <= lastMeilleurCircuit.total:
                    
                    lastMeilleurCircuit = copy.deepcopy(meilleurCircuitCurrent)
                    

                    
                else:
                    
                    meilleurCircuitCurrent = copy.deepcopy(lastMeilleurCircuit)
    
                            
                            
                    

                
            self.meilleursCircuits[elems] = lastMeilleurCircuit
                
            
        

