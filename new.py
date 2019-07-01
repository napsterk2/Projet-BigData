
from random import randint

class CreatePays:
    
    
    
    def __init__(self, name):
        self.name = name
    
        
        
        self.pointTable = []
    
    
    
        print ("Entrez la taille de la matrice (attention + d'1 minute d'attente apres 500) ")
        taille = input()
        
        taille = int(taille)
        
        pointTable = self.pointTable
        
        stop = False
        again = True
        
        for x in range(taille):
            
            pointTable.append([])
            
            again = True
            stop = False
            
            print(pointTable)
            
            while again == True:
                
                stop = False
            
                abscisse = randint(0, 99)
                ordonee = randint(0, 99)
                
                print(abscisse, ordonee)
                
                if len(pointTable) > 1:
            
                    while stop == False:
                        for y in (pointTable):
                        
                            print("+++++++++++++++++++++++++++++++++++++")
                
                            print("test",y);
                            
                            if len(y) > 1:
                        
                                if (abscisse == y[0]) and (ordonee == y[1]):
                        
                                    print("-----------------------------")
                                    
                                    stop = True
                                    
                                    break
                                    
                                    
                                
                       
                        if stop == False :
                            again = False
                        
                        if stop == False and again == False:
            
                            stop = True
                         
                            pointTable[x].append(abscisse)
                            pointTable[x].append(ordonee)
                            
                    print(stop)
                            
                else:
                    
                    print("willian")
                    
                    pointTable[x].append(abscisse)
                    pointTable[x].append(ordonee)
                    
                    again = False
                    
            
        print(pointTable)
        
        x_number_list = []
        y_number_list = []
        
        for x in (pointTable):
            
            x_number_list.append(x[0])
            y_number_list.append(x[1])



p1 = CreatePays("pays1")

print(p1.pointTable[5])

