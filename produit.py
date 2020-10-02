"""Création d'une fontion qui fait le multiple de 2 nombre par des additions"""
def multiplication(m, n):
    index = 1
    produit = 0
    while index <= n:
        produit = produit + m
        index += 1
    return produit

print(multiplication(4, 4))