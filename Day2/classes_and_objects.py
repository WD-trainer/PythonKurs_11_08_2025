##############################################################
# OBIEKTOWOŚĆ W PYTHONIE — MATERIAŁ SZKOLENIOWY
##############################################################

from timeit import default_timer as timer
import time

from abc import ABC, abstractmethod
from dataclasses import dataclass

import pandas as pd
from functools import total_ordering, cached_property   # fills in missing comparison methods (<, <=, >, >=) based on just two: either __eq__ and one other comparison method like __lt__ or __gt__.

from exceptiongroup import catch


class Osoba(object):

    def __init__(self, imie: str, nazwisko: str, wiek: int):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def wypiszMnie(self):
        print(self.imie, self.nazwisko, self.wiek)

    def __str__(self): # dla print i użytkownika
        return f'Cześć jestem: {self.imie}, {self.nazwisko}, {self.wiek}'

    def __repr__(self): # dla debuggera, programisty
        return f"Osoba({self.imie}, {self.nazwisko}, {self.wiek})"


o = Osoba("Wojtek", "Dudzik", 31)
o2 = Osoba("Jan", "Nowak", 25)

print(o.imie)
o.wiek += 1
print(o.wiek)
o.wypiszMnie()

o3 = Osoba(imie="Krzysztof", nazwisko="Nowak", wiek=32)

lista_osob = [o, o2, o3]

for osoba in lista_osob:
    osoba.wypiszMnie()

print(o3)
napis = str(o3)
print(napis)

print(repr(o3))

# ------------------------------------------------------------
# KLASY I INSTANCJE
# Klasa — szablon definiujący zachowanie i strukturę obiektów.
# Instancja — konkretny obiekt stworzony na podstawie klasy.
# ------------------------------------------------------------



#     Stwórz klasę "Samochod" posiadającą pola "marka", "model", "rejestracja".
#     Klasa ta powinna zawierać też metodę "wyswietl" wypisującą dane z obiektu na konsoli
#     Stwórz dwa obiekty tej klasy i korzystajac  z metody "wyświetl" wyswietl na konsoli ich zawartość.

# dopisz metody __str__ i __repr__ do klasy samochod
class Samochod:
    ile_kol = 4

    def __init__(self, marka: str, model:str, rejestracja: str, kierowca: Osoba = None):
        self.marka = marka
        self.model = model
        self.rejestracja = rejestracja
        if kierowca is None:
            kierowca = Osoba("Jan", "Nowak", 35)
        self.__kierowca = kierowca

    def wypiszMnie(self):
        print(self.marka, self.model, self.rejestracja, self.__kierowca)

    def __repr__(self):
        return f'Samochod("{self.marka}", "{self.model}", "{self.rejestracja}", {repr(self.__kierowca)})'

    def __str__(self):
        return f'Samochod: {self.marka}, {self.model}, {self.rejestracja}, {self.__kierowca}'

    def __napraw(self):
        self._funkcja_dla_mechanika()
        #self.kiedy_kolejna_naprawa = "2026" # ZŁA praktyka
        print("Naprawiono")

    def _funkcja_dla_mechanika(self):
        print("Wymieniam świece")


s = Samochod("Skoda", "Octawia", 'WS124')
s2 = Samochod("Toyota", "Yaris", 'WWL642')

s.wypiszMnie()
s2.wypiszMnie()

print(f'ile kol ma samochod {s.ile_kol}')

print(s2)
print(repr(s2))

s.silnik = "Moj super v8"

# lista = [1,2,3]
# print(lista)

s2.marka = "Lexus"
print(s2)

# s2.__napraw()
# s2._funkcja_dla_mechanika()

# Tak nie robimy
#print(s2._Samochod__kierowca)


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def _get_radius(self):
        print("Get radius")
        return self.__radius

    def _set_radius(self, value):
        print("Set radius")
        self.__radius = value

    radius = property(fget=_get_radius,
                      fset=_set_radius,
                      doc="Radius property of circle")



kolo = Circle(5)
print(f"Promien {kolo.radius}")

kolo.radius = 10


class Rectangle:
    def __init__(self, a:int, b:int):
        self._a = a
        self.b = b

    @property
    def dlugosc_a(self):
        print("Get a")
        return self._a

    @dlugosc_a.setter
    def dlugosc_a(self, value):
        print("Set a")
        self._a = value


r = Rectangle(4,2)
r.b = 8
try:
    r.dlugosc_a = 30
except Exception as e:
    print(e)
print(f'Rectangle {r.dlugosc_a}, {r.b}')
r.dlugosc_a = 10
print(f'Rectangle {r.dlugosc_a}, {r.b}')



# Stwórz klasę Zawodnik posiadającą pola wzrost i masa, imie. Pola te mają być uzupełniane przy tworzeniu obiektu.
# Wzrost jest atrybutem prywatnym (__wzrost)
# masa i imie są atrybutami chronionymi (_masa, _imie)
# stwórz właściwość Waga która będzie wykorzystywać atrybut _masa
# właściwość Waga może być zmieniana ale tyklo z wykorzystaniem dekoratora @property
# stworz właściwość BMI który będzie tylko do odczytu
# wzor na bmi = masa / (wzrost ** 2)   wzrost podany w metrach 1.84
# Powołaj do życia obiekt tej klasy i wyświetl na konsoli obliczone BMI.
# dodac metode __str__
class Zawodnik:
    def __init__(self, wzrost: float, masa: float, imie: str):
        self.__wzrost = wzrost
        self._masa_zawodnika = masa
        self._imie = imie

    @cached_property
    def BMI(self) -> float:
        return self._masa_zawodnika / (self.__wzrost ** 2)

    @property
    def waga(self) -> float:
        return self._masa_zawodnika

    @waga.setter
    def waga(self, value: float):
        self._masa_zawodnika = value

    def __str__(self):
        return f'Zawodnik: {self._imie}, o BMI={self.BMI:.3f}'

    @staticmethod
    def nie_uzywam_atrybutow(info: str):
        print(info)

    @classmethod
    def create_from_string(cls, text: str):
        dane = text.strip().split(';')
        if len(dane) == 3:
            wzrost_cm, waga_lbs, imie = dane
            z = cls(wzrost=int(wzrost_cm) / 100, masa=int(waga_lbs) * 0.454, imie=imie)
            return z


    # odczytali dane z pliku dane.txt
    # zbudowali sobie liste zawodnikow (jako obietky klasy) przy uzyciu  @classmethod
    def create_from_file(cls, path_to_file: str) -> list:


z = Zawodnik(1.8, 80, "Jan")

print(z)
z.waga = 75
print(z)

Zawodnik.nie_uzywam_atrybutow()


z3 = Zawodnik.create_from_string("176;150;Paweł")
print(z3)


class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y


MathUtils.add(2,2)









########## Atrybuty domyślne mutowalne ###################

# class Bag:
#     def __init__(self, items=[]):  # Uwaga! Domyślna mutowalna lista
#         self.items = items
#
#     def add_item(self, item):
#         self.items.append(item)

# Tworzymy dwie instancje klasy Bag
# bag1 = Bag()
# bag2 = Bag()
#
# bag1.add_item("jabłko")
# bag2.add_item("banan")
#
# print("Zawartość bag1:", bag1.items)  # ['jabłko', 'banan']  <-- nieoczekiwane!
# print("Zawartość bag2:", bag2.items)  # ['jabłko', 'banan']  <-- nieoczekiwane!

########## Atrybuty domyślne mutowalne ###################

# wersja poprawna
class Bag:
    def __init__(self, items: list=None):
        if items is None:
            items = []
        self.items = items

    def add_item(self, item):
        self.items.append(item)

bag1 = Bag()
bag2 = Bag()

bag1.add_item("jabłko")
bag2.add_item("banan")

print("Zawartość bag1:", bag1.items)
print("Zawartość bag2:", bag2.items)
