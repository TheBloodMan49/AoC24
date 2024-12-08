def is_safe_sequence(nums):
    prev_num = int(nums[0])
    mode = None
    if prev_num < int(nums[1]):
        mode = "inc"
    elif prev_num > int(nums[1]):
        mode = "dec"
    else:
        return False

    for i in range(1, len(nums)):
        num = int(nums[i])
        if mode == "inc" and (num <= prev_num or num - prev_num > 3):
            return False
        elif mode == "dec" and (num >= prev_num or prev_num - num > 3):
            return False
        prev_num = num

    return True

with open("input.txt") as f:
    total_sum = 0

    for line in f:
        nums = line.split(" ")
        if is_safe_sequence(nums):
            total_sum += 1
            continue

        safe = False
        for i in range(len(nums)):
            modified_nums = nums[:i] + nums[i+1:]
            if is_safe_sequence(modified_nums):
                safe = True
                break

        if safe:
            total_sum += 1

    print(total_sum)