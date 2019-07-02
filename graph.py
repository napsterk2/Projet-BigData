import matplotlib.pyplot as plt


class Graph:
    
    
    def get_x(self):
        return self.name

    def set_x(self, x):
        self.name = x
    
    
    def __init__(self, name):
        self.name = name

        
        
    def createGraph(self, circuit):

        
        x=[]
        y=[]
        
        for items in range(len(circuit)):

            x.append(circuit[items].x)
            y.append(circuit[items].y)
            
        
    
        plt.plot(x, y, '-o')
        
        plt.plot(x[0], y[0], color='green', linestyle='dashed', marker='o', markerfacecolor='blue', markersize=12)
        
        plt.axis([0, 100, 0, 100])

        
        plt.show()

        

