# import time

with open("days/day2/data.txt") as file:
    games = [line.rstrip() for line in file]

limits = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

# t0 = time.time()
answer = 0
for game in games:
    possible = True
    sets = game.split(": ")[1].split("; ")
    # avoiding re.finditer to make it more fun
    for game_set in sets:
        for colour in limits.keys():
            i = game_set.find(colour)
            if i != -1:
                # thank god there aren't 3 digit numbers (i.e. >= 100)
                cube_count = game_set[: i - 1][-2:]
                if int(cube_count) > limits[colour]:
                    possible = False
                    break
        if not possible:
            break
    if possible:
        answer += int(game.split(": ")[0].split(" ")[1])
print(answer)
# t1 = time.time()
# total = t1 - t0
# print(total)
