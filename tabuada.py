"""Tabuada do 1 a 10."""
__version__ = "0.1.0"
__author__ = "Matheus"

numeros = list(range(1, 11))

for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(outro_numero * numero)
    print("---------")