def draw_triangle(height):
    if height < 1:
        return

    for i in range(height):
        spaces = " " * (height - i - 1)

        if i == height - 1:
            # Dernière ligne
            middle = "_" * (2 * i)
            print(spaces + "/" + middle + "\\")
        else:
            # Lignes intermédiaires
            middle = " " * (2 * i)
            print(spaces + "/" + middle + "\\")


if __name__ == "__main__":
    # Test avec height = 5
    draw_triangle(5)