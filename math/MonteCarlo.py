#!/usr/bin/env python3

import random


def get_pi_by_sequence(numbers):
    count = 0
    for i in range(numbers):
        x = float(i) / numbers
        for j in range(numbers):
            y = float(j) / numbers
            if x**2 + y**2 < 1:
                count += 1
    return count / (numbers**2) * 4.0


def get_pi_by_random(numbers):
    count = 0
    for i in range(numbers):
        x = random.random()
        y = random.random()

        if x**2 + y**2 < 1:
            count += 1
    return count / numbers * 4.0


if __name__ == '__main__':
    print(get_pi_by_random(90000))
    print(get_pi_by_sequence(300))
