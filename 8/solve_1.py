from typing import Dict


def main(file: str):
    with open(file) as f:
        existing_nodes = dict()
        matrix = [line.strip() for line in f.readlines()]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                tile = matrix[i][j]
                if tile != '.':
                    if not existing_nodes.get(tile):
                        existing_nodes[tile] = [(i,j)]
                    else:
                        existing_nodes[tile].append((i,j))

        #print(existing_nodes)

        antinodes = set()
        for node_type in existing_nodes:
            nodes = existing_nodes[node_type]
            for a_node in nodes:
                for b_node in nodes:
                    if a_node == b_node:
                        continue
                    else:
                        distance = (b_node[0]-a_node[0], b_node[1]-a_node[1])
                        new_antinode = (a_node[0]-distance[0], a_node[1]-distance[1])
                        if 0 <= new_antinode[0] < len(matrix) and 0 <= new_antinode[1] < len(matrix[0]):
                            antinodes.add(new_antinode)
                        new_antinode = (b_node[0]+distance[0], b_node[1]+distance[1])
                        if 0 <= new_antinode[0] < len(matrix) and 0 <= new_antinode[1] < len(matrix[0]):
                            antinodes.add(new_antinode)

        #print(antinodes)
        print(len(antinodes))

main('input.txt')