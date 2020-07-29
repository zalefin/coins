from collections import defaultdict
from copy import deepcopy

import numpy as np


def _least_path(n, cache, denom):
    if n in cache.keys():
        combos = cache[n]
        return combos[np.argmin(list(map(lambda l: len(l), combos)))]
    for c in denom:
        if c <= n:
            r = n - c
            cache[n].append(_least_path(r, cache, denom) + [ c ])
    if n in cache.keys():
        combos = cache[n]
        return combos[np.argmin(list(map(lambda l: len(l), combos)))]
    else:
        return []

def least_path(n, denom):
    denom = sorted(denom, reverse=True) # shave recursion times by taking largest coin first
    cache = defaultdict(list) # our cache of outcomes during DP recursion
    r = _least_path(n, cache, denom)
    if sum(r) != n:
        return -1
    else:
        return len(r), r


if __name__ == "__main__":
    print(least_path(6, [1, 5, 6, 8]))
    print(least_path(17, [1, 5, 6, 8]))
    print(least_path(2750, [1, 3, 7, 11]))
    print(least_path(13593, [1, 5, 10, 100, 1000]))
