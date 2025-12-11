# https://adventofcode.com/2025/day/7

from collections import deque

def solve(fileName: str) -> int:
    startRow, *grid = open(fileName,"r").read().strip().split("\n")
    gridHeight = len(grid)
    splitters = set()

    q = deque()
    q.append((-1,startRow.find("S")))
    while q:
        sy,sx = q.popleft()

        while True:
            sy += 1
            if sy >= gridHeight:
                break

            if grid[sy][sx] == ".":
                continue

            # If not blank tile, must be a splitter
            if (sy,sx) not in splitters:
                splitters.add((sy,sx))
                q.append((sy,sx-1))
                q.append((sy,sx+1))

            break

    return len(splitters)

# print(solve("Solutions/Day7/unitTest.txt"))
print(solve("Solutions/Day7/input.txt"))