# https://adventofcode.com/2025/day/4

def solve(fileName: str):
    paperRollDiagram = open(fileName,"r").read().strip().split("\n")
    adjacentCount = [[0] * len(paperRollDiagram[0]) for i in range(len(paperRollDiagram))]
    accessibleRolls = 0

    for r,row in enumerate(paperRollDiagram):
        for c,element in enumerate(row):
            # Add count to neighboring tiles
            if element == "@":
                addCount(adjacentCount,r-1,c-1)
                addCount(adjacentCount,r-1,c)
                addCount(adjacentCount,r-1,c+1)
                addCount(adjacentCount,r,c-1)
                addCount(adjacentCount,r,c+1)
                addCount(adjacentCount,r+1,c-1)
                addCount(adjacentCount,r+1,c)
                addCount(adjacentCount,r+1,c+1)
            # If not a paper roll, impossible to be accessible
            else:
                adjacentCount[r][c] += 4

    # Count accessible rolls
    for r,row in enumerate(adjacentCount):
        for c,count in enumerate(row):
            if count < 4:
                accessibleRolls += 1

    return accessibleRolls

def addCount(countList,r,c):
    # Avoid wrapping to end of list
    if r < 0 or c < 0:
        return

    try:
        countList[r][c] += 1
    except IndexError:
        pass

#print(solve("Solutions/Day4/unitTest.txt"))
print(solve("Solutions/Day4/input.txt"))