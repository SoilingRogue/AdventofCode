area = []
start_i, start_j, direction = -1, None, None
with open("../input/day6.txt", "r") as f:
    for line in f:
        row = list(line.strip())
        area.append(row)
        if start_j is None:
            start_i += 1
            for j, ele in enumerate(row):
                if ele in "<>^v":
                    start_j = j
                    if ele == "<":
                        direction = "LEFT"
                    elif ele == ">":
                        direction = "RIGHT"
                    elif ele == "^":
                        direction = "UP"
                    else:
                        direction = "DOWN"


dir_to_dxdy = {"LEFT": (0, -1), "RIGHT": (0, 1), "UP": (-1, 0), "DOWN": (1, 0)}
next_dir = {"LEFT": "UP", "UP": "RIGHT", "RIGHT": "DOWN", "DOWN": "LEFT"}
rows = len(area)
cols = len(area[0])
i, j = start_i, start_j


def next_move(i, j, direction):
    next_i, next_j = dir_to_dxdy[direction][0] + i, dir_to_dxdy[direction][1] + j
    if 0 <= next_i < rows and 0 <= next_j < cols:
        if area[next_i][next_j] == "#":
            return i, j, next_dir[direction]
        return next_i, next_j, direction
    return next_i, next_j, direction


def move(i, j, direction):
    visited = set()
    while 0 <= i < rows and 0 <= j < cols:
        visited.add((i, j))
        i, j, direction = next_move(i, j, direction)
    return len(visited)


def move2(start_i, start_j, start_direction):
    global rows, cols, area
    obstacles = 0
    for row in range(rows):
        for col in range(cols):
            visited = set()
            i, j, direction = start_i, start_j, start_direction
            original = area[row][col]
            area[row][col] = "#"
            while True:
                if (i, j, direction) in visited:
                    obstacles += 1
                    break
                visited.add((i, j, direction))
                i, j, direction = next_move(i, j, direction)
                if not (0 <= i < rows and 0 <= j < cols):
                    break
            area[row][col] = original
    return obstacles


# print(move(i, j, direction))
print(move2(i, j, direction))
