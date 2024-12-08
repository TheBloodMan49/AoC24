from collections import defaultdict, deque

def parse_input(file_path):
    with open(file_path) as f:
        lines = f.read().strip().split('\n')

    rules = []
    updates = []
    is_update_section = False

    for line in lines:
        if line == '':
            is_update_section = True
            continue

        if is_update_section:
            updates.append(list(map(int, line.split(','))))
        else:
            x, y = map(int, line.split('|'))
            rules.append((x, y))

    return rules, updates

def is_correct_order(update, rules):
    index_map = {page: idx for idx, page in enumerate(update)}

    for x, y in rules:
        if x in index_map and y in index_map:
            if index_map[x] > index_map[y]:
                return False
    return True

def find_middle_page(update):
    return update[len(update) // 2]

def topological_sort(pages, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for x, y in rules:
        if x in pages and y in pages:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_pages = []

    while queue:
        node = queue.popleft()
        sorted_pages.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages

def main(file_path):
    rules, updates = parse_input(file_path)
    total_sum = 0

    for update in updates:
        if not is_correct_order(update, rules):
            sorted_update = topological_sort(update, rules)
            total_sum += find_middle_page(sorted_update)

    print(total_sum)

main('input.txt')