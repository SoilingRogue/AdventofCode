from collections import defaultdict


ordering = defaultdict(set)
adj = defaultdict(set)
updates = []

with open("../input/day5.txt", "r") as f:
    is_order = True
    for line in f:
        if line == "\n":
            is_order = False
            continue
        if is_order:
            first, second = line.split("|")
            first, second = int(first), int(second)
            ordering[second].add(first)
            adj[first].add(second)
        else:
            updates.append([int(i) for i in line.split(",")])


def build_indeg(order_set, update_set):
    indeg = defaultdict(int)
    for node in update_set:
        indeg[node] = len(order_set[node].intersection(update_set))
    return indeg


sum_of_valid_mids = 0
sum_of_invalid_mids = 0
for update in updates:
    update_set = set(update)
    indeg = build_indeg(ordering, update_set)
    is_valid = True
    ### PART 1 ###
    for node in update:
        if indeg[node] != 0:
            is_valid = False
            break
        for other_node in (adj[node] - {node}).intersection(update_set):
            indeg[other_node] -= 1
    if is_valid:
        sum_of_valid_mids += update[len(update) // 2]

    ### PART 2 ###
    else:
        indeg = build_indeg(ordering, update_set)
        order = []
        valid = []
        for node in update_set:
            if not indeg[node]:
                valid.append(node)
        visited = set(valid)
        while valid:
            node = valid.pop()
            order.append(node)
            for other_node in (adj[node] - {node}).intersection(update_set):
                indeg[other_node] -= 1
                if not indeg[other_node] and other_node not in visited:
                    valid.append(other_node)
                    visited.add(other_node)

        sum_of_invalid_mids += order[len(order) // 2]

print(sum_of_valid_mids)
print(sum_of_invalid_mids)