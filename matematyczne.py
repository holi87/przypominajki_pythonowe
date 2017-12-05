'''

obliczanie pól kilku figur geometrycznych

'''
# obliczanie pola koła
def pole_kola(promien_okregu):
    pi = 3.14
    return pi * promien_okregu ** 2


# obliczanie pola kwadratu
def pole_kwadratu(bok):
    return pole_prostokata(bok, bok)


# obliczanie pola prostokąta
def pole_prostokata(krotszy, dluzszy):
    return krotszy * dluzszy


# obliczanie pola trapezu
def pole_trapezu(podstawa_gora, podstawa_dol, wysokosc):
    return ((podstawa_dol + podstawa_gora) / 2) * wysokosc


# wydruki
print(pole_kola(5))
print(pole_kwadratu(5))
print(pole_prostokata(5, 4))
print(pole_trapezu(4, 3, 3))