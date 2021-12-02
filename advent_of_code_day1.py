# advent of code 2021 day1
with open("./data/input-day1.txt") as f:
    depths = []
    for line in f:
        depths.append(int(line))

# Part 1
res = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        res += 1
print("Part1's answer is", res)


# Part 2
# initiate varaibles
fir = sum([depths[0], depths[1], depths[2]])
res = 0
for start in range(1, len(depths)-2): # can go to the later 2 indexes
    sec = fir - depths[start-1] + depths[start+2]
    if sec > fir:
        res +=1
    fir = sec
print("Part 2's answer is", res)