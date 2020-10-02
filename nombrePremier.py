"""Cette fontion calcule et affiche une list de nombre premier"""

def nombrePremier(nombre):
    for nombre in range(1, 101):#Creation de la boucle d'intervall 1 à 100
        if nombre % 2 == 0: # Verication si x est divisible par 2, s'il es un nombre premier. 
            premier = nombre
            #print(premier)
    return premier
print(nombrePremier([13,15,12,14,50,41,53]))