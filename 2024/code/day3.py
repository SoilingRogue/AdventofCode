res = 0
memory = "".join([line for line in open("../input/day3.txt", "r").readlines()])
muls = memory.split("mul(")
n = len(muls)
do = muls[0].rfind("do()")
dont = muls[0].rfind("don't()")
is_do = do >= dont
for i in range(1, n):
    next_do = muls[i].rfind("do()")
    next_dont = muls[i].rfind("don't()")
    if is_do:
        numbers = muls[i].split(",")
        if len(numbers) >= 2 and numbers[0].isnumeric():
            for i in range(len(numbers[1])):
                if not numbers[1][i].isnumeric():
                    break
            if i != 0 and numbers[1][i] == ")":
                res += int(numbers[0]) * int(numbers[1][:i])
    if next_do != next_dont:
        is_do = next_do > next_dont

print(res)