#!/usr/bin/env python3

import random
import time


def _bubble_to_right(numbers, start_pos, target_right):
    right = start_pos
    for i in range(start_pos, target_right):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            right = i
    return right


def _bubble_to_left(numbers, start_pos, target_left):
    left = start_pos
    for i in range(start_pos, target_left, -1):
        if numbers[i] < numbers[i-1]:
            numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
            left = i
    return left


def improved_bubble_sorting(numbers):
    result = numbers[:]

    target_right = len(result)-1
    target_left = 0
    moved = True
    while moved:
        target_right = _bubble_to_right(result, target_left, target_right)
        target_left = _bubble_to_left(result, target_right, target_left)
        if target_left >= target_right:
            moved = False
    return result


if __name__ == '__main__':
    numbers = [random.randint(0, 9999) for _ in range(2000)]
    elapse = time.time()
    result = improved_bubble_sorting(numbers)
    elapse = time.time() - elapse
    print('Took {} secs'.format(elapse))
