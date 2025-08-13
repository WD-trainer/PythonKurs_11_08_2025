import random
import time
import sys

"""
GENERATORY w Pythonie

🔹 Czym jest generator?
    - Generator to specjalna funkcja lub obiekt, który zwraca kolejne wartości na żądanie.
    - Zamiast zwracać wszystkie dane naraz (jak lista), generator "produkuje" wartości w momencie ich pobrania.
    - Używa słowa kluczowego `yield` zamiast `return`.

🔹 Różnica yield vs return:
    - return → kończy funkcję i zwraca jedną wartość.
    - yield → zwraca wartość, ale funkcja zapamiętuje swój stan i może być wznowiona.

🔹 Dlaczego warto używać generatorów?
    - Oszczędność pamięci (nie przechowują wszystkich elementów naraz).
    - Możliwość tworzenia nieskończonych sekwencji.
    - Czysty, czytelny kod.

🔹 Rodzaje generatorów:
    1. Generatory skończone → mają określony koniec.
    2. Generatory nieskończone → mogą działać w nieskończoność (np. strumienie danych).

"""

def elements():
    yield 'element 1'
    yield 'element 2'
    yield 'element 3'
    print("hello world")
    yield 'element 4'




if __name__ == '__main__':
    generator = elements()

    print(generator.__next__())
    print(generator.__next__())
    print(generator.__next__())

    for e in elements():
        print(e)

    for i in range(10000000000000000000):
        print(i)
        if i > 10:
            break

    # start = time.time()
    # range_list = [i for i in range(100000000)]
    # end = time.time()
    # print(f'Time needed: {end - start}')
    #
    # for i in range_list:
    #     print(i)
    #     if i > 10:
    #         break

    # -------------------------
    # generatory skończone
    # -------------------------
    def reverse_string(text):
        """Zwraca znaki w odwrotnej kolejności"""
        for ch in reversed(text):
            yield ch

    # print("\n=== reverse_string ===")
    # for ch in reverse_string("Python"):
    #     print(ch)


    # -------------------------
    # generatory nieskończone
    # -------------------------
    def infinite_counter(start=0):
        """Generator nieskończony – liczy w górę"""
        while True:
            yield start
            start += 1


    # print("\n=== infinite_counter (pierwsze 5 liczb) ===")
    # counter = infinite_counter(10)
    # for _ in range(5):
    #     print(next(counter))  # ręczne pobieranie


    # -------------------------
    # generatory nieskończone - przyklad 2
    # -------------------------
    def tens():
        i = 1
        while True:
            yield i * 10
            i += 1


    # print("\n=== Liczymy po 10 ===")
    #
    # generator_tens = tens()
    # print(generator_tens.__next__())
    # print(generator_tens.__next__())
    #
    # print("And now in for loop")
    #
    # for ten in generator_tens:
    #     print(ten)
    #     if ten > 100:
    #         break


    # Generatory mogą symulować strumienie danych, np. sensory zbierające dane.
    def data_stream():
        while True:
            yield random.randint(1, 100)
            time.sleep(0.1)


    # stream = data_stream()
    # for _ in range(5):
    #     print(next(stream))  # Symuluje odbiór danych co sekundę


    # -------------------------
    # generator a oszczędność pamięci
    # -------------------------
    def big_range(n):
        """Generator dużego zakresu (bez zajmowania dużej ilości RAMu)"""
        for i in range(n):
            yield i


    # big_list = list(range(1_000_000))  # zużywa dużo pamięci
    # big_gen = big_range(1_000_000)  # praktycznie zerowe zużycie pamięci
    #
    # print("\nRozmiar listy:", sys.getsizeof(big_list), "B")
    # print("Rozmiar generatora:", sys.getsizeof(big_gen), "B")

    # -------------------------
    # generator a czas wykonania (lazy evaluation)
    # -------------------------
    # potegi2 = [2 ** i for i in range(100)]
    #
    # generator_potegi = (2 ** i for i in range(1000000000000))
    #
    # print(generator_potegi)
    # print(next(generator_potegi))
    # print(next(generator_potegi))
    # print(next(generator_potegi))

    #  Stworz generator ktory bedzie przyjmowal przez parametr ilosc elementow a nastepnie zwracal elementy o tresci
    #  f'element o indeksie {x}'( gdzie x bedzie numerem podawanego elementu) czekajac 0.1 sekunde przed zwrotem kazdego elementu (time.sleep(0.1)).









    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # napisz generator ktory bedzie zwracał nieskonczenie wiele liczb pierwszych

    # generator_of_primes = prime_numbers()
    #
    # for i in range(20):
    #     print(next(generator_of_primes))


    # -------------------------
    # Przykłady praktyczne
    # -------------------------
    # def read_lines_in_batches(file_path: str, batch_size: int = 3) -> list[str]:
    #     with open(file_path) as file:
    #         while True:
    #             batch = []
    #             for _ in range(batch_size):
    #                 line = file.readline()
    #                 if not line:
    #                     break
    #                 batch.append(line.strip())
    #             if not batch:
    #                 break
    #             yield batch
    #
    #
    # file = r'../Day1/text.txt'
    # for i, batch in enumerate(read_lines_in_batches(file, batch_size=10)):
    #     print(f'Batch number {i}: {batch}')
    #
    #
    # def generate_combinations(elements, length):
    #     return itertools.combinations(elements, length)
    #
    #
    # # Generowanie kombinacji
    # for combination in generate_combinations([1, 2, 3, 4], 2):
    #     print(combination)