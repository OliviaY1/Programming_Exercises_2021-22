# advent of code day 3
# author: olivia yan

# convert binary to decimal: int("101", 2)
# convert decimal to binary: bin(#)

with open("./data/input-day1.txt") as f:
    depths = []
    for line in f:
        depths.append(line.strip("\n"))

# PART 1
'''
collect = [[0,0]for i in range(len(depths[0]))] # the first index is num of 0, the second is num of 1
gamma_rate = 0
epsilon_rate = 0

for i in depths:
    for a in range(len(i)):
        if i[a] == '1':
            collect[a][1] += 1
        else:
            collect[a][0] += 1
for i in collect:
    # get gamma rate and epsilon rate
    if i[0] > i[1]: # more 0, less 1
        gamma_rate = gamma_rate*10 + 0
        epsilon_rate = epsilon_rate*10 + 1
    else:
        gamma_rate = gamma_rate*10 + 1
        epsilon_rate = epsilon_rate*10 +0
gamma_rate = int(str(gamma_rate), 2)
epsilon_rate = int(str(epsilon_rate), 2)
print(gamma_rate, epsilon_rate, epsilon_rate*gamma_rate)
'''

# PART 2
oxy = depths.copy()
# while loop
while len(oxy) > 1:
    for i in range(len(oxy[0])):
        num1 = 0
        num0 = 0
        for a in oxy:
            if a[i] == 0:
                num0 += 1
            else:
                num1 += 1


print(oxy)