while True:
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
        import random
        from src import functies as func
        print('\n''De kleuren waaruit je kan kiezen zijn: Rood(R), Blauw(B), Groen(GR), Geel(G), Oranje(O) en Paars(P)'
              '\n')
        kleuren = ['R', 'B', 'Gr', 'G', 'O', 'P']
        PCcode = []

        for i in range(4):
            PCcode.append(random.choice(kleuren))

        print(PCcode)
        for i in range(1, 11):
            Gokken = []
            while len(Gokken) < 4:
                PlGok = input('Vul jouw gok in met spaties tussen de kleuren:')
                Gokken = PlGok.split(' ')

            print(PCcode)
            print('zwart:', func.pinchecker(Gokken, PCcode)[1],
                '\nwit:', func.pinchecker(Gokken, PCcode)[0])

            if func.pinchecker(Gokken, PCcode)[1] == 4:
                print('Je hebt binnen 10 zetten gewonnen!')
                break

        print('Helaas, je beurten zijn op. De code was,', PCcode, '\nNog een keertje proberen?')


    '''Optie 2'''
    if optie == '2':
        import random
        from src import functies as func






