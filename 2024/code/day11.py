from collections import Counter
from functools import cache


with open("../input/day11.txt") as f:
    rocks = Counter(list(map(int, list(f.readline().strip().split(" ")))))


@cache
def get_next_rocks(rock):
    if rock == 0:
        return [1]
    str_rock = str(rock)
    n = len(str_rock)
    if n & 1:
        return [rock * 2024]
    return [int(str_rock[:n // 2]), int(str_rock[n // 2:])]


### PART 1 ###
blinks = 25
### PART 2 ###
blinks = 75
for _ in range(blinks):
    new_rocks = Counter()
    for rock, count in rocks.items():
        for new_rock in get_next_rocks(rock):
            new_rocks[new_rock] += count
    rocks = new_rocks

print(sum(rocks.values()))
