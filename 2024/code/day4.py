arr = []
with open("../input/day4.txt", "r") as f:
    for line in f:
        arr.append(list(line))

curr_to_next = {"X": "M", "M": "A", "A": "S"}
rows = len(arr)
cols = len(arr[0])


### PART 1 ###
def find(i, j, c="X", dir=None):
    if i < 0 or j < 0 or i == rows or j == cols or arr[i][j] != c:
        return 0
    if c not in curr_to_next:
        return 1
    count = 0
    next_c = curr_to_next[c]
    if dir is None:
        count += find(i, j + 1, next_c, (0, 1))
        count += find(i, j - 1, next_c, (0, -1))
        count += find(i + 1, j, next_c, (1, 0))
        count += find(i - 1, j, next_c, (-1, 0))
        count += find(i + 1, j + 1, next_c, (1, 1))
        count += find(i + 1, j - 1, next_c, (1, -1))
        count += find(i - 1, j + 1, next_c, (-1, 1))
        count += find(i - 1, j - 1, next_c, (-1, -1))
    else:
        count = find(i + dir[0], j + dir[1], next_c, dir)
    return count


### PART 2 ###
def find2(i, j, c="A"):
    if i < 0 or j < 0 or i == rows or j == cols or arr[i][j] != c:
        return 0
    if c != "A":
        return 1
    valid_pos_diag = (find2(i - 1, j - 1, "M") and find2(i + 1, j + 1, "S")) or (find2(i - 1, j - 1, "S") and find2(i + 1, j + 1, "M"))
    valid_neg_diag = (find2(i - 1, j + 1, "M") and find2(i + 1, j - 1, "S")) or (find2(i - 1, j + 1, "S") and find2(i + 1, j - 1, "M"))
    if valid_pos_diag and valid_neg_diag:
        return 1
    return 0


res = 0
for row in range(1, rows):
    for col in range(1, cols):
        # res += find(row, col)
        res += find2(row, col)

print(res)