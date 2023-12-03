import re
import time

def get_sides(lines, start, end):
    bot = lines[0][start - 1 : end + 1]
    left = lines[1][start - 1]
    right = lines[1][end]
    top = lines[2][start - 1 : end + 1]
    return bot, left, right, top

def check_numbers(indexes: tuple(int, int), numbers: list[tuple[int, int]], line_number: int):
    for start, end in numbers:
        if indexes[0] in list(range(start, end + 1)) or indexes[1] in list(range(start, end + 1)):
            return int(lines[line_number][start:end])
    return 1

with open("days/day3/day3.txt") as file:
    all_lines = [line.rstrip() for line in file]


dummy_line = "." * len(all_lines[0])
all_lines = [dummy_line] + all_lines + [dummy_line]
all_lines = [f".{l}." for l in all_lines]


# PART 1
time_start = time.perf_counter()
answer = 0
for i in range(1, len(all_lines)):
    lines = all_lines[i - 1 : i + 2]
    number_indexes = [(m.start(0), m.end(0)) for m in re.finditer(r"\d+", lines[1])]
    for start, end in number_indexes:
        all_sides = "".join(get_sides(lines, start, end))
        part_number = all_sides != len(all_sides) * "."
        if part_number:
            answer += int(lines[1][start:end])
print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")  # Solved in 0.03631 Sec.
print(answer)

# PART 2
time_start = time.perf_counter()
answer = 0
for i in range(1, len(all_lines) - 1):
    lines = all_lines[i - 1 : i + 2]
    top_numbers = [(m.start(0), m.end(0)) for m in re.finditer(r"\d+", lines[0])]
    mid_numbers = [(m.start(0), m.end(0)) for m in re.finditer(r"\d+", lines[1])]
    bot_numbers = [(m.start(0), m.end(0)) for m in re.finditer(r"\d+", lines[2])]
    gear_indexes = [(m.start(0), m.end(0)) for m in re.finditer(r"\*", lines[1])]
    for start, end in gear_indexes:
        all_sides = get_sides(lines, start, end)
        gear = sum([any(s.isdigit() for s in side) for side in all_sides]) == 2
        if gear:
            # worst thing I've ever written, it's 1 AM though
            top = check_numbers(indexes=(start, end), numbers=top_numbers, line_number=0)
            mid = check_numbers(indexes=(start, end), numbers=mid_numbers, line_number=1)
            bot = check_numbers(indexes=(start, end), numbers=bot_numbers, line_number=2)
            print(top, mid, bot)
            answer += top * mid * bot
print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")
print(answer)