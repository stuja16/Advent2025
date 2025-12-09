# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2025/day/7#part2

from functools import cache

grid = [""]     # Lists are unhashable -> use glob var instead of parameter passing

def solve(fileName: str) -> int:
    global grid
    startRow, *grid = open(fileName,"r").read().strip().split("\n")

    startRow.find("S")

    return simBeam(-1, startRow.find("S"))

@cache
def simBeam(y, x) -> int:
    global grid
    while(grid[y][x] == "."):
        y += 1
        if y >= len(grid):
            return 1

    return simBeam(y,x-1) + simBeam(y,x+1)

# print(solve("Solutions/Day7/unitTest.txt"))
print(solve("Solutions/Day7/input.txt"))