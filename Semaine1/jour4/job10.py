def verifier_pair_impair(nombre):
    if not isinstance(nombre, int) or nombre <= 0:
        return "Erreur : veuillez entrer un entier positif"

    if nombre % 2 == 0:
        return f"Le nombre {nombre} est pair"
    else:
        return f"Le nombre {nombre} est impair"

print(verifier_pair_impair(4))
print(verifier_pair_impair(7))
print(verifier_pair_impair(0))  
print(verifier_pair_impair(-3)) 
print(verifier_pair_impair(4.5))
print(verifier_pair_impair(10))