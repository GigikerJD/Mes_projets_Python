def ValeurMinimale(L):
    vmin = L[0]
    for j in range(0,len(L)):
        if L[j] < vmin :
            vmin = L[j]
    return vmin

def ValeurMaximale(L):
    vmax = L[0]
    for i in range(0,len(L)):
        if L[i] > vmax:
            vmax = L[i]
    return vmax

print(ValeurMaximale([15, 4, 8, 9, 6]))
print(ValeurMinimale([15, 4, 8, 9, 6]))

def TrierListe(L):
    new_l = []
    while (len(L) != 0):
        a0 = ValeurMinimale(L)
        new_l.append(a0)
        L.remove(a0)
    return new_l

def ListUniqueElements(liste):
    l = []
    for i in range(0,len(liste)):
        if liste[i] not in l :
            l.append(liste[i])
        else:
            pass
    return TrierListe(l)


def TrierListeInverse(L):
    new_l = []
    while(len(L) != 0):
        a0 = ValeurMaximale(L)
        new_l.append(a0)
        L.remove(a0)
    return new_l

print(TrierListe([15,4,8,9,6]))
print(TrierListeInverse([15,4,8,9,6]))
print(ListUniqueElements([90,56,75,20,20,15,15,36,42,45]))