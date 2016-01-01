#!/usr/bin/env python3


def combi(r, n):
    p = 1
    for i in range(1, n+1):
        p = p * (r-i+1) / i
    return int(p)


def pascal(n):
    for row in range(n+1):
        print('    ' * (n - row), end='')
        for num in range(row+1):
            print('{:8}'.format(combi(row, num)), end='')

        print()


if __name__ == '__main__':
    pascal(10)
