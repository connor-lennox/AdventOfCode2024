import sys

fname = sys.argv[1]

with open(fname) as infile:
    lines = infile.readlines()


left_list = [int(line.split()[0]) for line in lines]
right_list = [int(line.split()[1]) for line in lines]

left_list.sort()
right_list.sort()

diffs = [abs(l-r) for (l,r) in zip(left_list, right_list)]

print(f"Part 1: {sum(diffs)}")

occs = {}

for elem in right_list:
    if elem not in occs:
        occs[elem] = 0
    occs[elem] += 1

p2_sums = [e * occs.get(e, 0) for e in left_list]

print(f"Part 2: {sum(p2_sums)}")
