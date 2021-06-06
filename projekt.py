#Projekt zaliczeniowy python
#Baza filmów

import json 
import re
opcja = 1
baza_filmow = []
info_filmy_json = "[{}]"

def wyswietlanie_wszystkich_filmow ():   # OPCJA 2
    print('~~BAZA FILMÓW~~')
    info_filmy = json.loads(info_filmy_json)
    for film in baza_filmow:
        film = json.loads(film)
        print(film['tytul'])

def usuwanie_filmow_z_systemu (usun_film): # OPCJA 4
    for i in range(0, len(baza_filmow)):
        film = json.loads(baza_filmow[i])

        if usun_film == film['tytul']:
            baza_filmow.pop(i)
            print(f"Usunięto film: {film['tytul']}")
            break


def wyswietl_szczegolowe_dane_o_filmie (tytul_filmu, rodzaj_opcji): # OPCJA 5
    if rodzaj_opcji == 'A' or rodzaj_opcji == 'a':

        for i in range(0, len(baza_filmow)):
            film = json.loads(baza_filmow[i])

            if tytul_filmu == film['tytul']:
                print(f"Film reżyserował: {film['rezyser']}")
                break

    elif rodzaj_opcji == 'B' or rodzaj_opcji == 'b':

        # info_gatunek = input('Podaj nazwę filmu: ')
        for i in range(0, len(baza_filmow)):
            film = json.loads(baza_filmow[i])

            if tytul_filmu == film['tytul']:
                print(f"Film należy do gatunku: {film['gatunek']}")
                break



    elif rodzaj_opcji == 'C' or rodzaj_opcji == 'c':
        #info_aktorzy = input('Podaj nazwę filmu: ')
        for i in range(0, len(baza_filmow)):
            film = json.loads(baza_filmow[i])

            if tytul_filmu == film['tytul']:
                print(f"W filmie grali: {film['aktorzy']}")
                break



    elif rodzaj_opcji == 'D' or rodzaj_opcji == 'd':
        #info_zwiastun = input('Podaj nazwę filmu: ')
        for i in range(0, len(baza_filmow)):
            film = json.loads(baza_filmow[i])

            if tytul_filmu == film['tytul']:
                print(f"Adres do zwiastunu: {film['adres_URL']}")
                break

def zapisywanie_filmow_do_pliku (): # OPCJA 6
    filmy_do_eksportu = ';'.join(baza_filmow)

    plik = open('wyeksportowane_filmy.txt', 'w')
    plik.write(filmy_do_eksportu)
    plik.close()

def odczytywanie_zapisanych_filmow (): # OPCJA 7
    plik = open('wyeksportowane_filmy.txt', 'r')
    dane = plik.readline()
    rozdzielone_filmy = dane.split(';')

    for rozdzielony_film in rozdzielone_filmy:
        baza_filmow.append(rozdzielony_film)

def dodawanie_ocen_do_filmow (film_do_oceny, ocena): # OPCJA 8

    for n in range(0, len(baza_filmow)):
        film = json.loads(baza_filmow[n])

        if film_do_oceny == film['tytul']:
            baza_filmow.pop(n)

            obecna_ocena = film['ocena_filmu']

            if obecna_ocena == 0.0:
                nowa_ocena = (ocena + obecna_ocena)
                film['ocena_filmu'] = nowa_ocena
            else:
                nowa_ocena = (ocena + obecna_ocena) / 2
                film['ocena_filmu'] = nowa_ocena

            oceny_filmow = json.dumps(film)
            baza_filmow.append(oceny_filmow)
            break

def wyswietlanie_rankingu_ocen(): # OPCJA 9
    oceny = {}
    for film in baza_filmow:
        film = json.loads(film)
        oceny[film['tytul']] = film['ocena_filmu']

    import operator
    oceny = dict(sorted(oceny.items(), key=operator.itemgetter(1), reverse=True))
    # items robi na liste
    # sorted przyjmuje tlyko liste
    # operator pozwala wyjąć element z listy

    licznik = 1
    for film in oceny:
        print(licznik, film, oceny[film])
        licznik += 1

def wyswietlanie_informacji_o_filmie(film_do_wys_info): # OPCJA 10
    for film in baza_filmow:
        film = json.loads(film)

        if film_do_wys_info == film['tytul']:
            print((f"INFORMACJE O FILIE: {film['tytul']}"), '\n' + (('Tytuł: ') + film['tytul']),
                  '\n' + (('Reżyser: ') + film['rezyser']), '\n' + (('Gatunek: ') + film['gatunek']),
                  '\n' + (('Aktorzy: ') + film['aktorzy']), '\n' + (('Link do zwiastunu: ') + film['adres_URL']))
            break

def edytowanie_filmow(rodzaj_opcji, film_do_edycji): # OPCJA 11
    if rodzaj_opcji == 'A' or rodzaj_opcji == 'a':
        nowy_rezyser = input('Podaj nowego reżysera: ')
        for i in range(0, len(baza_filmow)):
            film = json.loads(baza_filmow[i])
            if film_do_edycji == film['tytul']:
                baza_filmow.pop(i)  #removes item at the given index from the list

                film['rezyser'] = nowy_rezyser
                film_nowy_rezyser = json.dumps(film)
                baza_filmow.append(film_nowy_rezyser)
                break

    elif rodzaj_opcji == 'B' or rodzaj_opcji == 'b':
        nowy_gatunek = input('Podaj nowy gatunek: ')
        for i in range(0, len(baza_filmow)):
            film = json.loads(baza_filmow[i])
            if film_do_edycji == film['tytul']:
                baza_filmow.pop(i)

                film['gatunek'] = nowy_gatunek
                film_nowy_gatunek = json.dumps(film)
                baza_filmow.append(film_nowy_gatunek)
                break


    elif rodzaj_opcji == 'C' or rodzaj_opcji == 'c':
        nowi_aktorzy = input('Podaj nowych aktorów: ')
        for i in range(0, len(baza_filmow)):
            film = json.loads(baza_filmow[i])
            if film_do_edycji == film['tytul']:
                baza_filmow.pop(i)

                film['aktorzy'] = nowi_aktorzy
                film_nowi_aktorzy = json.dumps(film)
                baza_filmow.append(film_nowi_aktorzy)
                break

    elif rodzaj_opcji == 'D' or rodzaj_opcji == 'd':
        nowy_URL = input('Podaj nowy adres zwiastunu: ')
        for i in range(0, len(baza_filmow)):
            film = json.loads(baza_filmow[i])
            if film_do_edycji == film['tytul']:
                baza_filmow.pop(i)

                film['adres_URL'] = nowy_URL
                film_nowy_URL = json.dumps(film)
                baza_filmow.append(film_nowy_URL)
                break


while opcja != '0':
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('DOSTEPNE OPCJE:')
    print('1 - DODAJ FILM')
    print('2 - WYŚWIETL WSZYSTKIE FILMY')
    print('3 - EDYTUJ DANE O FILMIE')
    print('4 - USUŃ FILM Z SYSTEMU')
    print('5 - SZCZEGÓŁOWE DANE O FILMIE')
    print('6 - ZAPISZ DO PLIKU')
    print('7 - ODCZYTAJ ZAPISANE FILMY')
    print('8 - DODAJ OCENĘ')
    print('9 - WYŚWIETL RANKING FILMÓW')
    print('10 - WYŚWIETL INFORMACJE O FILMIE')
    print('11 - EDYCJA FILMU')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    opcja = input('Proszę wybrać opcję: ')


    if opcja == '1':
        tytul = input('Proszę podać nazwę filmu: ')
        rezyser = input('Proszę podać reżysera: ')
        gatunek = input('Proszę podać gatunek filmu: ')
        aktorzy = input('Proszę podaj aktorów: ')
        adres_URL = input('Proszę podaj adres URL zwiastunu: ')
        info_film = {'tytul':tytul, 'rezyser':rezyser, 'gatunek':gatunek, 'aktorzy':aktorzy, 'adres_URL':adres_URL, 'ocena_filmu':0.0}


        info_filmy_json = json.dumps(info_film)
        baza_filmow.append(info_filmy_json)


    elif opcja == '2':

        wyswietlanie_wszystkich_filmow()


    elif opcja == '4':
        usun_film = input('Podaj nazwę filmu do usunięcia: ')

        usuwanie_filmow_z_systemu(usun_film)



    elif opcja == '5':
        print('Wybierz opcje: ', '\n' 'A = reżyser', '\n' 'B = gatunek', '\n' 'C = aktorzy', '\n' 'D = adres URL zwiastunu')
        rodzaj_opcji = input('Twoja opcja: ')
        info_rezyser = input('Podaj nazwę filmu: ')


        wyswietl_szczegolowe_dane_o_filmie(info_rezyser, rodzaj_opcji)


    elif opcja == '6':

        zapisywanie_filmow_do_pliku()


    elif opcja == '7':

        odczytywanie_zapisanych_filmow()

    elif opcja == '8':

        film_do_oceny = input('Podaj nazwę filmu: ')
        ocena = float(input('Podaj ocenę: '))

        dodawanie_ocen_do_filmow(film_do_oceny, ocena)



    elif opcja == '9':
        print('~~RANKING FILMÓW~~')

        wyswietlanie_rankingu_ocen()




    elif opcja == '10':
        film_do_wys_info = input('Podaj nazwę filmu: ')

        wyswietlanie_informacji_o_filmie(film_do_wys_info)

#dopisz ocenę

    elif opcja == '11':
        print('Wybierz opcje: ', '\n' 'A = reżyser', '\n' 'B = gatunek', '\n' 'C = aktorzy',
              '\n' 'D = adres URL zwiastunu')
        rodzaj_opcji = input('Twoja opcja: ')
        film_do_edycji = input('Tytuł filmu: ')

        edytowanie_filmow(rodzaj_opcji, film_do_edycji)



    else:
        print('Nie ma takiej opcji! Uruchom program ponownie.')