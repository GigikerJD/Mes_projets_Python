import math

from sympy import *
from math import *

def encipher(message, keys, alphabet):
    nbr_modulo = len(alphabet)
    minuscule = message.lower()
    ciphertext = []
    new_message = ""
    y = 0

    for char in range(0,len(minuscule)):
        y = keys[0] * alphabet.index(minuscule[char]) + keys[1]
        ciphertext.append(alphabet[y%nbr_modulo])

    new_message = "".join(ciphertext)
    print(f"The ciphertext of {message} with the encrypted key {keys} is : {new_message}.")


def MessageChiffre(message, decalage):
    min_message = message.lower()
    alphabet = [chr(char) for char in range(97,122+1)]
    crypte_index = []
    crypte = []
    msg_crypte = ""
    nbr = len(alphabet)
    n = 0
    str = ""

    for k in range(0, len(message)):
        n = alphabet.index(min_message[k])+decalage
        if n >= nbr:
            crypte_index.append(n%nbr)
        else:
            crypte_index.append(n)
    for j in crypte_index:
        crypte.append(alphabet[j])

    msg_crypte = "".join(crypte)
    print(f"Le message crypté de {message} est : {msg_crypte}.")

def MessageDechiffre(message, decalage):
    alphabet = [chr(char) for char in range(97, 123)]

    msg_decrypte = ""
    crypte = []
    crypte1 = []
    t_al = len(alphabet)

    for k in range(0, len(message)):
        n = alphabet.index(message[k]) - decalage
        if n <= 0:
            crypte.append(n % t_al)
        else:
            crypte.append(n)
    crypte1 = [alphabet[j] for j in crypte]
    msg_decrypte = "".join(crypte1)
    print(f"Le message décrypté de {message} est : {msg_decrypte}.")


def PGCD(n1, n2):
    if n1 == 0 :
        return n2

    if n2 == 0 :
        return n1

    if n1 == n2:
        return n1 or n2

    if n1 > n2 :
        return PGCD(n1-n2, n2)
    else:
        return PGCD(n1, n2-n1)


def modulo(dividende, diviseur):

    if dividende > 0 and dividende < diviseur:
        return dividende
    else:
        return modulo(dividende-diviseur, diviseur)

def modulo2(dividende, divisor):
    reste = 0
    while dividende > divisor:
        dividende = dividende - divisor
        reste = dividende
    return reste


def NombrePremier(n):

    if isprime(n):
        print("{} est un nombre premier.".format(n))
    else:
        print("{} n'est pas un nombre premier.".format(n))

def EulerTotientList(n):
    cpt = 0
    integer_list = []
    for i in range(0, n+1):
        if PGCD(n,i) == 1 :
            cpt = cpt + 1
            integer_list.append(i)
        else :
            pass
    print("Nombres compris entre {} et {} sont : {}.".format(0,n,integer_list))
    print("On prend en compte {} entiers qui sont premiers avec {}.".format(cpt,n))

def EulerTotient(n):
    cpt = 0
    for i in range(1, n+1):
        if math.gcd(n, i) == 1 :
            cpt = cpt + 1
        else :
            pass
    return cpt

def EulerPrimeNumber(p, alpha):
    if isprime(p) and alpha >=0 :
        return (p-1) * (p**(alpha-1))
    else:
        return "Erreur : impossible d'exécuter le programme."

def EulerPrimeNumber1(p):
    if isprime(p) :
        return p-1
    else:
        return "Erreur : impossible d'exécuter le calcul."


def EulerTwoPrimeNumbers(a, b):
    if isprime(a) and isprime(b) and math.gcd(a, b) == 1:
        return EulerTotient(a) * EulerTotient(b)
    else :
        return "Erreur : impossible d'exécuter le programme."

def Premier(n):

    if len(Diviseurs(n)) == 2:
        print("{} est un nombre premier.".format(n))
    elif len(Diviseurs(n)) > 2 or len(Diviseurs(n)) == 1:
        print("{} n'est pas un nombre premier".format(n))


def Diviseurs(n):
    liste = []
    for i in range(1,n+1):
        if n%i == 0:
            liste.append(i)
        else:
            pass
    return liste

def Multiples(nombre, fois):
    liste_multiples = []
    for i in range(0,fois):
        liste_multiples.append(nombre*fois)
        fois = fois - 1
    return liste_multiples


def extendedEucliden(a, b):
    x, yy = 1, 1
    y, xx = 0, 0
    while b!=0:
        q = a//b
        a, b = b, a%b
        xx, x = x - q*xx, xx
        yy, y = y - q*yy, yy
    return [a,x,y]


print(f"{Diviseurs(2022)}")














