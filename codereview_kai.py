def combinatielijst(elementenlijst, lengte):
    import itertools as it
    allecombinaties = []

    for j in it.product((elementenlijst), repeat=lengte): # Zet alle mogelijke combinaties in een lijst
        allecombinaties.append(j)
        
    return allecombinaties


def pinchecker(Gok, PCcode):
    Zwart = 0
    Wit = 0
    Algebruikt = []
    
    for i in range(4):
        if Gok[i] == PCcode[i]: 
            Zwart += 1
            Algebruikt.append(Gok[i])
            
        elif Gokken[j] in PCcode and Gokken[j] != PCcode[j] and Gokken[j] not in Algebruikt:: 
            Wit += 1
        
    return Wit, Zwart

