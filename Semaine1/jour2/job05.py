phrase = input("Entrez une phrase : ")
voyelles = "aeiouAEIOU"
compte = 0
for caractere in phrase:
    if caractere in voyelles:
        compte += 1
print(f"Le nombre de voyelles est : {compte}")