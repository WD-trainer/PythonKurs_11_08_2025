##############################################
# ZADANIE 1
# Napisz dekorator `log_call`, który będzie wypisywał w konsoli:
# - nazwę funkcji
# - przekazane argumenty
# - wynik działania funkcji
# Użyj go do udekorowania funkcji `add(a, b)`.
##############################################





def add(a, b):
    return a + b

add(3, 5)

##############################################
# ZADANIE 2
# Utwórz dekorator `require_login`, który będzie sprawdzał,
# czy zmienna globalna `LOGGED_IN` jest ustawiona na True.
# Jeśli tak — wywołaj funkcję, jeśli nie — wypisz komunikat "Dostęp zabroniony".
# Użyj go do zabezpieczenia funkcji `get_secret_data()`.
##############################################

LOGGED_IN = False  # Zmień na True, aby zobaczyć działanie

def require_login(func):
    #TODO: uzupełnij
    pass


@require_login
def get_secret_data():
    return "To jest tajna wiadomość!"

print(get_secret_data())




##############################################
# ZADANIE 3
# Stwórz dekorator `retry` przyjmujący argumenty `retries` i `delay`,
# który ponowi wywołanie funkcji w przypadku wystąpienia wyjątku,
# czekając `delay` sekund między próbami.
# Użyj go do funkcji `unstable_function()` symulującej losowe błędy.
##############################################

import random








def unstable_function():
    if random.random() < 0.7:
        raise ValueError("Losowy błąd!")
    return "Sukces!"

print(unstable_function())


##############################################
# ZADANIE 4
# Stwórz dekorator `cache_results`, który będzie zapisywał wyniki funkcji
# w słowniku cache (klucz = argumenty, wartość = wynik).
# Przy kolejnym wywołaniu z tymi samymi argumentami funkcja powinna zwrócić
# wynik z cache zamiast liczyć ponownie.
# Użyj go do udekorowania funkcji `slow_square(n)`, która symuluje wolne obliczenia.
##############################################

import time





def slow_square(n):
    time.sleep(1)  # Symulacja wolnych obliczeń
    return n * n


print(slow_square(5))  # oblicza
print(slow_square(5))  # z cache