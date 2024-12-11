from functools import lru_cache
from collections import defaultdict
from math import log
from time import perf_counter

def iteration(data: defaultdict) -> defaultdict:
    new_data = defaultdict(int)
    for elem, count in data.items():
        for new_elem in process_element(elem):
            new_data[new_elem] += count
    return new_data

@lru_cache(maxsize=None)
def process_element(elem: int) -> list[int]:
    if elem == 0:
        return [1]
    elif int(log(elem,10) + 1) % 2 == 0:
        length = int(log(elem,10) + 1)
        divisor = 10 ** (length // 2)
        first = elem // divisor
        second = elem % divisor
        return [first, second]
    else:
        return [elem * 2024]

def main(file: str):
    with open(file) as f:
        data = list(map(int, f.read().strip().split(" ")))
        data_dict = defaultdict(int, {elem: 1 for elem in data})

        start = perf_counter()

        for _ in range(75):
            data_dict = iteration(data_dict)

        print(f"Time: {perf_counter() - start}")

        #print(len(data_dict))
        print(sum(data_dict.values()))

main("input.txt")
