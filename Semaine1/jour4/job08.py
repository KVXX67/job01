def fruits_legumes(type_produit, saison):
    if type_produit == "fruits" and saison == "hiver":
        return "orange, mandarine et kiwi"
    elif type_produit == "fruits" and saison == "été":
        return "Poire, fraise, cassis"
    elif type_produit == "légume" and saison == "hiver":
        return "carotte, topinambour, endive"
    elif type_produit == "légume" and saison == "été":
        return "artichaut, aubergine, navet"
    else:
        return "Combinaison non reconnue"

print(fruits_legumes("fruits", "hiver"))
print(fruits_legumes("fruits", "été"))
print(fruits_legumes("légume", "hiver"))
print(fruits_legumes("légume", "été"))
print(fruits_legumes("fruits", "printemps"))  