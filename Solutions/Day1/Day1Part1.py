# https://adventofcode.com/2025/day/1

def solve(fileName):
    turns = [(r[0],int(r[1:])) for r in open(fileName,"r").read().strip().split("\n")]
    pos = 50    # Starting position of dial
    count = 0

    for t in turns:
        # Turn dial
        if t[0] == "L":
            pos -= t[1]
        else:
            pos += t[1]
        pos = pos % 100

        if pos == 0:
            count += 1

    return count

#print(solve("Solutions/Day1/unitTest.txt"))
print(solve("Solutions/Day1/input.txt"))