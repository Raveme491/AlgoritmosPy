import time
from array import array
from math import floor
from random import randint

start = time.time()
a = sorted(array('i', [randint(0, 100) for _ in range(100)]))


def BinarySearch(vetor: list[int], number: int) -> int:
    left: int = 0
    right: int = len(vetor)-1
    middle: int = floor((right+left)/2)

    while(middle < len(vetor)):
        if vetor[middle] == number:
            return middle
        if vetor[middle] < number:
            left = middle + 1
        if vetor[middle] > number:
            right = middle - 1
        if left > right:
            raise Exception("Não existe esse valor na lista")
        middle = floor((left+right)/2)


print(f'Array composto por:{a}')
print(f'a posição do elemento desejado é: {BinarySearch(a, 25)}')
print(f'Elemento desejado: {a[BinarySearch(a, 25)]}')
print(f'Tempo de Execução: {time.time()-start}')
