from functools import cmp_to_key

import sys

fname = sys.argv[1]

with open(fname) as infile:
    lines = [line.strip() for line in infile.readlines()]
    
    
rules = [tuple(int(v) for v in s.split('|')) for s in lines if '|' in s]
updates = [[int(v) for v in s.split(',')] for s in lines if len(s) > 0 and '|' not in s]


def check_update(update, rules):
    # Flip update index <-> page number
    flipped = [-1 for _ in range(100)]
    
    for index, elem in enumerate(update):
        flipped[elem] = index
    
    for rule in rules:
        if flipped[rule[0]] != -1 and flipped[rule[1]] != -1:
            if flipped[rule[1]] < flipped[rule[0]]:
                return False
    
    return True


valid_updates = [u for u in updates if check_update(u, rules)]
middle_pages = [u[len(u)//2] for u in valid_updates]

print(f"Part 1: {sum(middle_pages)}")


invalid_updates = [u for u in updates if not check_update(u, rules)]


def sort_update(update, rules):
    return sorted(update, key=cmp_to_key(lambda i, j: -1 if (i, j) in rules else 1))


sorted_updates = [sort_update(u, rules) for u in invalid_updates]
middle_pages_2 = [u[len(u)//2] for u in sorted_updates]

print(f"Part 2: {sum(middle_pages_2)}")