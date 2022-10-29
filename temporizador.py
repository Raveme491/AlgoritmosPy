import time


def temporizador(func):
    def inner(vetor, number):
        start = time.time()
        result = func(vetor, number)
        print(f'Tempo de Execução: {time.time()-start}')
        return result
    return inner
