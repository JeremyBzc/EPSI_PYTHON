# TD COURS PYTHON 14/10/22 Jérémy BruzacB

# ===Partie 01: COURS + Partie 02: Exercices===

#  01 Spécifier le type:

y = int(20)
print(y)

x = ["apple", "banana", "cherry"]
print(x)
print(type(y))

z = 3 + 5j
print(type(z))

# 02 Conversion
x = float(1)
y = int(2.8)
z = complex(1)

print(x) # donne 1.0
print(y) # donne 2
print(z) # donne (1.0j)

# 03 Type string
a = """blabla
llslsslxlsxl
"""
print(a)

b = '''blabla
lorem ipsum
'''
print(b)

c = "Salut"
print(c[1])

# 04 Boucle
for t in "Banana":
    print(t)

# 05 Afficher la longueur de la chaine "Lait"

test = "J'aime la thune"
print(len(test))

# 06 Détecter un mot dans cette phrase

a = "Voilà la phrase"
print(a.__contains__("Voilà"))

# 07 J'aimerais afficher quelque chose de plus sympa qu'un true ou False

a = "Voilà la seconde phrase"
if "la" in a:
    print("Trouvé")

b = "Voilà la seconde phrase"
if "Camion" not in a:
    print("Pas trouvé")

# 08 Le "slicing"

a = "Exemple"
print(a[2:4]) # affiche "em"

# 09 Comment afficher la position d'un caractère ?

b = "Exemple"
print(b[3])

# 10 Si je peux afficher pl d' "Exemple", au moins 2 solutions...j'aimerais partir "à l'envers" de la chaîne

c = "Exemple"
print(c[-3:-1])

# 11 Tests Bool
print(bool("Hello")) # True
print(bool(12)) # True
print(bool(0)) # False
print(bool(None)) # False
print(bool("")) # False
print(bool(False)) # False
print(bool()) # False
print(bool(())) # False
print(bool([])) # False
print(bool({})) # False

def maFonction() :
    return  True
print(maFonction())


# 12 Les tuples
aa = (3,4,7)
print(type(aa))
bb,cc = 5,6
(bb,cc) = (5,6)

def test():
    return 5,6

for i in aa:
    print(i)

# 13 Tuple avec un seul élément
a = (3,)

print(type(a)) # donne <class 'tuple'>

# 14 Récupérer l'élément unique présent dans le tuple

c=b[0]


#=====================================================#
#=====================EXERCICES=======================#
#=====================================================#


# [Exercice-00] Afficher un nombre aléatoire entre 1 et 10
import random
print(random.randrange(1, 10)) # donne un chiffre aléatoire, entre 1 et 10, à chaque exécution


# [EXERCICE 01] J'aimerais tester si un nombre est un entier
is_in_integer = 12

if  int == type(is_in_integer):
    print("C'est un entier")
else:
    print("Ce n'est pas un entier")


"""[EXERCICE 02] Déclarer différents types de variables. La variable 'prenom' qui doit contenir la chaîne de caractère Pierre
la variable 'age' qui doit contenir le nombre 20. La variable 'majeur' qui doit contenir un boolean vraie. La variable 'compte_en_banque 
qui doit contenir le nombre décimal 20135,384.
La variable 'amis' qui doit contenir une liste contenant trois chaîne de caractères: Marie, Julien et Adrien
La variable 'parents' qui doit contenir un tuple contenant deux chaînes de caractères : Marc et Caroline) """

prenom = "Pierre"
age = int(20)
majeur = True



# [EXERCICE 03] : Variable d'un type vers un autre. Après avoir déclaré une variable afficher "Le nombre est 17"

nombre = 17

print('Le nombre est', nombre)



# [EXERCICE 04] : Trouver la valeur de la variable. On veut "printer" la valeur que contient la variable a

a = 3
b = 6
a = b
b = 7

print(a)

# [EXERCICE 05] : Comment printer les valeurs ? et leur somme d'un coup ? On veut afficher "2 + 6 + 3"
# Contrainte: utiliser une nouvelle fonctionnalité de Python3

a = 2
b = 6
c = 3

print(a,b,c, sep=" + ")

# [EXERCICE 06]

list1 = range(3) # on doit renommer list en list1 car list est un mot réservé dans Python...
list2 = range(5)
print(list(list2))

# [EXERCICE 07] : Vérifier qu'une variable est bien d'un certain type
prenom = "Bernard"

if type(prenom) == str:
    print("C'est bien une string")
elif type(prenom) == int:
    print("C'est un entier")
else:
    print("Ce n'est ni un entier, ni une string")

# [EXERCICE 08] : Remplacer un mot par un autre dans la chaîne "Salut les devs". Remmplace Salut par Bonsoir

ma_phrase = "salut les devs, salut ça va"
ma_nouvelle_phrase = ma_phrase[0:5] + ' les devs ça va ?'
print(ma_nouvelle_phrase)

ma_phrase = "salut les devs, salut ça va"
ma_nouvelle_phrase = ma_phrase.replace("salut", "Bonsoir", 1) # On remplace le premier salut par "Bonsoir"
print(ma_nouvelle_phrase)