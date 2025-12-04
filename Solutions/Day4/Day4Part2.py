# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2025/day/4#part2

def solve(fileName: str):
    paperRollDiagram = open(fileName,"r").read().strip().split("\n")
    adjacentCount = [[0] * len(paperRollDiagram[0]) for i in range(len(paperRollDiagram))]
    accessibleRolls = 0

    # Create initial count
    for r,row in enumerate(paperRollDiagram):
        for c,element in enumerate(row):
            # Add count to neighboring tiles
            if element == "@":
                changeAdjacentCounts(adjacentCount,r,c,1)
            # If not a paper roll, impossible to be accessible
            else:
                adjacentCount[r][c] += 4

    # Count accessible rolls
    newRoll = True      # If we've removed a new roll on this pass
    while newRoll:
        newRoll = False
        for r,row in enumerate(adjacentCount):
            for c,count in enumerate(row):
                if count < 4:
                    accessibleRolls += 1
                    changeCount(adjacentCount,r,c,4)
                    changeAdjacentCounts(adjacentCount,r,c,-1)
                    newRoll = True

    return accessibleRolls

def changeAdjacentCounts(countList,r,c,delta):
    changeCount(countList,r-1,c-1,delta)
    changeCount(countList,r-1,c,delta)
    changeCount(countList,r-1,c+1,delta)
    changeCount(countList,r,c-1,delta)
    changeCount(countList,r,c+1,delta)
    changeCount(countList,r+1,c-1,delta)
    changeCount(countList,r+1,c,delta)
    changeCount(countList,r+1,c+1,delta)


def changeCount(countList,r,c,delta):
    # Avoid wrapping to end of list
    if r < 0 or c < 0:
        return

    try:
        countList[r][c] += delta
    except IndexError:
        pass

#print(solve("Solutions/Day4/unitTest.txt"))
print(solve("Solutions/Day4/input.txt"))