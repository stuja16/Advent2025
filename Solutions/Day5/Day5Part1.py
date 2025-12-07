# https://adventofcode.com/2025/day/5

import re

def solve(fileName: str) -> int:
    freshIngredients, ingredients = open(fileName,"r").read().strip().split("\n\n")
    freshIngredients = [int(i) for i in re.findall("\d+",freshIngredients)]
    ingredients = [int(i) for i in ingredients.split("\n")]
    freshTotal = 0

    for ingredient in ingredients:
        for startIndex in range(len(freshIngredients)//2):
            startIndex *= 2
            if freshIngredients[startIndex] <= ingredient and ingredient <= freshIngredients[startIndex+1]:
                freshTotal += 1
                break

    return freshTotal

#print(solve("Solutions/Day5/unitTest.txt"))
print(solve("Solutions/Day5/input.txt"))