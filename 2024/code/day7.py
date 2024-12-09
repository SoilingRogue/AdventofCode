from functools import cache


@cache
def calc(target, curr, idx):
    if idx == len(remaining):
        return target == curr
    
    if target < curr:
        return False
    ele = remaining[idx]
    part1 = calc(target, curr + ele, idx + 1) or calc(target, curr * ele, idx + 1)
    if part1:
        return True
    part2 = calc(target, int(str(curr) + str(ele)), idx + 1)
    return part2


valid_equations = 0
with open("../input/day7.txt") as f:
    for line in f:
        arr = line.split(" ")
        target = int(arr[0].split(":")[0])
        remaining = list(map(int, arr[1:]))
        if calc(target, remaining[0], 1):
            valid_equations += target

print(valid_equations)