# https://adventofcode.com/2025/day/6

import re

def solve(fileName: str) -> int:
    *rawFactors, operations = open(fileName,"r").read().strip().split("\n")
    factors = []
    total = 0

    for row in rawFactors:
        factors.append([int(i) for i in re.findall("\d+", row)])
    operations = re.findall("[*+]", operations)

    for i in range(len(operations)):
        if operations[i] == "+":
            for n in factors:
                total += n[i]
        elif operations[i] == "*":
            product = 1
            for n in factors:
                product *= n[i]
            total += product

    return total

#print(solve("Solutions/Day6/unitTest.txt"))
print(solve("Solutions/Day6/input.txt"))