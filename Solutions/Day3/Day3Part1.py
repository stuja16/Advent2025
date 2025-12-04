# https://adventofcode.com/2025/day/3

def solve(fileName: str):
    banks = [list(map(lambda x: int(x),r)) for r in open(fileName,"r").read().strip().split("\n")]
    sum = 0

    for b in banks:
        maxDigit = max(b)
        maxIndex = b.index(maxDigit)

        if maxIndex == len(b) - 1:
            sum += int(str(max(b[:-1]))+str(maxDigit))
        else:
            sum += int(str(maxDigit) + str(max(b[maxIndex+1:])))

    return sum

#print(solve("Solutions/Day3/unitTest.txt"))
print(solve("Solutions/Day3/input.txt"))