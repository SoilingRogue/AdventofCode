### PART 1 ###
def is_safe(arr):
    n = len(arr)
    is_inc = arr[1] > arr[0]
    for i in range(1, n):
        diff = arr[i] - arr[i - 1]
        if (is_inc and 0 < diff <= 3) or ((not is_inc) and -3 <= diff < 0):
            continue
        return False
    return True


### PART 2 ###
def is_safe2(arr):
    if is_safe(arr):
        return True
    for i in range(len(arr)):  # prob exists a faster method
        if is_safe(arr[:i] + arr[i + 1:]):
            return True
    return False


num_safe = 0
with open("../input/day2.txt") as f:
    for line in f:
        arr = list(map(lambda x: int(x), line.split(" ")))
        # if is_safe(arr):
        #     num_safe += 1
        if is_safe2(arr):
            num_safe += 1

print(num_safe)
