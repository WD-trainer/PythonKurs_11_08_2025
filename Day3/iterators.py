from collections.abc import Iterator

from Day2.classes_and_objects import Zawodnik

print("*" * 50)
print("*" * 50)
print("*" * 50)
print("*" * 50)
print("*" * 50)


"""
ITERATORY w Pythonie

🔹 Czym jest iterator?
    Iterator to obiekt, który:
        1. Przechowuje stan iteracji (wie, gdzie jest).
        2. Implementuje metody:
            - __iter__() → zwraca iterator (najczęściej self)
            - __next__() → zwraca kolejny element lub zgłasza StopIteration
    Dzięki temu obiekt może być użyty w pętli for, w list comprehensions, itp.

🔹 W Pythonie wiele wbudowanych obiektów to iteratory lub iterowalne (np. listy, słowniki, pliki).

🔹 Kluczowe różnice:
    - Iterable → obiekt, po którym można iterować (ma __iter__())
    - Iterator → obiekt, który sam wie, jak pobrać kolejny element (ma __iter__() i __next__()).
"""

class CountDown:
    """Iterator odliczający od zadanej liczby do zera"""
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # iterator zwraca sam siebie

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

print("=== CountDown od 5 ===")
for number in CountDown(5):
    print(number)



class IncrementIterator(Iterator):
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __next__(self):
        if self.n == self.i:
            raise StopIteration
        self.i += 1
        return self.i


for e in IncrementIterator(10):
    print(e)

print("*" * 50)


nasz_iterator = IncrementIterator(5)

next(nasz_iterator)
next(nasz_iterator)
next(nasz_iterator)
print(next(nasz_iterator))


########################## Kiedy __iter__ nie zwraca self
# iterator własny vs obiekt iterowalny
class MyList:
    """Obiekt iterowalny, ale nie iterator"""
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        # Zwracamy nowy iterator, żeby można było zacząć od początku
        return MyListIterator(self.data)


class MyListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        val = self.data[self.index]
        self.index += 1
        return val


# print("\n=== Iterowalny obiekt MyList ===")
# my_list = MyList(["A", "B", "C"])
# for item in my_list:
#     print(item)

# for item in my_list:
#     print(item)

# Jak to działa z iteratorem
# nasz_iterator = IncrementIterator(5)
# for e in nasz_iterator:
#     print(e)
# for e in nasz_iterator:
#     print(e)

# class TreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
#
#
# tree = TreeNode(1,
#                 TreeNode(2,
#                                 TreeNode(4),
#                                 TreeNode(5)),
#
#                 TreeNode(3,
#                             None,
#                                 TreeNode(6)))
#
#
# class TreeIterator:
#     def __init__(self, root):
#         self.stack = [root] if root else []
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if not self.stack:
#             raise StopIteration
#
#         node = self.stack.pop()
#
#         if node.right:
#             self.stack.append(node.right)
#         if node.left:
#             self.stack.append(node.left)
#
#         return node.value
#
#
# iterator = TreeIterator(tree)
#
# for value in iterator:
#     print(value)


# import torch
# from torch.utils.data import DataLoader, Dataset
#
#
# # Definiujemy niestandardowy dataset
# class MyDataset(Dataset):
#     def __init__(self):
#         self.data = torch.arange(10)  # Tworzymy proste dane od 0 do 9
#
#     def __len__(self):
#         return len(self.data)
#
#     def __getitem__(self, idx):
#         return self.data[idx]
#
# # Tworzymy dataset
# dataset = MyDataset()
#
# # Używamy DataLoader, który tworzy iterator
# dataloader = DataLoader(dataset, batch_size=2, shuffle=True)
#
# # Iterujemy po DataLoader (wykorzystując iterator wbudowany w DataLoader)
# for batch in dataloader:
#     print(batch)



# uzupełnic klase lista zwodnikow o metody __iter__ oraz __next__
class ListaZawodnikow:
    def __init__(self, path: str):
        self.zawodnicy = []
        with open(path, "r") as plik:
            for linia in plik:
                dane = linia.strip().split(";")
                if len(dane) == 3:
                    imie, waga, wzrost = dane
                    self.zawodnicy.append(Zawodnik(masa=float(waga), wzrost=float(wzrost), imie=imie))
        self.index = 0




# nasza_lista = ListaZawodnikow("dane.txt")
# for z in nasza_lista:
#     print(z)



#  Utwórz klasę ReverseString, która działa jak iterator odwracający kolejność znaków w napisie.
#  Przykład:
#        for ch in ReverseString("Python"):
#            print(ch)
#    Wynik:
#        n
#        o
#        h
#        t
#        y
#        P

