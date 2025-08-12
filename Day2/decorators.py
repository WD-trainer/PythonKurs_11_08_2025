import operator
import random
import os
import re
from collections import defaultdict

from datetime import datetime
import time
import functools
from typing import Callable
import statistics


def do_opakowania():
    print("Opakuj mnie")


def dekorator(funkcje: Callable) -> Callable:
    def opakowujaca():
        print("Przed")
        funkcje()
        print("Po")

    return opakowujaca

@dekorator
def do_opakwoanie_2():
    print("Skladnia dekorator pythona")

if __name__ == '__main__':
    # https://refactoring.guru/pl/design-patterns/decorator

    udekorwana = dekorator(do_opakowania)
    udekorwana()

    do_opakwoanie_2()

    # Stwórz funkcję której zadaniem będzie poczekanie 3 sekundy i wypisanie na konsoli komunikatu.
    # Dodaj dekorator który zliczy czas wykonywania tej funkcji. Pobranie aktualnego czasu to: "time.time()" lub  datetime.now()
    def licz_czas(fun):
        def wew():
            poczatek = datetime.now()
            fun()
            koniec = datetime.now()
            print(f'Wywolanie trwalo {koniec - poczatek}')

        return wew

    @licz_czas
    def opakuj_mnie():
        #time.sleep(3)
        print("Robie ciekawe rzeczy w Pythonie")

    opakuj_mnie()

    # opakuj_mnie = dekorator(opakuj_mnie)
    # opakuj_mnie()
    # help(opakuj_mnie)

    @licz_czas
    def opakowanie_inne():
        print("inna funkcja")


    def dekorator_z_1_parametrem(fun):
        def wew(liczba: int):
            print("Hurra działa z parametrem")
            print(fun(liczba))

        return wew


    @dekorator_z_1_parametrem
    def dodaj_cztery(liczba: int) -> int:
        return liczba + 4

    dodaj_cztery(4)


    def dekorator_do_funkcji_z_parameterami(fun):
        def wew(*args, **kwargs):
            print("Hurra działa zawsze")
            fun(*args, **kwargs)
            print("Po wszystkim")

        return wew


    @dekorator_do_funkcji_z_parameterami
    def dekorowana(x: str):
        print(f'siema {x}')

    @dekorator_do_funkcji_z_parameterami
    def dekorowana_bez_p():
        print(f'siema')

    dekorowana("Janek")
    dekorowana(x="Wojtek")
    dekorowana_bez_p()


    @dekorator_do_funkcji_z_parameterami
    def moja_suma(*liczby: tuple[int, ...]) -> int:
        suma = 0
        for i in liczby:
            suma += i
        print(f'Wynik to  {suma}')
        return suma

    moja_suma(1,2,3,3,4,5)


    # Napisz funkcje która przed i po wykonaniu innej funkcji wypisze 25 '*'     print("*" * 25)
    def star(func):
        def inner(*args, **kwargs):
            print("*" * 25)
            func(*args, **kwargs)
            print("*" * 25)

        return inner


    def percent(func):
        def inner(*args, **kwargs):
            print("%" * 15)
            func(*args, **kwargs)
            print("%" * 15)

        return inner


    @percent
    @star
    def printer(msg: str):    # printer = percent(star(printer))
        print(msg)

    @star
    def printer_2(msg: str, count: int):
        print(msg * count)

    printer_2("Hello World", 2)

    printer("Hello world")


    def hello_decorator(func):
        def inner1(*args, **kwargs):
            print("before Execution")

            # getting the returned value
            returned_value = func(*args, **kwargs)
            print("after Execution")

            # returning the value to the original frame
            return returned_value

        return inner1

    @hello_decorator
    def sum_two_numbers(a: int, b: int) -> int:          # sum_two_numbers = hello_decorator(sum_two_numbers)
        print("Inside the function sum_two_numbers")
        return a + b

    result = sum_two_numbers(12, 4)
    print(f"Wynik dodawania: 12 + 4 = {result}")


    # Dodaj dekorator który zliczy czas wykonywania funkcji z parametrami.
    # Zaloguj na konsole wszystkie przekazane parametry (czyli args i kwargs)
    # wypisz wynik opakowanej funkcji
    def licz_czas_i_loguj(fun):
        def wewnetrzna(*args, **kwargs):
            print(f'Argumenty {args}')
            print(f'Key-word arguments {kwargs}')
            poczatek = datetime.now()
            value = fun(*args, **kwargs)
            koniec = datetime.now()
            print(f'wywolanie trwalo {koniec - poczatek}')
            print(f'Wynik dzialania funkcji {value}')
            return value

        return wewnetrzna


    @licz_czas_i_loguj
    def opakuj_mnie_z_parametrami(x, napis_do_wypisania):
        for i in range(x):
            time.sleep(1)
        print(f"Robie ciekawe rzeczy w Pythonie {napis_do_wypisania}")
        return 10


    returned_value = opakuj_mnie_z_parametrami(x=1, napis_do_wypisania="jestem cool")
    print(returned_value)