def Line(sommet : int, file : str) -> str:  # ok
    f = open(file, "r")
    if sommet == 0:
        return "0 0"
    elif sommet >= size(file):
        return ""
    else:
        return f.readlines()[sommet - 1].rstrip()


def size(file : str) -> int:  # ok
    f = open(file, "r")
    return len(f.readlines()) + 1

def finalSize(file):  # ok
    return size(file) + 1


def sommet(sommet : int, file : str) -> int:  # ok
    number = ""
    ligne = Line(sommet, file)
    SIZE = size(file)
    num = 0

    if sommet in [0, SIZE]:
        return sommet

    while ligne[num] != ' ':
        number = number + ligne[num]
        num += 1
    return int(number)


def duree(sommet, file):  # ok
    l = Line(sommet, file)
    SIZE = size(file)
    copy = ""
    duree = ""

    if sommet in [0, SIZE]:
        return 0
    copy = l[l.find(' ') + 1:]
    for i in range(len(copy)):
        if copy[i] == " ":
            break
        duree += copy[i]
    return int(duree)


def predecessors(sommet : int, file : str) -> str:  # ok
    l = Line(sommet, file)
    copy = l[l.find(' ') + 1:]
    copy1 = copy[copy.find(' ') + 1:]

    if sommet == 0: return ""
    whitespaces = sum(l[i] == ' ' for i in range(len(l)))
    return "0" if whitespaces == 1 else copy1


def predsToArray(sommet : int, file : str) -> list:  # ok
    if sommet == size(file): return addLastPredecessors(file)

    pred = predecessors(sommet, file)
    number, num, preds = 0, "", []

    if sommet == 0: return preds

    for j in range(len(pred)):
        if pred[j] == ' ':
            number = int(num)
            preds.append(number)
            num = ""
        elif pred[len(pred) - 1] != ' ' and j == len(pred) - 1:
            num += pred[j]
            number = int(num)
            preds.append(number)
        else:
            num += pred[j]
    return preds


def addLastPredecessors(file : str) -> list:  # ok
    predfinals = []
    SIZE = size(file)
    s = ""
    for i in range(SIZE):
        s += predecessors(i, file) + " "
    for j in range(1, SIZE):
        if str(j) not in s:
            predfinals.append(j)
    return predfinals


def succsToArray(sommet : int, file : str) -> list:  # ok
    return [cpt for cpt in range(finalSize(file)) if sommet in predsToArray(cpt, file)]


def Matrice(file : str):  # ok
    SIZE = finalSize(file)
    print(end="\t")
    for sommet in range(SIZE):
        print(sommet, end="\t")
    print(" <- sommets")

    for ligne in range(SIZE):
        print(ligne, end="\t")
        for colonne in range(SIZE):
            if ligne in predsToArray(colonne, file):
                print(duree(ligne, file), end="\t")
            else:
                print("_", end="\t")
        print()


def nbreArcs(file : str) -> int:  # ok
    arcs = 0
    SIZE = finalSize(file)
    for ligne in range(SIZE):
        for colonne in range(SIZE):
            if ligne in predsToArray(colonne, file):
                arcs += 1
    return arcs


def showArcs(file : str):  # ok
    SIZE = finalSize(file)
    for ligne in range(SIZE):
        for colonne in range(SIZE):
            if ligne in predsToArray(colonne, file):
                print(f"{ligne} -> {colonne} = {duree(ligne, file)}")


def uniqueEntry(file : str) -> bool:
    cpt = sum(len(predsToArray(i, file)) == 0 for i in range(finalSize(file)))
    return cpt == 1


def uniqueExit(file : str) -> bool:
    cpt = sum(len(succsToArray(i, file)) == 0 for i in range(finalSize(file)))
    return cpt == 1


"""
def rang(file):  # ok
    liste, s = [], []
    liste = [1 if 0 in predsToArray(i1, file) else 0 for i1 in range(finalSize(file))]
    for i in range(finalSize(file)):
        if i == 0:
            liste[i] = 0
        else:
            if 0 in predsToArray(i, file):
                liste[i] = 1
            else:
                for j in range(finalSize(file)):
                    if j in predsToArray(i, file) and j < i:
                        s.append(liste[j] + 1)
                    elif j in predsToArray(i, file) and j > i:
                        for k in range(0, finalSize(file)):
                            if k in predsToArray(j, file):
                                s.append(liste[k] + 2)
                liste[i] = max(s)
                s.clear()
    return liste
"""


def rangs(file : str) -> list:
    SIZE = finalSize(file)
    sommets = list(range(SIZE))

    degres = [0 for _ in range(SIZE)]
    ranks = [0 for _ in range(SIZE)]
    cpt = 0  # rang de départ

    while sommets:
        for i in sommets:
            TAB_PRED = predsToArray(i, file)
            for j in sommets:
                if j in TAB_PRED:
                    degres[sommets.index(i)] += 1  # si le sommet admet des degrés intérieurs
        if 0 not in degres:
            break
        for k in range(len(sommets)):
            if degres[k] == 0:  # si la valeur du nombre de degrés intérieurs est nulle
                ranks[sommets[k]] = cpt  # alors nous l'affectons son rang
        copy = [sommets[spt] for spt in range(len(sommets)) if degres[spt] != 0]
        sommets = copy
        degres = [0 for _ in range(len(sommets))]
        cpt += 1  # on incrémente le compteur (== rang).
    return ranks


def hasCircuit(file : str) -> bool:
    rangsCopy = rangs(file)
    SIZE_COPY = len(rangsCopy)
    zeros = sum(rangsCopy[r] == 0 for r in range(SIZE_COPY))
    return zeros > 1


def negativeArc(file : str) -> bool:
    neg = False
    for i in range(finalSize(file)):
        if duree(i, file) < 0:
            neg = True
            break
    return neg


def dictgraph(file : str) -> dict:
    dicto = {}
    ranks = rangs(file)
    for i in range(finalSize(file)):
        dicto[i] = ranks[i]
    return dicto


def sortSomms(file : str) -> dict:
    dicto = dictgraph(file)
    sortedByVal = {k: v for k, v in sorted(dicto.items(), key=lambda v: v[1])}
    return list(sortedByVal.keys())


def trierPos(file : str) -> list:  # ok
    SIZE = finalSize(file)
    indices = list(range(SIZE))
    ranks = rangs(file)

    for i in range(SIZE):
        for j in range(i + 1, SIZE):
            if ranks[indices[i]] > ranks[indices[j]]:
                indices[i], indices[j] = indices[j], indices[i]
    return indices


def datesTot(file : str) -> list:  # ok
    datesTot, lists = [], []
    ordSommets = trierPos(file)

    for start in range(finalSize(file)):
        TABLE_PRED = predsToArray(ordSommets[start], file)
        if len(TABLE_PRED) == 0 or 0 in TABLE_PRED:
            datesTot.append(0)
        else:
            for j in range(start):
                if ordSommets[j] in TABLE_PRED:
                    lists.append(datesTot[j] + duree(ordSommets[j], file))
            datesTot.append(max(lists))
            lists.clear()
    return datesTot


def datesTard(file : str) -> list:  # ok
    datesTard, lists = [], []
    datesTots = inverserListe(datesTot(file))
    ordSommets = inverserListe(trierPos(file))

    for step in range(finalSize(file)):
        ti = duree(ordSommets[step], file)
        if step == ordSommets.index(ordSommets[0]):
            datesTard.append(datesTots[step])
        elif ordSommets[step] in succsToArray(datesTots[0], file):
            datesTard.append(datesTard[0] - ti)
        else:
            for j in range(step):
                if ordSommets[j] in succsToArray(ordSommets[step], file):
                    lists.append(datesTard[j] - ti)
            datesTard.append(min(lists))
            lists.clear()
    return inverserListe(datesTard)


def inverserListe(liste):  # ok
    return [liste[i] for i in range(len(liste) - 1, 0 - 1, -1)]


def marges(file : str) -> list:  # ok
    marges = []
    diff = 0
    for dates in range(finalSize(file)):
        tTard = datesTard(file)[dates]
        tTot = datesTot(file)[dates]
        diff = tTard - tTot
        marges.append(diff)
    return marges


def chemin(file : str) -> str:  # ok
    triP = trierPos(file)
    m = marges(file)

    path = "".join(f"{str(triP[s])} " for s in range(finalSize(file)) if m[s] == 0)
    return path.rstrip()


file = input("Quel fichier voulez-vous lire ? : ")
file += ".txt"

print(""
      "Affichage du graphe 1 :\n"
      "Achiffage des prédécesseurs par sommet : 2\n"
      "Affichage des successeurs par sommet : 3\n"
      "Afficher les arcs : 4\n"
      "Afficher les rangs : 5\n"
      "Afficher les sommets ordonnées par leur rang : 6\n"
      "Afficher les dates au plus tôt : 7\n"
      "Afficher les dates au plus tard : 8\n"
      "Afficher les marges totales : 9\n"
      "Afficher le chemin critique : 10\n"
      "Afficher couples-rangs : 11\n"
      "")

exo = int(input("Votre choix ? : "))
reponse = ""
print()
while True:
    if hasCircuit(file) or negativeArc(file) or not uniqueEntry(file) or not uniqueExit(file):
        print("Cette table ne représente pas un graphe d'ordonnancement")
        break
    else:
        if exo == 1:
            Matrice(file)
        if exo == 2:
            for i in range(0, finalSize(file)):
                print(f"Prédecesseurs de {i} : {predsToArray(i, file)}")
        if exo == 3:
            for i in range(0, finalSize(file)):
                print(f"Successeurs de {i} : {succsToArray(i, file)}")
        if exo == 4:
            print(f"Nombre d'arcs = {nbreArcs(file)}")
            showArcs(file)
        if exo == 5:
            for i in range(0, finalSize(file)):
                print(i, end="\t")
            print()
            for j in range(0, finalSize(file)):
                print(rangs(file)[j], end="\t")
            print()
        if exo == 6:
            print(f"Liste des sommets ordonnés : {trierPos(file)}")
        if exo == 7:
            print(f"Les dates au plus tôt : {datesTot(file)}")
        if exo == 8:
            print(f"Les dates au plus tard : {datesTard(file)}")
        if exo == 9:
            print(f"Marges totales : {marges(file)}")
        if exo == 10:
            print(f"Chemin critique = {chemin(file)}")
        if exo == 11:
            print(f"Couples sommets/rang : {dictgraph(file)}")


    print()
    reponse = input("Voulez-vous continuer ? : o/n \n")
    if reponse.startswith("o") or reponse.startswith("O"):
        print(""
              "Affichage du graphe 1 :\n"
              "Achiffage des prédécesseurs par sommet : 2\n"
              "Affichage des successeurs par sommet : 3\n"
              "Afficher les arcs : 4\n"
              "Afficher les rangs : 5\n"
              "Afficher les sommets ordonnées par leur rang : 6\n"
              "Afficher les dates au plus tôt : 7\n"
              "Afficher les dates au plus tard : 8\n"
              "Afficher les marges totales : 9\n"
              "Afficher le chemin critique : 10\n"
              "Afficher couples-rangs : 11\n")
        exo = int(input("Votre choix ? : "))
        print()
    elif reponse.startswith("n") or reponse.startswith("N"):
        print("Au revoir !")
        break