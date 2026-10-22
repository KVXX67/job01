def rectangle(width, height):
    """Dessine un rectangle avec des bordures en caractères ASCII."""

    # V largeur m
    if width < 2 or height < 1:
        return

    # Ligne horizontale
    horizontal = "|" + "-" * (width - 2) + "|"

    # Ligne du milieu 
    middle = "|" + " " * (width - 2) + "|"

    # ligne en haut
    print(horizontal)

    # Lignes du milieu 

    for _ in range(height - 2):
        print(middle)

    # ligne du bsa
    if height > 1:
        print(horizontal)

if __name__ == "__main__":
    rectangle(10, 3)