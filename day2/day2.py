import sys

fname = sys.argv[1]

with open(fname) as infile:
    lines = infile.readlines()

seqs = [[int(v) for v in line.split()] for line in lines]


def validate(seq):
    cur = seq[0]
    increasing = seq[1] > seq[0]
    
    for sub in seq[1:]:
        if increasing and (sub <= cur or sub > (cur + 3)):
            return False
        
        elif not increasing and (sub >= cur or sub < (cur - 3)):
            return False
        cur = sub
    
    return True


validations = [validate(seq) for seq in seqs]
validations_count = sum([1 for v in validations if v])

print(f"Part 1: {validations_count}")


validations_2 = [any(validate(seq[:i] + seq[i+1:]) for i in range(len(seq))) for seq in seqs]
validations_2_count = sum([1 for v in validations_2 if v])

print(f"Part 2: {validations_2_count}")
