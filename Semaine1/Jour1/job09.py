print(f"=== LA PLATEFORME MARKET ===")

nom = "Canette de RedBull"
prix_unitaire = 2.5
quantite_en_stock = 50


print("=== INFORMATIONS INITIALES DU PRODUIT ===")
print(f"Nom du produit : {nom}")
print(f"Prix unitaire : {prix_unitaire} €")
print(f"Quantité en stock : {quantite_en_stock} unités")
print()


quantite_a_acheter = int(input("Entrez la quantité de produits que vous souhaitez acheter : "))

quantite_en_stock -= quantite_a_acheter

prix_unitaire *= 1.10 # INFLATION 

print("\n=== INFORMATIONS MISES À JOUR ===")
print(f"Nom du produit : {nom}")
print(f"Prix unitaire (après inflation de 10%) : {prix_unitaire:.2f} €")
print(f"Quantité en stock (après achat de {quantite_a_acheter} unités) : {quantite_en_stock} unités")

