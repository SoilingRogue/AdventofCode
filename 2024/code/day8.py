from collections import defaultdict


freq_to_coord = defaultdict(list)
cols = None
rows = 0
with open("../input/day8.txt") as f:
    for line in f:
        arr = list(line.strip())
        if cols is None:
            cols = len(arr)
        for col, c in enumerate(arr):
            if c != ".":
                freq_to_coord[c].append((rows, col))
        rows += 1

antinodes = set()
for freq, coords in freq_to_coord.items():
    n = len(coords)
    for i in range(n):
        for j in range(i + 1, n):
            xi, yi = coords[i]
            xj, yj = coords[j]
            x_diff, y_diff = xi - xj, yi - yj
            first_anti = xi + x_diff, yi + y_diff
            antinodes.add(coords[i])
            antinodes.add(coords[j])
            while 0 <= first_anti[0] < rows and 0 <= first_anti[1] < cols:
                antinodes.add(first_anti)
                first_anti = first_anti[0] + x_diff, first_anti[1] + y_diff
                # print(coords[i], coords[j], "anti1", first_anti)
            second_anti = xj - x_diff, yj - y_diff
            while 0 <= second_anti[0] < rows and 0 <= second_anti[1] < cols:
                antinodes.add(second_anti)
                second_anti = second_anti[0] - x_diff, second_anti[1] - y_diff
                # print(coords[i], coords[j], "anti2", second_anti)

print(len(antinodes))
