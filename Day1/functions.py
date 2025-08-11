import operator
import random
import os
import re
from collections import defaultdict

from datetime import datetime
import time
import functools
from operator import truediv
from typing import Callable, Tuple, List, Union


def times2(a: int | list[int]) -> str | int:  # Union[str, int]
    if a == 0:
        return "przez zero nie mnoze"
    return a * 2


if __name__ == '__main__':
    print(times2(2))

    print(times2("string"))

    print(type(times2([1, 2, 3, 4])))
    print(times2([1, 2, 3, 4]))


    def funckja_jako_argument(f: Callable, x: int):
        print(f(x))

    funckja_jako_argument(times2, 32)
    funckja_jako_argument(lambda arg: arg + 2, 3)


    def powieksz(x: str) -> str:
        return x.upper()


    def tytul(napis: str) -> str:
        return napis.title()


    def zastosuj_dla_wszystkich(funkcja: Callable, *strings):  # *args
        print(strings)
        print(type(strings))
        for a in strings:
            print(funkcja(a))


    zastosuj_dla_wszystkich(powieksz, 'siała', 'baba', 'mak', 'aaaaa')
    zastosuj_dla_wszystkich(tytul, 'siała', 'baba', 'mak', )

    # Stwórz funkcję która wydrukuje na konsoli sumę wartości przekazanych do niej jako *args
    def moja_suma(*liczby: tuple[int, ...]) -> int:
        suma = 0
        for i in liczby:
            suma += i
        return suma

    # def moja_suma(*liczby: tuple[int, ...]) -> int:
    #    return sum(liczby)

    suma = moja_suma(1, 2, 3, 4, 5, 15, 18, 50)
    suma2 = moja_suma(1, 2, 3, 4, 5, 15, 18, 50, 10, 4, 3, 4, 5, 6, 7, 8, 9)
    print(suma)


    #################################

    list1 = [1, 2, 3]
    list2 = [4, 5]
    list3 = [6, 7, 8, 9]

    print(moja_suma(*list1, *list2, *list3))  # *list1 = 1,2,3

    def my_sum(a, b, c):
        print(f"a={a}")
        print(a + b + c)


    my_sum(*list1)  # my_sum(1,2,3)

    slownik = {"c": 2, "a": 4, "b": 3}
    my_sum(**slownik)  # my_sum(a=4,b=3,c=2) -- działa bo argumenty się nazywają tak jak klucze w słowniku


    def pomnoz_razy_dwa(x):
        return x * 2

    def podziel_przez_trzy(x):
        return x / 3

    def dodaj_piec(x):
        return x + 5


    funkcje = [pomnoz_razy_dwa, podziel_przez_trzy, dodaj_piec]

    def aplikuj(wartosc: int, *funckje) -> float:
        for f in funckje:
            wartosc = f(wartosc)
        return wartosc


    print(aplikuj(1, *funkcje))
    print(aplikuj(1, pomnoz_razy_dwa, podziel_przez_trzy, dodaj_piec, times2))


    def wiele_argumentów(*args):
        ile_ich = len(args)
        print(ile_ich)
        for element in args:
            print(element, type(element))
            if isinstance(element, str):
                print(f"znalazłem str na *args i to jest {element}")


    wiele_argumentów([1], "abc", 1.0, 123, "Moj super kurs pythona")


    # Napisz funkcję process_data, która:
    #
    # Przyjmuje dowolną liczbę argumentów pozycyjnych (*args), które mogą być liczbami, stringami lub listami.
    # Jeśli argument jest liczbą, dodaje ją do wyniku.
    # Jeśli argument jest stringiem, konkatenuje go do napisu (łączy wszytkie napisy w jeden).
    # Jeśli argument jest listą, sumuje wszystkie jej elementy. Powinno sumować wiele list razem
    def process_data(*args):
        total_sum = 0
        concatenated_string = ""
        list_sum = 0

        for item in args:
            if isinstance(item, int) or isinstance(item, float):
                total_sum += item
            elif isinstance(item, str):
                concatenated_string += item
            elif isinstance(item, list):
                list_sum += sum(item)

        return total_sum, concatenated_string, list_sum


    # Test
    result = process_data(1, "Hello", [1, 2], 3, "World", [3, 4])
    print(result)  # Wyjście: (4, "HelloWorld", 10)


    #######################################################

    def parametr_kwargs(**kwargs):
        for k in kwargs:
            print(k, kwargs[k])

    parametr_kwargs(dodatkowy=48, nastepny=111)


    def funkcja_przykladowa(arg1, *args, **kwargs):
        print("arg1:", arg1)
        print("args:", args)
        print("kwargs:", kwargs)


    funkcja_przykladowa(1, 2, 3, 4, imie='Anna', wiek=30)


    def zapisz_parametry_do_pliku(nazwa_pliku, **parametry):
        plik = open(nazwa_pliku, mode='w', encoding='utf-8')
        for p in parametry:
            plik.write(f'{p};{parametry[p]}\n')
        plik.close()

    zapisz_parametry_do_pliku('mojplik.csv', parametr1='wartość 1', parametr2=2,
                              moj_argument="Jestesmy zmeczeni bardzo")


    studenci = {
        "1001": {'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 21, 'oceny': [4, 3, 5, 4]},
        "1002": {'imie': 'Anna', 'nazwisko': 'Nowak', 'wiek': 22, 'oceny': [5, 5, 4, 5]},
        "1003": {'imie': 'Marek', 'nazwisko': 'Zielinski', 'wiek': 23, 'oceny': [3, 4, 2, 3]},
        "1004": {'imie': 'Zofia', 'nazwisko': 'Wiśniewska', 'wiek': 20, 'oceny': [4, 4, 4, 4]},
        "1005": {'imie': 'Krzysztof', 'nazwisko': 'Wojcik', 'wiek': 24, 'oceny': [2, 3, 2, 3]}
    }

    zapisz_parametry_do_pliku('mojplik.csv', parametr1='wartość 1', parametr2=2,
                              moj_argument="Jestesmy zmeczeni bardzo", **studenci)

    parametry = {"param1": 1, "param2": 2, "param3": 3}

    zapisz_parametry_do_pliku('mojplik2.csv', **parametry)

    # Stworz funkcje "config" ktora bedzie otrzymywala argumenty kwargs bedace ustawieniami.
    # Funkcja ta ma zapisac podane argumenty do pliku config.csv w 2 kolumnach z czego pierwsza jest nazwa
    # argumentu a druga jego wartoscia. Jesli dany argument juz istnieje w pliku to trzeba bedzie tylko zaktualizowac
    # jego wartosc, jesli jeszcze go nie ma to trzeba go bedzie dodac do pliku.

    def config(filename, **params):
        loaded_config = {}
        with open(filename, mode="r", encoding='utf-8') as file:
            for line in file:
                if line.isspace():
                    continue
                key, value = line.split(';')
                loaded_config[key] = value

        # TODO: aktualizacja wartosci loaded_config
        for key_params in params:
            loaded_config[key_params] = params[key_params]

        # TODO: zapis loaded_config do pliku (tego samego)
        with open(filename, mode="w", encoding='utf-8') as file:
            for key in loaded_config:
                file.write(f'{key};{loaded_config[key]}\n')


    config("plik.csv", wersja=1, arg=2, argument321=3, parametr1="wartość 2")
    config("plik.csv", arg_inny=2, argument321=10, wersja=2.0)

    ##############################################

    def zewnetrzna(x):
        def wewnetrzna(x):
            return x * 2

        print(wewnetrzna(x))
        return 1

    print(zewnetrzna(x=5))


    # funkcja zwracajaca funkcje
    def outer(x):
        def inner(y):
            return x + y

        return inner

    dodaj_dwa = outer(2)
    wynik = dodaj_dwa(7)
    print(wynik)

    def create_formatter(prefix="", suffix=""):
        return lambda text: f"{prefix}{text}{suffix}"

    important = create_formatter("!!! ", " !!!")
    print(important("Błąd krytyczny"))  # !!! Błąd krytyczny !!!


    def retry(delay, retries, func):
        def wrapper(*args, **kwargs):
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    time.sleep(delay)
                    print(f"Retrying after {delay} seconds...")
            raise Exception("Max retries reached")

        return wrapper


    # Funkcja, która czasem się "wysypie"
    def unstable_function():
        if random.random() < 0.7:  # 70% szans na błąd
            raise ValueError("Losowy błąd!")
        return "Sukces!"

    # Tworzymy wersję z automatycznymi ponownymi próbami
    safe_function = retry(delay=1, retries=5, func=unstable_function)

    try:
        result = safe_function()
        print(result)
    except Exception as e:
        print("Nie udało się wykonać funkcji:", e)


    ############################################## ##############################################

    # Do analizy własnej jak to zadziała
    def create_filter(criteria):

        def filter_function(data):
            return [
                item for item in data
                if all(item.get(key) == value for key, value in criteria.items())
            ]

        return filter_function


    # Przykład użycia:
    data = [
        {"name": "Alice", "age": 25, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"},
        {"name": "Alice", "age": 30, "city": "Chicago"}
    ]

    # Tworzymy filtr dla osób z Chicago w wieku 30 lat
    chicago_30_filter = create_filter({"city": "Chicago", "age": 30})

    # Używamy wygenerowanej funkcji do filtrowania danych
    filtered_data = chicago_30_filter(data)
    print(filtered_data)

    ############################################## ##############################################


    # Napisz funkcje która będzie tworzyła listę liczb parzystych lub nieparzystych w danym zakresie
    # funkcje do sprawdzenia parzystosci napisz jako funckje wewnętrzne i w zależności
    # od przekazanego parametru wywołuj odpowiednią
    # range(start, koniec)









    ############################################## ##############################################


    # rekurencja

    # fn(0,1) = 1
    # fn(2) = fn(1) + fn(0)
    # fn(3) = fn(2) + fn(1)

    @functools.lru_cache()
    def fibonacci(num):
        print(f"Calculating fibonacci({num})")
        if num < 2:
            return num
        return fibonacci(num - 1) + fibonacci(num - 2)


    poczatek = datetime.now()
    fibonacci(20)
    koniec = datetime.now()
    print(f'Fibonnaci time: {koniec - poczatek}')


    # def list_files(path):
    #     for entry in os.listdir(path):
    #         full_path = os.path.join(path, entry)
    #         if os.path.isdir(full_path):
    #             list_files(full_path)  # rekurencja w podfolder
    #         else:
    #             print(full_path)
    #
    #
    # list_files("E:\PythonKurs_11_08_2025")

    @functools.lru_cache()
    def dluga_funkcja():
        time.sleep(5)
        print("liczy sie")
        return 1

    poczatek = datetime.now()
    for i in range(100):
        dluga_funkcja()
    koniec = datetime.now()
    print(f'Ile czasu nam to zajęło: {koniec - poczatek}')

