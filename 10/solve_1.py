
def number_of_trails(data: list[list[int]], pos: tuple[int,int], current: int, target: int) -> set[tuple[int,int]]:
    #print(f"pos: {pos}, current: {current}")
    if current == target:
        #print(f"Trail end at {pos}")
        return {pos}
    res = set()
    if pos[0] > 0 and data[pos[0]-1][pos[1]] == current+1:
        res = res.union(number_of_trails(data, (pos[0]-1, pos[1]), current+1, target))
    if pos[0] < len(data)-1 and data[pos[0]+1][pos[1]] == current+1:
        res = res.union(number_of_trails(data, (pos[0]+1, pos[1]), current+1, target))
    if pos[1] > 0 and data[pos[0]][pos[1]-1] == current+1:
        res = res.union(number_of_trails(data, (pos[0], pos[1]-1), current+1, target))
    if pos[1] < len(data[0])-1 and data[pos[0]][pos[1]+1] == current+1:
        res = res.union(number_of_trails(data, (pos[0], pos[1]+1), current+1, target))
    return res

def main(file: str):
    with open(file) as f:
        data = [[int(x) for x in line.strip()] for line in f.readlines()]
        #print(data)
        target = max(max(row) for row in data)
        res = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] == 0:
                    cur_set = number_of_trails(data, (i, j), 0, target)
                    res += len(cur_set)

        print(res)

main('input.txt')