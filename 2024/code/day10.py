trial = []
with open("../input/day10.txt") as f:
    for line in f:
        trial.append(list(map(int, list(line.strip()))))


rows = len(trial)
cols = len(trial[0])
score = [[-1] * cols for _ in range(rows)]


### PART 1 ###
def dfs1(row, col, visited):
    if trial[row][col] == 9:
        visited.add((row, col))
        return

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dy, col + dx
        if new_row < 0 or new_row == rows or new_col < 0 or new_col == cols:
            continue
        
        next_val = trial[new_row][new_col]
        if next_val - trial[row][col] == 1:
            dfs1(new_row, new_col, visited)


### PART 2 ###
def dfs2(row, col):
    if trial[row][col] == 9:
        return 1
    if score[row][col] == -1:
        curr_score = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dy, col + dx
            if new_row < 0 or new_row == rows or new_col < 0 or new_col == cols:
                continue
            
            next_val = trial[new_row][new_col]
            if next_val - trial[row][col] == 1:
                curr_score += dfs2(new_row, new_col)
        score[row][col] = curr_score
    return score[row][col]


sum_scores = 0
for row in range(rows):
    for col in range(cols):
        if trial[row][col] == 0:
            # visited = set()
            # dfs1(row, col, visited)
            # sum_scores += len(visited)
            sum_scores += dfs2(row, col)

print(sum_scores)
