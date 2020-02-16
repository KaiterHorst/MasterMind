import random
''' interface gedeelte'''
print('Kies een optie.')
print(  'Optie 1: De computer kiest een patroon en jij gokt'
        '\nOptie 2: Kies zelf een patroon en de computer gokt, implementatie 1'
        '\nOptie 3: Kies zelf een patroon en de computer gokt, implementatie 2'
        '\nOptie 4: Kies zelf een patroon en de computer gokt, eige implementatie')

optie = input(('Maak een keuze:'))

''' Optie 1'''
if optie == '1':
    print('\n''De kleuren waaruit je kan kiezen zijn: Rood, Blauw, Groen, Geel, Oranje en Paars\n')
    kleuren = ['Rood', 'Blauw', 'Groen', 'Geel', 'Oranje', 'Paars']
    PCcode = []

    for i in range(4):
      PCcode.append(random.choice(kleuren))

    print(PCcode)
    for i in range(1,11):
        Gokken = []
        Gok1 = input('Eerste kleur?')
        Gokken.append(Gok1)
        while Gok1 not in kleuren:
            print('Dit is geen geldige keuze, probeer opnieuw.')
            Gok1 = input('Eerste kleur?')

        Gok2 = input('Tweede kleur?')
        Gokken.append(Gok2)
        while Gok2 not in kleuren:
            print('Dit is geen geldige keuze, probeer opnieuw.')
            Gok2 = input('Tweede kleur?')

        Gok3 = input('Derde kleur?')
        Gokken.append(Gok3)
        while Gok3 not in kleuren:
            print('Dit is geen geldige keuze, probeer opnieuw.')
            Gok3 = input('Derde kleur?')

        Gok4 = input('Vierde kleur?')
        Gokken.append(Gok4)
        while Gok4 not in kleuren:
            print('Dit is geen geldige keuze, probeer opnieuw.')
            Gok4 = input('Vierde kleur?')

        Zwart = 0  # Goede kleur, Goede plek
        Wit = 0  # Goede kleur, foute plek
        print(Gokken)

        for i in range(4):
            if Gokken[i] == PCcode[i]:
                Zwart += 1
            if Gokken[i] in PCcode and Gokken[i] != PCcode[i]:
                Wit += 1

        print('Je hebt', Zwart,'aantal pinnen op de juiste positie.'
            '\nJe hebt', Wit, ' kleuren goed maar op de foute positie')

        if Zwart == 4:
            print('Je hebt binnen 10 zetten gewonnen!')
            break
    if Zwart != 4:
        print('Helaas, je beurten zijn op.\n Nog een keertje proberen?')


'''Optie 2'''
if optie == '2':
    print(2)