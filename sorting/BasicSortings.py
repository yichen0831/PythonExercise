#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random


def selection_sorting(numbers):
    result = numbers[:]

    processed = 0
    # find the smallest number and move it to the head
    while processed < len(result):
        smallest = processed
        for i in range(processed, len(result)):
            if result[smallest] > result[i]:
                smallest = i
        result[processed], result[smallest] = result[smallest], result[processed]
        processed += 1
    return result


def insertion_sorting(numbers):
    result = numbers[:]

    processed = 0
    while processed < len(result):
        pos = 0
        for i in range(processed):
            if result[i] > result[processed]:
                break
            pos = i + 1

        # make room for insertion
        for i in range(processed, pos, -1):
            result[i], result[i-1] = result[i-1], result[i]
        processed += 1
    return result


def insertion_sorting_v2(numbers):
    result = numbers[:]
    processed = 0
    while processed < len(result):
        pos = 0
        for i in range(processed):
            if result[i] > result[processed]:
                break
            pos += 1

        num = result[processed]
        del result[processed]
        result = result[:pos] + [num] + result[pos:]
        processed += 1

    return result


def insertion_sorting_v3(numbers):
    result = []

    for number in numbers:
        for i in range(len(result)):
            if number < result[i]:
                result.insert(i, number)
                break
        else:
            result.append(number)

    return result


def bubble_sorting(numbers):
    result = numbers[:]

    processed = 0
    while processed < len(result):
        for i in range(len(result) - processed - 1):
            if result[i] > result[i + 1]:
                result[i], result[i+1] = result[i+1], result[i]
        processed += 1
    return result


if __name__ == '__main__':
    numbers_to_sort = [random.randint(1, 9999) for _ in range(2000)]

    elapse = time.time()
    result = selection_sorting(numbers_to_sort)
    elapse = time.time() - elapse
    print('Selection sorting took {} secs'.format(elapse))

    elapse = time.time()
    result = insertion_sorting(numbers_to_sort)
    elapse = time.time() - elapse
    print('Insertion sorting took {} secs'.format(elapse))

    elapse = time.time()
    result = insertion_sorting_v2(numbers_to_sort)
    elapse = time.time() - elapse
    print('Insertion sorting v2 took {} secs'.format(elapse))

    elapse = time.time()
    result = insertion_sorting_v3(numbers_to_sort)
    elapse = time.time() - elapse
    print('Insertion sorting v3 took {} secs'.format(elapse))

    elapse = time.time()
    result = bubble_sorting(numbers_to_sort)
    elapse = time.time() - elapse
    print('Bubble sorting took {} secs'.format(elapse))

    elapse = time.time()
    result = sorted(numbers_to_sort)
    elapse = time.time() - elapse
    print('Built-in sorting took {} secs'.format(elapse))
