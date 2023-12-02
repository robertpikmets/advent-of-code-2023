import re

with open("days/day1/data.txt") as file:
    input = [line.rstrip() for line in file]

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

# PART 1
# without regex and maybe not so efficient, but it works just fine
part1_answer = 0
for line in input:
    first_digit, second_digit = None, None
    for i, j in zip(line, line[::-1]):
        if i.isdigit() and not first_digit:
            first_digit = i
        if j.isdigit() and not second_digit:
            second_digit = j
        if first_digit and second_digit:
            break
    part1_answer += int(first_digit + second_digit)

# PART 2
part2_answer = 0
for line in input:
    first_digit = re.findall(r"(?=(" + "|".join(digits.keys()) + r"|\d))", line)[0]
    rev_digits = [d[::-1] for d in digits.keys()]
    last_digit = re.findall(r"(?=(" + "|".join(rev_digits) + r"|\d))", line[::-1])[0][::-1]
    try:
        first_digit = digits[first_digit]
    except KeyError:
        pass
    try:
        last_digit = digits[last_digit]
    except KeyError:
        pass
    part2_answer += int(first_digit + last_digit)
print("hello")