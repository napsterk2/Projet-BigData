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
    
        
        for x in self.meilleursCircuits:
            
            print("algo genetique :---- ", x.name, x.total)
            
        self.algoGenetique1();
            
            
            
    def algoGenetique1(self):
        
        
        
        meilleurCircuitCurrent = copy.deepcopy(self.meilleursCircuits[0])
        
        lastMeilleurCircuit = copy.deepcopy(meilleurCircuitCurrent)
        
        print("jafejjkfkeef")
        
        
#        for x in self.meilleursCircuits[0].circuit:
#        
#            print(x.name)
        
        
        
        for x in range(100):
            
            randomIndex1 = randint(0, (len(meilleurCircuitCurrent.circuit)-1))
            
            randomIndex2 = randint(0, (len(meilleurCircuitCurrent.circuit)-1))
            
            while randomIndex2 == randomIndex1:
                randomIndex2 = randint(0, (len(meilleurCircuitCurrent.circuit)-1))
                
            
            villeIndex1 = meilleurCircuitCurrent.circuit[randomIndex1]
            
            villeIndex2 = meilleurCircuitCurrent.circuit[randomIndex2]
            
            meilleurCircuitCurrent.circuit[randomIndex1] = villeIndex2
            
            meilleurCircuitCurrent.circuit[randomIndex2] = villeIndex1
            
            
            total = 0
        
        #print("calcul de la distance")
        
            for ville in range(len(meilleurCircuitCurrent.circuit)-1):
            
        
                total = total + (math.sqrt((meilleurCircuitCurrent.circuit[ville+1].x - meilleurCircuitCurrent.circuit[ville].x)**2+(meilleurCircuitCurrent.circuit[ville+1].y - meilleurCircuitCurrent.circuit[ville].y)**2))
        
            meilleurCircuitCurrent.total = total

            print(meilleurCircuitCurrent.total)
            print(lastMeilleurCircuit.total)
                
            if meilleurCircuitCurrent.total <= lastMeilleurCircuit.total:
                
                lastMeilleurCircuit = copy.deepcopy(meilleurCircuitCurrent)
                
                print("changed")
                
            else:
                
                meilleurCircuitCurrent = copy.deepcopy(lastMeilleurCircuit)

                        
                        
                
            print("ours:          ", lastMeilleurCircuit.name, lastMeilleurCircuit.total)
                
#            for x in lastMeilleurCircuit.circuit:
#                
#                print("ours:          ", x.name)
                
        print("finiiiiiiiiiiiiiiiiiiiii", lastMeilleurCircuit.name, lastMeilleurCircuit.total)
            
        self.meilleursCircuits[0] = lastMeilleurCircuit
            
            
        for x in self.meilleursCircuits:
            print("nouveaux meilleurs circuits: ",x.name, x.total)
            
        g = Graph("graph")
        print("Circuit le plus optimisé apres Algo Genetique :")
        g.createGraph(self.meilleursCircuits[len(self.meilleursCircuits)-1].circuit)
        
        
        
      
      





