#!/usr/bin/env python
# -*- coding: utf-8 -*-

class UpperTriangleMatrix:
    def __init__(self, array):
        """
        array is a m*m upper triangle array/matrix
        """
        self._m = len(array)
        self._array = []
        for row in array:
            for v in row:
                if v != 0:
                    self._array.append(v)

    def get_original_matrix(self):
        original_matrix = []
        for i in range(self._m):
            row = []
            for j in range(self._m):
                if i > j:
                    row.append(0)
                else:
                    v = self._array[self._m * i - (i+1) * i//2 + (j)]
                    row.append(v)
            original_matrix.append(row)
        return original_matrix

    def __str__(self):
        original_matrix = self.get_original_matrix()
        return '\n'.join(map(str, original_matrix))


class LowerTriangleMatrix:
    def __init__(self, array):
        """
        array is a m*m lower triangle array/matrix
        """
        self._m = len(array)
        self._array = []
        for row in array:
            for v in row:
                if v != 0:
                    self._array.append(v)

    def get_original_matrix(self):
        original_matrix = []
        for i in range(self._m):
            row = []
            for j in range(self._m):
                if i < j:
                    row.append(0)
                else:
                    v = self._array[i*(i+1)//2 + j]
                    row.append(v)
            original_matrix.append(row)
        return original_matrix

    def __str__(self):
        original_matrix = self.get_original_matrix()
        return '\n'.join(map(str, original_matrix))


if __name__ == '__main__':
    upper_array = [
        [1, 2, 3, 4, 5],
        [0, 6, 7, 8, 9],
        [0, 0, 10, 11, 12],
        [0, 0, 0, 13, 14],
        [0, 0, 0, 0, 15]
    ]

    lower_array = [
        [1, 0, 0, 0, 0],
        [2, 3, 0, 0, 0],
        [4, 5, 6, 0, 0],
        [7, 8, 9, 10, 0],
        [11, 12, 13, 14, 15]
    ]

    upper_triangle_matrix = UpperTriangleMatrix(upper_array)
    print(upper_triangle_matrix)

    print('* ' * 8)

    lower_triangle_matrix = LowerTriangleMatrix(lower_array)
    print(lower_triangle_matrix)
