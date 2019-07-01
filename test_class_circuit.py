class GestionnaireCircuit:
	listeVillesParcourus[]
	
	def ajouterVille(self, ville):
		self.listeVillesParcourus.append(ville)
	
	def getVille(self, index):
		return self.listeVillesParcourus[index]

	def nombreVilles():
		return len(self.listeVillesParcourus)