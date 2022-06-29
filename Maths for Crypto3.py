import math
import sympy

def modarithmetics(n, x, res):
    list_reste, list_values = [], []
    for i in range(0,n):
        if ((i*x)%n == res):
            list_values.append(i)
        list_reste.append((i*x)%n)
    print(list_reste)
    print(f"Le résultat est : {list_values}")

def fermatprimenumber(n, p):
    if sympy.isprime(p)==True:
        return p
    else:
        return None

def invmod(n, x):
    if math.gcd(n,x) == 1 :
        print(f"{x} est inversible.")
    else:
        print(f"{x} n'est pas inversible.")


def eng_alphabet():
    alphabet = [chr(i).upper() for i in range(97,123)]
    alphabet.append(" ")
    alphabet.append(".")
    for j in range(0,len(alphabet)) :
        print(f"{j} : {alphabet[j]}")
    print()

eng_alphabet()
