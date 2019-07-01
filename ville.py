class CreateVille:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.name

    def set_x(self, x):
        self.name = x
    

ville1 = CreateVille("Tamere", 10, 50)

print (ville1.get_x())

ville1.set_x("ouaf")

print (ville1.get_x())