def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : division par zéro"
    elif operator == "%":
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur : modulo par zéro"
    else:
        return "Opérateur non reconnu"

print(calcule(10, "+", 5))
print(calcule(10, "-", 5))
print(calcule(10, "*", 5))
print(calcule(10, "/", 5))
print(calcule(10, "%", 3))
print(calcule(10, "/", 0))  