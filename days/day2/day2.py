import math

with open("days/day2/data.txt") as file:
    games = [line.rstrip() for line in file]

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

# PART 1
answer = 0
for game in games:
    possible = True
    sets = game.split(": ")[1].split("; ")
    # avoiding re.finditer to make it more fun
    for colour in LIMITS.keys():
        for game_set in sets:
            i = game_set.find(colour)
            if i != -1:
                # thank god there aren't 3 digit numbers (i.e. >= 100)
                cube_count = game_set[: i - 1][-2:]
                if int(cube_count) > LIMITS[colour]:
                    possible = False
                    break
        if not possible:
            break
    if possible:
        answer += int(game.split(": ")[0].split(" ")[1])
print(answer)

# PART 2
answer = 0
for game in games:
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    sets = game.split(": ")[1].split("; ")
    # avoiding re.finditer to make it more fun
    for colour in max_cubes.keys():
        for game_set in sets:
            i = game_set.find(colour)
            if i != -1:
                cube_count = int(game_set[: i - 1][-2:])
                if cube_count > max_cubes[colour]:
                    max_cubes[colour] = cube_count
    answer += math.prod(max_cubes.values())
print(answer)
