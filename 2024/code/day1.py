from collections import Counter


first_lst = []
second_lst = []
first_count = Counter()
second_count = Counter()

with open("../input/day1.txt") as f:
    for line in f:
        arr = line.split(" ")
        first, second = int(arr[0]), int(arr[-1])
        first_lst.append(first)
        second_lst.append(second)
        first_count[first] += 1
        second_count[second] += 1


### PART 1 ###
dist = 0
for first, second in zip(sorted(first_lst), sorted(second_lst)):
    dist += abs(first - second)

print(dist)


### PART 2 ###
sim = 0
for first in first_count.keys():
    sim += first * second_count[first] * first_count[first]

print(sim)