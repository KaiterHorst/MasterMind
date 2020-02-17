import random
''' interface gedeelte'''
print('Dit zijn de keuzes:'
      '\n=======================================================================')
print(  'Optie 1: De computer kiest een patroon en jij gokt'
        '\nOptie 2: Kies zelf een patroon en de computer gokt, implementatie 1'
        '\nOptie 3: Kies zelf een patroon en de computer gokt, implementatie 2'
        '\nOptie 4: Kies zelf een patroon en de computer gokt, eige implementatie'
        '\n======================================================================='
        '\nKies 1, 2, 3 of 4')

optie = input(('Maak een keuze:'))

''' Optie 1'''
if optie == '1':
    print('\n''De kleuren waaruit je kan kiezen zijn: Rood(R), Blauw(B), Groen(GR), Geel(G), Oranje(O) en Paars(P)\n')
    kleuren = ['R', 'B', 'Gr', 'G', 'O', 'P']
    PCcode = []

    for i in range(4):
      PCcode.append(random.choice(kleuren))

    print(PCcode)
    for i in range(1,11):
        Gokken = []
        while len(Gokken) < 4:
            PlGok = input('Vul de combinatie in die jij denkt dat het is met spaties tussen de letters.\n Code:')
            Gokken = PlGok.split(' ')

        print(Gokken)
        Zwart = 0
        Wit = 0
        Algebruikt = []
        for i in range(4):
            if Gokken[i] == PCcode[i]:
                Algebruikt.append(Gokken[i])
                Zwart += 1

        for j in range(4):
            if Gokken[j] in PCcode and Gokken[j] != PCcode[j] and Gokken[j] not in Algebruikt:
                Wit += 1

        print('zwart:', Zwart,
            '\nwit:', Wit,)

        if Zwart == 4:
            print('Je hebt binnen 10 zetten gewonnen!')
            break
    if Zwart != 4:
        print('Helaas, je beurten zijn op.\n Nog een keertje proberen?')


'''Optie 2'''
if optie == '2':
    print(2)