import random

class algorithme:
    def __inti(self, gestionnaire_circuit):
        self.gestionnaire_circuit= gestionnaire_circuit
        self.tauxMutation = 0.015
        self.tailleTournoi = 5
        #elitisme
        
        def selectionTournoi (self, echant):
            tournoi = Echantillon(self.gestionnaire_circuit, self.tailleTournoi, False)
            for i in range(0, self.tailleTournoi):
                randomId = int (random.random() * echant.tailleEchantillon())
                tournoi.sauvegarderCircuit(i, echant.getCircuit(randomId))
                fittest = tournoi.getFittest()
            return fittest
        
        def muter(self, circuit):
            for circuitPos1 in range(0,circuit.tailleCircuit()):
                if random.random() < self.tauxMutation:
                   circuitPos2 = int(circuit.tailleCircuit() * random.random())
                   
                   ville1 = circuit.getVille(circuitPos1)
                   ville2 = circuit.getVille(circuitPos2)
                   
                   circuit.setVille(circuitPos2, ville1)
                   circuit.setVille(circuitPos1, ville2)                

        
        
        def evoluerEchantillon (self, echant):
            nouvelleEchantillon = Echantillon(self.gestionnaire_circuit, echant.tailleEchantillon(),False)
            for i in range (0,nouvelleEchantillon.tailleEchantillon()):
                parent1 = self.selectionTournoi(echant)
                parent2 = self.selectionTournoi(echant)
                enfant = self.crossover(parent1,parent2)
            for i in range(0,nouvelleEchantillon.tailleEchantillon()):
                
                if not enfant.contientVille(parent2.getVille(i)):
                    for ii in range(0, enfant.tailleCircuit()):
                        if enfant.getVille(ii) == None:
                            enfant.setVille(ii, parent2.getVille(i))
                            break      
      return enfant
                
                
                
                