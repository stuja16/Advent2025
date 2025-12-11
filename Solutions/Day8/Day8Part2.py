# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2025/day/8#part2

import re
import heapq
import math

def solve(fileName: str) -> int:
    input = [int(c) for c in re.findall("\d+", open(fileName,"r").read().strip())]
    coordinates = []
    for i in range(len(input)//3):
        coordinates.append((input[i*3], input[i*3+1], input[i*3+2])) # Create tuples surrounding each set of 3 coordinates

    distancePQ = []
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            distance = math.sqrt(pow(coordinates[j][0]-coordinates[i][0],2)+pow(coordinates[j][1]-coordinates[i][1],2)+pow(coordinates[j][2]-coordinates[i][2],2))
            heapq.heappush(distancePQ, (distance, i, j))

    # Find spanning tree
    circuits = []
    while distancePQ:
        _,a,b = heapq.heappop(distancePQ)
        aCircuit, bCircuit = -1,-1                      # Indices of existing circuit containing given box

        for i in range(len(circuits)):                  # Find if a,b boxes are in existing circuits
            if a in circuits[i]:
                aCircuit = i
            if b in circuits[i]:
                bCircuit = i

        if aCircuit == -1 and bCircuit == -1:
            newCircuit = set()
            newCircuit.add(a)
            newCircuit.add(b)
            circuits.append(newCircuit)
        elif aCircuit == -1:
            circuits[bCircuit].add(a)
        elif bCircuit == -1:
            circuits[aCircuit].add(b)
        elif aCircuit == bCircuit:
            continue
        else:
            circuits[aCircuit] |= circuits[bCircuit]    # Merge sets
            circuits.pop(bCircuit)

        if len(circuits[0]) == len(coordinates):        # Check for spanning tree
            return coordinates[a][0] * coordinates[b][0]

    return -1   # Failed state: no spanning tree found

# print(solve("Solutions/Day8/unitTest.txt"))
print(solve("Solutions/Day8/input.txt"))