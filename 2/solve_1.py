with open("input.txt") as f:
    sum = 0

    for line in f:
        nums = line.split(" ")
        safe = True
        prev_num = int(nums[0])
        mode = None
        if prev_num < int(nums[1]):
            mode = "inc"
        elif prev_num > int(nums[1]):
            mode = "dec"
        else:
            safe = False
        for num in nums[1:]:
            num = int(num)
            if mode == "inc" and (num <= prev_num or num - prev_num > 3):
                safe = False
                break
            if mode == "dec" and (num >= prev_num or prev_num - num > 3):
                safe = False
                break
            prev_num = num

        if safe:
            sum += 1

    print(sum)