# Premier projet
# nombre1 = input("Veuillez saisir le premier nombre: ")
# nombre2 = input("Veuillez saisir le deuxième nombre: ")
# nombre1 = int(nombre1)
# nombre2 = int(nombre2)
# resultat = f"Le résultat de l'addition du nombre {nombre1} avec le nombre {nombre2} est égal à {nombre1 + nombre2}"
# print(resultat)

# Correction:
# a = input("Entrez un premier nombre: ")
# b = input("Entrez un deuxième nombre: ")
# print(f"Le résultat de l'addition de {a} avec {b} est égal {int(a) + int(b)}")

# a = int(input("Entrez un premier nombre: "))
# b = int(input("Entrez un deuxième nombre: "))
# print(f"Le résultat de l'addition de {a} avec {b} est égal {a + b}")

from tokenize import Number


number1 = number2 = ""

while not (number1.isdigit() and number2.isdigit()):
    number1 = input("Entrez un premier nombre: ")
    number2 = input("Entrez un deuxième nombre: ")
    if not (number1.isdigit() and number2.isdigit()):
        print("Veuillez saisir des nombres valides")

print(f"Le résultat de l'addition de {number1} et de {number2} est égale à {int(number1) + int(number2)}")