def combinatielijst(elementenlijst, lengte):
    import itertools as it
    allecombinaties = []


    for j in it.product((elementenlijst), repeat=lengte):
        allecombinaties.append(j)
    return allecombinaties


elementenlijst = [1, 2, 3]


def pinchecker(Gokken, PCcode):
    Zwart = 0
    Wit = 0
    Algebruikt = []
    for i in range(4):
        if Gokken[i] == PCcode[i]:
            Zwart += 1
            Algebruikt.append(Gokken[i])

    for j in range(4):
        if Gokken[j] in PCcode and Gokken[j] != PCcode[j] and Gokken[j] not in Algebruikt:
            Wit += 1

    return Wit, Zwart

