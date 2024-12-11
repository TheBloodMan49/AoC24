from time import perf_counter

def iteration(data: list[int]) -> list[int]:
    new_data = []
    for elem in data:
        if elem == 0:
            new_data.append(1)
        elif len(str(elem)) % 2 == 0:
            string = str(elem)
            first = string[:len(string)//2]
            second = string[len(string)//2:]
            new_data.append(int(first))
            new_data.append(int(second))
        else:
            new_data.append(elem*2024)
    return new_data

def main(file: str):
    with open(file) as f:
        data = map(int,f.read().strip().split(" "))

        start = perf_counter()

        for _ in range(25):
            data = iteration(data)

        print(f"Time: {perf_counter() - start}")

        print(len(data))

main("input.txt")
