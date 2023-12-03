import re
import time

with open("days/day3/day3.txt") as file:
    all_lines = [line.rstrip() for line in file]

time_start = time.perf_counter()

dummy_line = "." * len(all_lines[0])
all_lines = [dummy_line] + all_lines + [dummy_line]
all_lines = [f".{l}." for l in all_lines]

answer = 0
for i in range(1, len(all_lines)):
    lines = all_lines[i - 1 : i + 2]
    number_indexes = [(m.start(0), m.end(0)) for m in re.finditer(r"\d+", lines[1])]
    for start, end in number_indexes:
        bot = lines[0][start - 1 : end + 1]
        left = lines[1][start - 1]
        right = lines[1][end]
        top = lines[2][start - 1 : end + 1]
        all_sides = bot + left + right + top
        part_number = all_sides != len(all_sides) * "."
        if part_number:
            answer += int(lines[1][start:end])
print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")  # Solved in 0.03631 Sec.
print(answer)
