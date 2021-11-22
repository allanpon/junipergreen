# Jeu de Juniper Green
# Allan Ponchaut
# 1C1
# Mardi 8 décembre 2020

from typing import List


def multiples(n, nmax):
    """
    Fonction pour avoir les multiples de n inférieurs à nmax.

    :param n: Multiples de n
    :type n: int
    :param nmax: Multiples inférieur à nmax
    :type nmax: int
    :return: Multiples de n inférieur à nmax
    :rtype: List[int]

    :Example:
    >>> multiples(2,20)
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    """
    resultat = []
    for i in range(n, nmax + 1):
        if i % n == 0:
            resultat.append(i)
    return resultat


def diviseur(n):
    """
    Fonction pour avoir l'ensemble des diviseurs de n qui sont inférieurs à nMax.

    :param n: Diviseurs de n
    :type n: int
    :return: L'ensemble des diviseurs de n inférieur à nmax
    :rtype: List[int]

    :Exemple:
    >>> diviseur(15)
    [1, 3, 5, 15]
    """
    resultat = []
    for i in range(1, n + 1):
        if n % i == 0:
            resultat.append(i)
    return resultat


def union(l1, l2):
    """
    Fait l'union des deux ensembles.

    :param l1: Premier ensemble
    :type l1: List[int]
    :param l2: Deuxième ensemble
    :type l2: List[int]
    :return: Union des deux ensembles
    :rtype: List[int]

    :Exemple:
    >>> union([1,2,3],[4,5,6])
    [1, 2, 3, 4, 5, 6]
    """
    resultat = l1
    for i in l2:
        if i not in resultat:
            resultat.append(i)
    return resultat


def filtres(m, r):
    """
    Supprime de M tous les éléments dans R.

    :param m: Liste originel
    :type m: List[int]
    :param r: Éléments à filtrer de M
    :type r: List[int]
    :return: Liste M sans les éléments de R
    :rtype: List[int]

    :Exemple:
    >>> filtres([1,2,3,4],[3,4,5,6])
    [1, 2]
    """
    resultat = []
    for i in m:
        if i not in r:
            resultat.append(i)
    return resultat


joueurCompteur = 1                                               # Compteur pour savoir qui est le joueur actuel
nbMax = 20                                                       # Nombre max de nombres valides
nbJoue = []                                                      # Nombres déjà joués
nbChoix = 1                                                      # Nombre choisit par le joueur actuel

print("Jouons avec des nombres entre 1 et " + str(nbMax) + ".")
print("")

# Premier tour
nbValide = union(diviseur(nbChoix), multiples(nbChoix, nbMax))
nbValide = filtres(nbValide, nbJoue)
print("Nombre valides: ", nbValide)
nbChoix = int(input("Joueur 1 choisit: "))
while nbChoix % 2 != 0 or nbChoix not in nbValide:              # Nombre doit être pair et un nombre présent la liste de nombres valides
    nbChoix = int(input("Joueur 1 choisit: "))
print("")
nbJoue.append(nbChoix)

while True:
    nbValide = union(diviseur(nbChoix), multiples(nbChoix, nbMax))
    nbValide = filtres(nbValide, nbJoue)
    joueurCompteur += 1

    if joueurCompteur % 2 != 0:                                 # Joueur 1
        if len(nbValide) == 0:                                  # On vérifie si la liste de nombre valides est vide et si le joueur 2 a gagné
            print("Bravo joueur 2 !")
            break
        print("Nombre valides: ", nbValide)
        nbChoix = int(input("Joueur 1 choisit: "))
        while nbChoix in nbJoue or nbChoix not in nbValide:     # Nombre ne doit pas être un nombre déjà joué ou un nombre qui n'est pas présent dans la liste de nombres valides
            nbChoix = int(input("Joueur 1 choisit: "))
        nbJoue.append(nbChoix)
        print("")

    if joueurCompteur % 2 == 0:                                 # Joueur 2
        if len(nbValide) == 0:                                  # On vérifie si la liste est vide et si le joueur 1 a gagné
            print("Bravo joueur 1 !")
            break
        print("Nombre valides: ", nbValide)
        nbChoix = int(input("Joueur 2 choisit: "))
        while nbChoix in nbJoue or nbChoix not in nbValide:     # Nombre ne doit pas être un nombre déjà joué ou un nombre qui n'est pas présent dans la liste de nombres valides
            nbChoix = int(input("Joueur 2 choisit: "))
        nbJoue.append(nbChoix)
        print("")
