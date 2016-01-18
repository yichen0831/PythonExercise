#!/usr/bin/env python3


def create_odd_magic_matrix(n=5):
    if n % 2 == 0:
        raise ValueError('n must be an odd number')
    array = [[0 for _ in range(n)] for _ in range(n)]
    i = 0
    j = n // 2
    for v in range(1, n*n+1):
        array[i][j] = v
        next_i = i - 1
        next_j = j + 1

        if next_i < 0:
            next_i += n
        if next_j >= n:
            next_j -= n

        if array[next_i][next_j]:
            next_i = i + 1
            if next_i >= n:
                next_i -= n
            next_j = j
        i = next_i
        j = next_j
    return array


if __name__ == '__main__':
    odd_magic_matrix = create_odd_magic_matrix(n=5)

    for row in odd_magic_matrix:
        print(row)
