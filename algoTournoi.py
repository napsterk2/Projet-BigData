from random import randint
import math
import copy
from graph import *
from circuit import *

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
        
        print(circuitList)





