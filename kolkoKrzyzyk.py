def narysuj_plansze(stan_gry):
    print('{}|{}|{}\n-----\n{}|{}|{}\n-----\n{}|{}|{}\n'.format(*stan_gry))

    
def zapytaj_gracza_o_liczbe(gracz, plansza):
    dobra_liczba = False
    while not dobra_liczba:
        narysuj_plansze = plansza
        liczba_gracz = input('Gracz {} gdzie wstawić {}: '.format(*gracz))
        liczby = range(0, 9, 1)
        try:
            liczba_gracz = int(liczba_gracz)
            if liczba_gracz in liczby:
                if plansza[liczba_gracz] == 'X' or plansza[liczba_gracz] == 'Y':
                    print('To pole jest zajęty, wybierz inne')
                else:
                    dobra_liczba = True
            else:
                print('Podaj liczbę z przedziału 0-8')
        except ValueError:
            print('To nie jest liczba')
    return int(liczba_gracz)


def aktualizuj_gre(stan_gry, gracz, pozycja):
    stan_gry[pozycja] = gracz[1]
    return stan_gry

def zmien_gracza(gracz):
    if gracz == (1,'X'):
        gracz = (2,'O')
    else:
        gracz = (1,'X')
    return gracz


def sprawdz_czy_wygrana(stan_gry):
    wygrana = [(0,1,2), (3,4,5), (6,7,8), (0,3,6),
               (1,4,7), (2,5,8), (6,4,2), (0,4,8)]
    for item in wygrana:
        if stan_gry[item[0]] == stan_gry[item[1]] == stan_gry[item[2]] == 'X':
            print('Gracz 1 wygrał!!!')
            narysuj_plansze(stan_gry)
            return True
        elif stan_gry[item[0]] == stan_gry[item[1]] == stan_gry[item[2]] == 'O':
            print('Gracz 2 wygrał!!!')
            narysuj_plansze(stan_gry)
            return True
    

def graj():
    stan_gry = [x for x in range(9)]
    obecny_gracz = (1,'X')
    koniec = False
    i = 0
    while not koniec:
        narysuj_plansze(stan_gry)
        print('Ruch nr: ', i+1)
        liczba = zapytaj_gracza_o_liczbe(obecny_gracz, stan_gry)
        aktualizuj_gre(stan_gry, obecny_gracz, liczba)
        print('\n')
        obecny_gracz = zmien_gracza(obecny_gracz)
        koniec = sprawdz_czy_wygrana(stan_gry)
        i += 1
        if i >= 9:
            print('Remis!!!')
            koniec = True

if __name__ == '__main__':
    graj()
