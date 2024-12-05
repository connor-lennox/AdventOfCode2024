import re
import sys

fname = sys.argv[1]

with open(fname) as infile:
    content = infile.read().replace('\n', '')


regex_string = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"

valid_muls = [(int(m[0]), int(m[1])) for m in re.findall(regex_string, content)]
print(f"Part 1: {sum([m[0] * m[1] for m in valid_muls])}")


trim_regex = r"don't\(\)(.*?)(?:do\(\)|$)"

trim_matches = list(re.finditer(trim_regex, content))
trim_matches.reverse()
trimmed_content = content
for match in trim_matches:
    trimmed_content = trimmed_content[:match.start()] + trimmed_content[match.end():]


valid_muls_2 = [(int(m[0]), int(m[1])) for m in re.findall(regex_string, trimmed_content)]

print(f"Part 2: {sum([m[0] * m[1] for m in valid_muls_2])}")
