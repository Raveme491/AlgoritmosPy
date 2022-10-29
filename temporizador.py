import time


def temporizador(func):
    def inner(*args, **kwargs):
        start = time.time()
        result = func(*args, *kwargs)
        print(f'Tempo de Execução: {time.time()-start}')
        return result
    return inner
