# advent of code 2021 day2
with open("./data/input-day1.txt") as f:
    depths = []
    for line in f:
        depths.append(line.strip("\n"))
# Part 1
hori = 0
dep = 0
for i in depths:
    move, index = i.split()
    if move == "forward":
        hori += int(index)
    elif move == "up":
        dep -= int(index)
    elif move == "down":
        dep += int(index)
print(hori, dep)
print(hori*dep)

# Part 2
aim = 0
hori = 0
dep = 0
for i in depths:
    move, value = i.split()
    if move == "forward":
        hori += int(value)
        dep += aim*int(value)
    elif move == "up":
        aim -= int(value)
    elif move == "down":
        aim += int(value)
print(dep, hori, hori*dep)
