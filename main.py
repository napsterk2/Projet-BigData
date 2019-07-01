from pays import *


def main():

    p1 = Pays("pays1")
    
    print ("Entrez le nombre de ville souhaités pour le pays (Optimalement le nombre de villes doit etre inferieur à 5000 ou 9000 au max)")
    nombreVilles = int(input())
    
    if nombreVilles > 9000:
        print("Le nombre de villes doit etre inferieur à 9000")
        print("")
        main()
    else:
    
        p1.createPays(nombreVilles)
    
        for x in p1.pays:
            print(x.name, x.x, x.y)

main()