def convert_to_disk_map(data: str) -> list[int]:
    ctr = 0
    disk_map = []
    index = 0
    while index < len(data):
        for _ in range(int(data[index])):
            disk_map.append(ctr)
        if index+1 == len(data):
            break
        for _ in range(int(data[index+1])):
            disk_map.append(-1)
        ctr += 1
        index += 2
    return disk_map

def disk_map_to_string(disk_map: list[int]) -> str:
    return ''.join(map(lambda x: str(x) if x != -1 else '.',disk_map))

def defragment(data: list[int]) -> list[int]:
    index = len(data) - 1
    for i in range(len(data)):
        while data[index] == -1:
            index -= 1
        if data[i] == -1:
            data[i] = data[index]
            data[index] = -1
            index -= 1
        if index == i:
            break
    return data

def checksum(data: list[int]) -> int:
    res = 0
    for i in range(len(data)):
        if data[i] != -1:
            res += data[i] * i
    return res

def main(file: str) -> None:
    with open(file) as f:
        data = f.read().strip()
    #print(data)
    disk_map = convert_to_disk_map(data)
    #print(disk_map_to_string(disk_map))
    defrag_map = defragment(disk_map)
    #print(disk_map_to_string(defragment(disk_map)))
    print(checksum(defrag_map))

main("input.txt")
