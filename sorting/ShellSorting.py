#!/usr/bin/env python3

import random
import time
from functools import reduce


def _interval_insertion_sorting(numbers, interval):
    for start in range(interval):
        processed = start

        while processed < len(numbers):
            pos = start
            # find the pos for insertion
            for i in range(start, processed, interval):
                if numbers[i] > numbers[processed]:
                    break
                pos = i + interval

            # make the number move to pos
            for i in range(processed, pos, -interval):
                numbers[i], numbers[i-interval] = numbers[i-interval], numbers[i]
            processed += interval


def shell_sorting_v1(numbers):
    result = numbers[:]

    interval = len(result) // 2
    while interval:
        # do insertion sorting per interval
        _interval_insertion_sorting(result, interval)
        interval //= 2

    return result


def _insertion_sorting(numbers):
    result = []

    for number in numbers:
        for i in range(len(result)-1, -1, -1):
            if number > result[i]:
                result.insert(i+1, number)
                break
        else:
            result.insert(0, number)

    return result


def shell_sorting_v2(numbers):
    result = numbers[:]

    def mk_interval(init):
        interval = init
        while interval > 1:
            interval //= 2
            yield interval

    intervals = [itv for itv in mk_interval(len(result))]
    for interval in intervals:
        tmp = []

        for i in range(interval):
            tmp.append(_insertion_sorting(result[i::interval]))

        result = []
        for i in tmp:
            for j in i:
                result += [j]
    return result


if __name__ == '__main__':
    numbers_to_sort = [random.randint(1, 9999) for _ in range(2000)]

    elapse = time.time()
    result = shell_sorting_v2(numbers_to_sort)
    elapse = time.time() - elapse
    print('Shell sorting v2 took {} secs'.format(elapse))

    elapse = time.time()
    result = shell_sorting_v1(numbers_to_sort)
    elapse = time.time() - elapse
    print('Shell sorting v1 took {} secs'.format(elapse))
