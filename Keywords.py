import keyword
import os

f = open("python_keywords.txt","w")

for kw in keyword.kwlist:
    f.write(f"{kw} : {keyword.kwlist.index(kw)}\n")

f.close()

if f.closed :
    print("Bien joué")
else:
    print("Dommage, essayez à nouveau")

if not f.closed :
    print("Error : try closing file")
else :
    print("Bien joué à nouveau")

if os.path.exists("python_keywords.txt"):
    print("Super : votre fichier est présent")
else:
    print("Error : try create file")