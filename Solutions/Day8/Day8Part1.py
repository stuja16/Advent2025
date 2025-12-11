# https://adventofcode.com/2025/day/8

import re
import heapq    # Need priority queue to store all distances
import math

def solve(fileName: str, connectionsLimit: int) -> int:
    input = [int(c) for c in re.findall("\d+", open(fileName,"r").read().strip())]
    coordinates = []
    for i in range(len(input)//3):
        coordinates.append((input[i*3], input[i*3+1], input[i*3+2])) # Create tuples surrounding each set of 3 coordinates

    distancePQ = []
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            distance = math.sqrt(pow(coordinates[j][0]-coordinates[i][0],2)+pow(coordinates[j][1]-coordinates[i][1],2)+pow(coordinates[j][2]-coordinates[i][2],2))
            heapq.heappush(distancePQ, (distance, i, j))

    circuits = []
    for _ in range(connectionsLimit):
        _,boxA,boxB = heapq.heappop(distancePQ)

        matchFound = False
        for cir in circuits:
            if boxA in cir or boxB in cir:
                matchFound = True
                cir.add(boxA)
                cir.add(boxB)
                break

        if matchFound: continue

        newCircuit = set()
        newCircuit.add(boxA)
        newCircuit.add(boxB)
        circuits.append(newCircuit)

    # Check for overlapping circuits
    overlapFound = True
    while overlapFound: # Need to keep checking bc sets are actively being changed
        overlapFound = False

        for i in range(len(circuits)):
            for j in range(i+1,len(circuits)):
                if circuits[i] & circuits[j]:
                    overlapFound = True
                    circuits[i].update(circuits[j])
                    circuits.pop(j)
                    break
            if overlapFound:
                break

    max1, max2, max3 = 0,0,0
    for c in circuits:
        max3 = max(max3,len(c))
        if len(c) > max1:
            max3 = max2
            max2 = max1
            max1 = len(c)
        elif len(c) > max2:
            max3 = max2
            max2 = len(c)

    return max1 * max2 * max3

# print(solve("Solutions/Day8/unitTest.txt",10))
print(solve("Solutions/Day8/input.txt",1000))