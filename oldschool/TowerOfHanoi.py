#!/usr/bin/env python3


def hanoi(n, a, b, c):
    if n == 1:
        print('Move from ' + a + ' to ' + c)

    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)


if __name__ == '__main__':
    hanoi(3, 'A', 'B', 'C')