from math import floor


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
    return middle

def search(vector: list[int], number: int, k: int) -> list:
    result = []
    if number in vector:
        local = vector.index(n)
        for element in range(k):
            if element % 2 == 0:
                try:
                    result.append(vector[local+element+1])
                except IndexError:
                    result.append(vector[(local)+element*-1])
            else:
                try:
                    result.append(vector[(local)+element*-1])
                except IndexError:
                    result.append(vector[local+element+1])
        return result
    
    elif number not in vector:
        if number > vector[-1]:
            return vector[len(vector)-k:len(vector)]
        if number < vector[0]:
            return vector[0:k]
        else:
            value_closest = BinarySearch(vector, number)
            for element in range(k):
                if element % 2 == 0:
                    try:
                        result.append(vector[value_closest+element+1])
                    except IndexError:
                        result.append(vector[(value_closest)+element*-1])
                else:
                    try:
                        result.append(vector[(value_closest+1)+element*-1])
                    except IndexError:
                        result.append(vector[value_closest+element+1])
            return result


if __name__ =="__main__":
    a = [x for x in range(1, 20, 2)]
    n = 10
    k = 3
    print(a)
    print(sorted(search(a,n,k)))
