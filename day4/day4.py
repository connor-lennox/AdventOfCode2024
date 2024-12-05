import sys

fname = sys.argv[1]

with open(fname) as infile:
    lines = [line.strip() for line in infile.readlines()]

max_x = len(lines[0])
max_y = len(lines)

found = 0

def check(start_x, start_y, offsets):
    return [lines[start_y + o[1]][start_x + o[0]] for o in offsets] == ["X", "M", "A", "S"]


def check_set(x_range, y_range, offsets):
    found_in_set = 0
    for x in x_range:
        for y in y_range:
            if check(x, y, offsets):
                found_in_set += 1
    return found_in_set

forward = check_set(range(0, max_x - 3), range(0, max_y), [(0, 0), (1, 0), (2, 0), (3, 0)])
backward = check_set(range(3, max_x), range(0, max_y), [(0, 0), (-1, 0), (-2, 0), (-3, 0)])
down = check_set(range(0, max_x), range(0, max_y-3), [(0, 0), (0, 1), (0, 2), (0, 3)])
up = check_set(range(0, max_x), range(3, max_y), [(0, 0), (0, -1), (0, -2), (0, -3)])

diag_right_down = check_set(range(0, max_x-3), range(0, max_y-3), [(0, 0), (1, 1), (2, 2), (3, 3)])
diag_right_up = check_set(range(0, max_x-3), range(3, max_y), [(0, 0), (1, -1), (2, -2), (3, -3)])
diag_left_down = check_set(range(3, max_x), range(0, max_y-3), [(0, 0), (-1, 1), (-2, 2), (-3, 3)])
diag_left_up = check_set(range(3, max_x), range(3, max_y), [(0, 0), (-1, -1), (-2, -2), (-3, -3)])

# print(forward)
# print(backward)
# print(down)
# print(up)
# print(diag_right_down)
# print(diag_left_down)
# print(diag_right_up)
# print(diag_left_up)

print(f"Part 1: {forward + backward + down + up + diag_right_down + diag_right_up + diag_left_down + diag_left_up}")


valid_p2_seqs = [
    ["M", "S", "A", "M", "S"],
    ["S", "M", "A", "S", "M"],
    ["M", "M", "A", "S", "S"],
    ["S", "S", "A", "M", "M"]
]

def check_2(start_x, start_y, offsets):
    res = [lines[start_y + o[1]][start_x + o[0]] for o in offsets]
    return res in valid_p2_seqs

found_p2 = 0

for x in range(1, max_x-1):
    for y in range(1, max_y-1):
        if check_2(x, y, [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)]):
            found_p2 += 1

print(f"Part 2: {found_p2}")
