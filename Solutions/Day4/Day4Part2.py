# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2025/day/4#part2

def solve(fileName: str):
    paperRollDiagram = open(fileName,"r").read().strip().split("\n")
    adjacentCount = [[0] * len(paperRollDiagram[0]) for _ in range(len(paperRollDiagram))]
    accessibleRolls = 0

    # Create initial count of adjacent rolls
    for r,row in enumerate(paperRollDiagram):
        for c,element in enumerate(row):
            if element == "@":      # +1 to neighboring tiles' count
                changeAdjacentCounts(adjacentCount,r,c,1)
            else:                   # If not a paper roll, impossible to be accessible
                adjacentCount[r][c] += 4

    # Count accessible rolls
    newRoll = True      # Have we removed a new roll on this pass?
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
    if r < 0 or c < 0:  # Avoid wrapping to end of list
        return

    try:
        countList[r][c] += delta
    except IndexError:
        return

#print(solve("Solutions/Day4/unitTest.txt"))
print(solve("Solutions/Day4/input.txt"))