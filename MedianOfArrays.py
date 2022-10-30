from random import randint


def merge(*args: list[int]) -> list[int]:
    z: list = []
    for element in args:
        z.extend(element)
    return sorted(z)


def mediana(vetor: list[int]) -> float:
    tamanho_vetor: int = len(vetor)

    if tamanho_vetor % 2 != 0:
        return vetor[int((tamanho_vetor+1)/2)-1]
    else:
        return (vetor[int(tamanho_vetor/2)] + vetor[int(tamanho_vetor/2 - 1)])/2


if __name__ == "__main__":
    a = [randint(0, 15) for _ in range(randint(10, 15))]
    b = [randint(-10, 19) for _ in range(randint(10, 15))]
    
    vector = merge(a, b)
    mediana_vector = mediana(vector)
    print(vector)
    print(f"o tamanho do vetor é: {len(vector)}")
    print(f"a mediana é: {mediana_vector}")
    
    print("------------")
    print(mediana(merge(a, b)))  # Funcão recebendo função
    