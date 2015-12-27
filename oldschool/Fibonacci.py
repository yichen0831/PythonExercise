#!/usr/bin/env python3


def fibonacci(n):
    n1 = 0
    n2 = 1

    for i in range(n):
        result = n2
        n2 += n1
        n1 = result
        print(str(result), end=' ')


if __name__ == '__main__':
    fibonacci(12)