from math import sqrt
import math
import numpy as np


def ord(x, n, e):
    i = 1
    a = x
    while i < n:
        a = (x ** i) % n
        if a == e:
            print("ord({}) est {}".format(x, i))
            i = n
        i = i + 1
    print("fin precesse")

ord(13,20,1)


def prime_factors(n):
    prime = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            prime.append(d)
            n //= d
        d += 1
    if n > 1:
        prime.append(n)
    return prime


def hashe(l):
    a = sorted(set(l), key=l.index)
    return a


def power(n, l):
    a = l.count(n)
    return a


def DecFacPremier(n):
    p = prime_factors(n)
    a = hashe(p)
    x = ""
    for i in range(len(a)):
        x = x + (str(a[i]) + '^' + '{' + str(power(a[i], p))) + '}'
        if i != len(a) - 1:
            x = x + '\\' + 'times'
    return x




def pgcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def estpremier(a):
    n = 2
    top = sqrt(a)
    while (n <= top):
        if a % n == 0:
            return False
        else:
            n += 1
    return True


def phi(n):
    retour = 1
    i = 2
    while (i < n):
        if (pgcd(i, n) == 1):
            retour += 1
        i += 1
    return retour


def inv(x, n):
    i = 1
    retour = -1
    while (i <= n):
        if ((x * i) % n == 1):
            retour = i
            i = n + 1
        else:
            i = i + 1
    return retour


def enc(message, eb, k, g, n):
    b = (eb ** k) % n
    y = (message * b) % n
    r = (g ** k) % n
    print("({},{})".format(r, y))

enc(768,1776,2003,3412,5657)

def dec(r, y, da, n):
    x = y * inv(r ** da, n)
    print(f"{x % n}")

dec(4615,6190,46,7159)

e = math.e


def findDa(g, y):
    return np.log(y) / np.log(g)

