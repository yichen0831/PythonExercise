#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def make_zero_matrix(m=1, n=1):
    if m == 0 or n == 0:
        return []

    matrix = []
    for i in range(m):
        row = [0 for j in range(n)]
        matrix.append(row)
    return  matrix


def restore_sparse_matrix(sparse, m=1, n=1):
    original_matrix = make_zero_matrix(m, n)
    for row in sparse:
        x, y, v = row
        original_matrix[x][y] = v
    return original_matrix


if __name__ == '__main__':
    sparse = [
        [1, 1, 3],
        [2, 3, 6],
        [3, 2, 9],
        [4, 4, 12],
    ]

    original_matrix = restore_sparse_matrix(sparse, m=5, n=6)
    for row in original_matrix:
        print(row)

