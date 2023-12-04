import math
import re
import time


def get_sides(lines, start, end):
    bot = lines[0][start - 1 : end + 1]
    left = lines[1][start - 1]
    right = lines[1][end]
    top = lines[2][start - 1 : end + 1]
    return bot, left, right, top


def get_gear_numbers(
    lines: list[str], gear_index: int, numbers: list[tuple[int, int]], line_number: int
) -> tuple[int, int] | int:
    output = ()
    for start, end in numbers:
        if any(i in [gear_index - 1, gear_index + 1] for i in list(range(start, end))):
            output += (int(lines[line_number][start:end]),)
    if len(output) == 0:
        return (1,)
    else:
        return output


def prepare_file(input):
    dummy_line = "." * len(input[0])
    all_lines = [dummy_line] + input + [dummy_line]
    all_lines = [f".{line}." for line in all_lines]
    return all_lines


# PART 1
def part1(all_lines):
    answer = 0
    for i in range(1, len(all_lines)):
        lines = all_lines[i - 1 : i + 2]
        number_indexes = [(m.start(0), m.end(0)) for m in re.finditer(r"\d+", lines[1])]
        for start, end in number_indexes:
            all_sides = "".join(get_sides(lines, start, end))
            part_number = all_sides != len(all_sides) * "."
            if part_number:
                answer += int(lines[1][start:end])
    return answer


# PART 2
# I am not proud of it
def part2(all_lines):
    answer = 0
    for i in range(1, len(all_lines) - 1):
        lines = all_lines[i - 1 : i + 2]
        number_lines = [
            [(m.start(0), m.end(0)) for m in re.finditer(r"\d+", lines[i])] for i in range(0, 3)
        ]
        gear_indexes = [(m.start(0), m.end(0)) for m in re.finditer(r"\*", lines[1])]
        for start, end in gear_indexes:
            all_sides = get_sides(lines, start, end)
            gear = sum([sum(s.isdigit() for s in side.split(".")) for side in all_sides]) == 2
            if gear:
                all_numbers = ()
                for n, line in enumerate(number_lines):
                    gear_number = get_gear_numbers(
                        lines, gear_index=start, numbers=line, line_number=n
                    )
                    all_numbers += gear_number
                answer += math.prod(all_numbers)
    return answer


if __name__ == "__main__":
    with open("days/day3/data.txt") as file:
        input = [line.rstrip() for line in file]
        all_lines = prepare_file(input)

        time_start = time.perf_counter()
        print(part1(all_lines))
        print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")  # Solved in 0.00357 Sec.

        time_start = time.perf_counter()
        print(part2(all_lines))
        print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")  # Solved in 0.11905 Sec.
