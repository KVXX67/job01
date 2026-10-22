# Job 06: Fonction de vérification du signe
def verifier_signe(nombre):
    if nombre > 0:
        print("Le nombre est positif")
    elif nombre < 0:
        print("Le nombre est négatif")
    else:
        print("Le nombre est zéro")

# Appel de la fonction plusieurs fois avec différents paramètres
verifier_signe(10)
verifier_signe(-5)
verifier_signe(0)
verifier_signe(3.14)
verifier_signe(-2.5)