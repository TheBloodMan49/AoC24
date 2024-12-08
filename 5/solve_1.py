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

def main(file_path):
    rules, updates = parse_input(file_path)
    total_sum = 0

    for update in updates:
        if is_correct_order(update, rules):
            total_sum += find_middle_page(update)

    print(total_sum)

main('input.txt')