'''

trochę przypominajek do stringow

'''

jakis_tekst = "siala Baba mak"


# w printach zeby widac bylo efekt
print(jakis_tekst.endswith("mak"))  # zwraca true lub false w zaleznosci czy string konczy sie na podana wartosc
print(jakis_tekst.capitalize())  # robi wielka pierwsza litere litere
print(jakis_tekst.casefold())  # robi wszystkie litery male
print(jakis_tekst.center(100,"."))  # centruje napis wedle danego argumentu - liczba int daje calkowita szerokosc,
                                    # znak - wypelnia miejsce zamiast spacji
print(jakis_tekst.count('a'))  # liczy ile takich znakow jest w stringu
print(jakis_tekst.upper())  # zmienia znaki w stringu na duze litery
print(jakis_tekst.lower())  # jw tylko na male
print(jakis_tekst.islower())  # sprawdza czy string jest stworzony z malych liter, isupper odpowiednio czy z duzych
print(jakis_tekst.find("ba", 6))  # zwraca na kotrym miejscu jest w stringu podany string w argumencie
                                  # oraz od ktorego zaczynamy (mozna tez podac na ktorym konczymy szukanie)
print(jakis_tekst.replace('ba', 'ka'))  # zamienia string(znak na nowy string (znak)
print(jakis_tekst.split("a"))  # zwraca liste, a jako parametr podajemy separator ktory oddziela elementy listy
print("".join(reversed(jakis_tekst)))  # a to odwraca tekst
print(jakis_tekst[::-1])  # to również, ale nie przez funkcje tylko przez cięcie