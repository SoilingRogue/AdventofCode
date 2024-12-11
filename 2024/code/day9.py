with open("../input/day9.txt") as f:
    memory = list(map(int, f.readline().strip()))

n = len(memory)
if n & 1:
    last_file_pos = n - 1
    last_file_id = n // 2
else:
    last_file_id = n // 2 - 1
    last_file_pos = n - 2

checksum = 0
current_start = 0
curr_id = 0
mem_copy = memory.copy()
for i in range(n):
    # if curr_id > last_file_id:  ### PART 1 ###
    #     break
    val = memory[i]
    current_end = current_start + val
    if i & 1:
        ### PART 1 ###
        # while val:
        #     needed = memory[last_file_pos]
            # if val >= needed:
            #     for pos in range(current_start, current_start + needed):
            #         checksum += pos * last_file_id
            #     last_file_id -= 1
            #     last_file_pos -= 2
            #     val -= needed
            #     current_start += needed
            # else:
            #     memory[last_file_pos] -= val
            #     for pos in range(current_start, current_end):
            #         checksum += pos * last_file_id
            #     val = 0

        ### PART 2 ###
        last_id = last_file_id
        last_pos = last_file_pos
        while val and curr_id <= last_id:
            needed = memory[last_pos]
            if val >= needed and needed:
                for pos in range(current_start, current_start + needed):
                    checksum += pos * last_id
                memory[last_pos] = 0
                val -= needed
                current_start += needed
            last_id -= 1
            last_pos -= 2
    else:
        for pos in range(current_start, current_end):
            checksum += pos * curr_id
        curr_id += 1
        if not val:  ### PART 2 ###
            current_end += mem_copy[i]
    current_start = current_end

print(checksum)
