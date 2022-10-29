import time
from array import array
from math import floor
from random import randint

from temporizador import temporizador

a = sorted(array('i', [randint(0, 100) for _ in range(100)]))

@temporizador
def BinarySearch(vetor, number: int) -> int:
    left: int = 0
    right: int = len(vetor)-1
    middle: int = floor((right+left)/2)

    while middle < len(vetor):
        if vetor[middle] == number:
            return middle
        if vetor[middle] < number:
            left = middle + 1
        if vetor[middle] > number:
            right = middle - 1
        if left > right:
            break
        middle = floor((left+right)/2)
    raise Exception("Não existe esse valor na lista")


resultado = BinarySearch(a, 25)
print(f"A posição é {resultado}")
print(f"o valor é {a[resultado]}")
