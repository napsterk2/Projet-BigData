import matplotlib.pyplot as plt
from random import randint
import math


class Graph:
    
    
    def get_x(self):
        return self.name

    def set_x(self, x):
        self.name = x
    
    
    def __init__(self, name):
        self.name = name
        
        #self.circuit = []
        
        
        
    def createGraph(self, circuit):
        
        print(circuit)
        
        x=[]
        y=[]
        
        for items in range(len(circuit)):
            print(circuit[items])
            x.append(circuit[items].x)
            y.append(circuit[items].y)
            
        
    
        plt.plot(x, y, '-o')
        plt.show()

        

