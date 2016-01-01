#!/usr/bin/env python3


def calculate_ranks(scores):
    ranks = []

    for score in scores:
        r = 1
        for cmp in scores:
            if score < cmp:
                r += 1
        ranks.append(r)

    result = zip(scores, ranks)
    for score, rank in result:
        print('Score {:3} ranks {:2}'.format(score, rank))


if __name__ == '__main__':
    scores = [100, 99, 99, 97, 88, 83, 99, 74, 78, 89]
    calculate_ranks(scores)
