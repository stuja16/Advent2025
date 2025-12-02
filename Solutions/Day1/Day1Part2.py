# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2025/day/1#part2

def solve(fileName):
    turns = [(r[0],int(r[1:])) for r in open(fileName,"r").read().strip().split("\n")]
    pos = 50    # Starting position of dial
    count = 0

    for dir, spin in turns:
        # Edge case adjustment
        if dir == "L" and pos == 0:
            count -= 1

        # Turn dial
        if dir == "L":
            pos -= spin
        else:
            pos += spin

        # Count passes
        if pos <= 0:
            count += abs(int(pos/100)) + 1
        elif pos >= 100:
            count += abs(int(pos/100))

        # Reset for next turn
        pos = pos % 100

    return count

#print(solve("Solutions/Day1/unitTest.txt"))
print(solve("Solutions/Day1/input.txt"))