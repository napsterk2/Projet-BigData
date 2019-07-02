from random import randint
import math
import copy
from graph import *
from circuit import *
from algoGenetique import *

class AlgoTournoi:
    
    def get_x(self):
        return self.name

    def set_x(self, x):
        self.name = x    
    
    def __init__(self, name):
        self.name = name         
        
    def algoTournoi(self, pays):   
        
        
        
        
        circuitList = []
                

        nombreCircuits = 5
        
        for x in range(nombreCircuits):
                    
            circuitList.append(Circuit("circuit"+str(x), pays.villes))

        
            circuitList[x].calculateDistance()
        
        
        circuitList.sort(key=lambda x: x.total, reverse=True)
        

            
        algoGenetique2 = AlgoGenetique("algoGenetique2")
        algoGenetique2.algoGenetique(circuitList)
        
        
        self.meilleurCircuit = algoGenetique2.meilleursCircuits[0]
        




    def alterElite(self, elite):
        

        
        elite.append(self.meilleurCircuit)
        
        elite.sort(key=lambda x: x.total, reverse=False)
        
        elite.pop(len(elite)-1)
        
        
        algoGenetique3 = AlgoGenetique("algoGenetique3")
        algoGenetique3.algoGenetique(elite)
        elite = algoGenetique3.meilleursCircuits
        
     