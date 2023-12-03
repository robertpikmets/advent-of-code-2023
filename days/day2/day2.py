import math
import time

with open("days/day2/data.txt") as file:
    games = [line.rstrip() for line in file]

LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

time_start = time.perf_counter()

# PART 1
answer = 0
for i, game in enumerate(games):
    possible = True
    sets = game.split(": ")[1].split("; ")
    # avoiding regex to keep the fun
    for game_set in sets:
        for draw in game_set.split(", "):
            n, colour = draw.split()
            if int(n) > LIMITS[colour]:
                possible = False
                break
        if not possible:
            break
    if possible:
        answer += i + 1
print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")  # Solved in 0.01122 Sec.
print(answer)

# PART 2
time_start = time.perf_counter()
answer = 0
for game in games:
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    sets = game.split(": ")[1].split("; ")
    # avoiding regex to keep the fun
    for colour in max_cubes.keys():
        for game_set in sets:
            for draw in game_set.split(", "):
                n, colour = draw.split()
                if int(n) > max_cubes[colour]:
                    max_cubes[colour] = int(n)
    answer += math.prod(max_cubes.values())
print(f"Solved in {time.perf_counter()-time_start:.5f} Sec.")  # Solved in 0.05261 Sec.
print(answer)
