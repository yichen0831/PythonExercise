#!/usr/bin/env python3


def create_4n_magic_matrix(n=4):
    if n % 4 != 0:
        raise ValueError('n must be multiple of 4')
    array1 = [[0 for _ in range(n)] for _ in range(n)]
    array2 = [[0 for _ in range(n)] for _ in range(n)]

    for v in range(n*n):
        i = v // n
        j = v % n
        if ((i % 4) == (j % 4)) or (((i+1) % 4 + (j+1)) % 4 == 1):
            array2[i][j] = n*n - (v+1) + 1
        else:
            array1[i][j] = v + 1

    result_array = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result_array[i][j] = array1[i][j] if array1[i][j] else array2[i][j]
    return result_array


if __name__ == '__main__':
    magic_matrix = create_4n_magic_matrix(n=4)

    for row in magic_matrix:
        print(row)
