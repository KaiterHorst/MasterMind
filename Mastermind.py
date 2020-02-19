while True:
    ''' interface gedeelte'''
    print('Dit zijn de keuzes:'
          '\n=======================================================================')
    print('Optie 1: De computer kiest een patroon en jij gokt'
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

        print('\nDe kleuren waaruit je kan kiezen zijn: Rood(R), Blauw(B), Groen(GR), Geel(G), Oranje(O) en Paars(P)'
              '\nEen zwart pinnetje betekent dat een kleur de goede kleur is en op de goede plek zit'
              '\nEen wit pinnetje betekent dat een kleur in de code zit maar op de foute plek.')
        kleuren = ['R', 'B', 'GR', 'G', 'O', 'P']
        PCcode = []

        for i in range(4):
            PCcode.append(random.choice(kleuren))

        print(PCcode)
        for i in range(1, 11):
            Gokken = []
            while len(Gokken) != 4:
                PlGok = input('Vul jouw gok in met spaties tussen de kleuren:')
                Gokken = PlGok.split(' ')
            print(Gokken)
            print(PCcode)
            print('zwart:', func.pinchecker(Gokken, PCcode)[1],
                  '\nwit:', func.pinchecker(Gokken, PCcode)[0])

            if func.pinchecker(Gokken, PCcode)[1] == 4:
                print('Je hebt binnen 10 zetten gewonnen!')
                break

        if func.pinchecker(Gokken, PCcode)[1] != 4:
            print('Helaas, je beurten zijn op. De code was,', PCcode, '\nNog een keertje proberen?')

        else:
            print('Nog een keertje spelen?')

    '''Optie 2'''
    if optie == '2':
        import random
        from src import functies as func
        print(  '\nDe kleuren waaruit je kan kiezen zijn: Rood(R), Blauw(B), Groen(GR), Geel(G), Oranje(O) en Paars(P)'
                '\nEen zwart pinnetje betekent dat een kleur de goede kleur is en op de goede plek zit'
                '\nEen wit pinnetje betekent dat een kleur in de code zit maar op de foute plek.'
                '\nKies een code die de computer moet raden.'
                '\nVul de code in als: X X X X'
                '\nGeef feedback als: Wit, Zwart')

        PLcode =input('Vul je code in:')
        code = []
        kleuren = ['R', 'B', 'GR', 'G', 'O', 'P']
        Allemogelijkheden = func.combinatielijst(kleuren, 4)

        for i in range(4):
            tijdelijk = PLcode.split(' ')
            code.append(tijdelijk[i])

        Overigemogelijkheden = []
        for i in range(len(Allemogelijkheden)):
            Overigemogelijkheden.append(Allemogelijkheden[i])


        for i in range(11):
            PCgok = Overigemogelijkheden[0]
            print(PCgok)
            feedback = input('Geef feedback (wit, zwart):')
            Feedback = (feedback.split(' '))
            Witzwart = []

            # verandert player input en pcfeedback naar de zelfde output [wit, zwart]
            for i in range(2):
                Witzwart.append(int(Feedback[i]))
            PCfeedback = list(func.pinchecker(list(PCgok), code)) #feedback van de pc die gebruik maakt van de pincheckerfunctie
            PLfeedback = Witzwart                                 #feedback van de speler












