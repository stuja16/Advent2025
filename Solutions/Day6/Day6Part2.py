# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2025/day/6#part2

import re

def solve(fileName: str) -> int:
    *rawFactors, operations = open(fileName,"r").read().strip().split("\n")
    factors = []
    total = 0

    maxRowLength = 0
    for row in rawFactors:
        maxRowLength = max(maxRowLength,len(row))

    factorRow = []
    for c in range(maxRowLength + 1):

        factorRow.append("")
        for row in rawFactors:
            try:
                factorRow[-1] += row[c]
            except IndexError:
                pass

        if factorRow[-1].strip() == "":   # Reset for next operation
            factorRow.pop()     # Remove empty column between operations
            factors.append(factorRow)
            factorRow = []

    operations = re.findall("[*+]", operations)

    for i in range(len(operations)):
        numbers = [int(n) for n in factors[i]]      # Convert strs to ints
        if operations[i] == "+":
            for num in numbers:
                total += num
        elif operations[i] == "*":
            product = 1
            for num in numbers:
                product *= num
            total += product

    return total

# print(solve("Solutions/Day6/unitTest.txt"))
print(solve("Solutions/Day6/input.txt"))