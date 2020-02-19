def combinatielijst(elementenlijst,lengte):
# Deze functie genereert een lijst met alle combinaties in (elementenlijst) met de lengte (lengte).
#bron https://www.hackerrank.com/challenges/itertools-product/problem
    import itertools as it
    allecombinaties = []

    for j in it.product((elementenlijst), repeat=lengte):
        allecombinaties.append(j)
    return allecombinaties


def pinchecker(Gokken, PCcode):

    Zwart = 0
    Wit = 0
    Tlijst = []

    for i in range(4):
        Tlijst.append(PCcode[i])

    for i in range(4):
        if Gokken[i] == PCcode[i]:
            Zwart += 1
            Tlijst.remove(Gokken[i])

    for j in range(4):
        if Gokken[j] in Tlijst and Gokken[j] != PCcode[j]:
            Wit += 1

    return Wit, Zwart



