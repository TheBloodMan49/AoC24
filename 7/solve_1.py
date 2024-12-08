def compute_rec(nums: [int], target: int, acc: int = 0) -> bool:
    if len(nums) == 0:
        return acc == target
    return (
            compute_rec(nums[1:], target, acc + nums[0]) or
            compute_rec(nums[1:], target, acc * nums[0])
            )

def check_line(line: str) -> int:
    result = int(line.split(":")[0])
    nums = list(map(int, line.split(":")[1].strip().split(" ")))

    if compute_rec(nums, result):
        return result
    return 0

def main():
    with open("input.txt") as f:
        lines = f.readlines()
        sum = 0
        for line in lines:
            sum += check_line(line)

        print(sum)

main()