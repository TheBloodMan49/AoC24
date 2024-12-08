

def main(file: str):
    with open(file) as f:
        nodes = dict()
        matrix = [line.strip() for line in f.readlines()]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tile = matrix[i][j]
                if tile != '.':
                    if not nodes.get(tile):
                        nodes[tile] = [(i,j)]
                    else:
                        nodes[tile].append((i,j))

        print(nodes)

        antinodes = []
        for

main('input_test.txt')