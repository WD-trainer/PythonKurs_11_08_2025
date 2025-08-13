# pip install fire
# https://google.github.io/python-fire/guide/

import os
import fire
#
# def hello(name):
#   return 'Hello {name}!'.format(name=name)
#
# if __name__ == '__main__':
#   fire.Fire()


################################### Example 2

# class Calculator():
#
#   def add(self, x, y):
#     return x + y
#
#   def multiply(self, x, y):
#     return x * y
#
# if __name__ == '__main__':
#   calculator = Calculator()
#   fire.Fire(calculator)


################################### Example 3

def znajdz_pliki_i_katalogi(katalog_startowy: str, fraza: str):
  """
  Ta funckja zajmuje sie znajdowaniem katalowgo i plikow. Ignoruje wielkosci liter
  Parameters
  ----------
  katalog_startowy - katalog od ktorego zaczniemy przeszukiwanie
  fraza - fraza ktora jest wyszukiwana w nazwach plikow i katalogow

  Returns
  -------

  """
  znalezione_elementy = []

  fraza = fraza.lower()

  for root, dirs, files in os.walk(katalog_startowy):
    for element in dirs + files:
      if fraza in element.lower():
        znalezione_elementy.append(os.path.join(root, element))

  print(znalezione_elementy)


if __name__ == "__main__":
  fire.Fire(znajdz_pliki_i_katalogi)