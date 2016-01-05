#!/usr/bin/env python3

import time


def eratosthenes_primes(num):
    numbers = [False for _ in range(num+1)]
    numbers[2] = True
    numbers[3] = True
    numbers[5] = True
    i = 1
    while i * 6 + 5 <= num:
        numbers[i * 6 + 1] = True
        numbers[i * 6 + 5] = True
        i += 1

    if i * 6 + 1 <= num:
        numbers[i*6+1] = True

    n = 0
    while (n * 6 + 5)**2 <= num:
        filter_it(numbers, n*6+5)
        filter_it(numbers, n*6+1)
        n += 1
    if (n * 6 + 1)**2 <= num:
        filter_it(numbers, n*6+1)

    return [i for i in range(num+1) if numbers[i] == True]


def filter_it(numbers, n):
    if n == 1:
        return
    i = 2
    while n * i < len(numbers):
        numbers[n*i] = False
        i += 1


if __name__ == '__main__':
    elapse = time.time()
    result = eratosthenes_primes(5000)
    elapse = time.time() - elapse
    print('took {} secs'.format(elapse))

    print(len(result))
