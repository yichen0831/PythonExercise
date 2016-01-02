#!/usr/bin/env python3


import time
import random


class Heap:

    def __init__(self, numbers=[]):
        self.heap_tree = []
        for number in numbers:
            self.put(number)

    def put(self, number):
        self.heap_tree.append(number)
        pos = len(self.heap_tree) - 1
        while pos > 0:
            parent = (pos - 1) // 2
            if self.heap_tree[pos] < self.heap_tree[parent]:
                self.heap_tree[pos], self.heap_tree[parent] = self.heap_tree[parent], self.heap_tree[pos]
                pos = parent
            else:
                break

    def take(self):
        taken = self.heap_tree[0]
        self.heap_tree[0], self.heap_tree[-1] = self.heap_tree[-1], self.heap_tree[0]
        self.heap_tree.pop(-1)
        pos = 0

        while True:
            # 2 child nodes
            if len(self.heap_tree) > pos * 2 + 2:
                left_child = pos * 2 + 1
                right_child = pos * 2 + 2
                compare = pos
                if self.heap_tree[left_child] < self.heap_tree[right_child]:
                    compare = left_child
                else:
                    compare = right_child

                if self.heap_tree[pos] > self.heap_tree[compare]:
                    self.heap_tree[pos], self.heap_tree[compare] = self.heap_tree[compare], self.heap_tree[pos]
                    pos = compare
                else:
                    break
            # 1 child node
            elif len(self.heap_tree) > pos * 2 + 1:
                compare = pos * 2 + 1
                if self.heap_tree[pos] > self.heap_tree[compare]:
                    self.heap_tree[pos], self.heap_tree[compare] = self.heap_tree[compare], self.heap_tree[pos]
                    pos = compare
                else:
                    break
            # no child
            else:
                break

        return taken

    def print(self):
        breakline = 1
        count = 0
        for i in range(len(self.heap_tree)):
            print('{:4}'.format(self.heap_tree[i]), end='')
            count += 1

            if count >= breakline:
                count = 0
                breakline *= 2
                print()


if __name__ == '__main__':
    numbers = [random.randint(0, 9999) for _ in range(2000)]

    elapse = time.time()
    heap = Heap(numbers)
    elapse = time.time() - elapse
    print('Took {} secs'.format(elapse))

    result = []
    while len(heap.heap_tree) > 0:
        result.append(heap.take())

    print(result)
