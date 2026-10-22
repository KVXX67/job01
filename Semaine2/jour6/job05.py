def process_list():
    L = [10, 20, 30, 40, 50]
    print(f"Deuxième valeur de la liste: {L[1]}")

    def replace_middle_element(lst):
        lst[3] = lst[2] + lst[4]
        return lst

    L = replace_middle_element(L)
    print(f"Liste après remplacement: {L}")
    print(f"Dernière valeur de la liste: {L[-1]}")

process_list()