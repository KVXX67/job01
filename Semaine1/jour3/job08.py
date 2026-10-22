print("Entrez les trois longueurs du triangle :")
a = float(input("Longueur a : "))
b = float(input("Longueur b : "))
c = float(input("Longueur c : "))

if a + b > c and a + c > b and b + c > a:
    print("Il est possible de construire un triangle.")

    if a == b and b == c:
        print("Le triangle est équilatéral.")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        if a == b or b == c or a == c:
            print("Le triangle est rectangle et isocèle.")
        else:
            print("Le triangle est rectangle.")
    elif a == b or b == c or a == c:
        print("Le triangle est isocèle.")
    else:
        print("Le triangle est quelconque.")
else:
    print("Il n'est pas possible de construire un triangle avec ces longueurs.")