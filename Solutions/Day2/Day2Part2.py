# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2025/day/2#part2

def solve(fileName: str):
    ids = [list(map(lambda x: int(x),r.split("-"))) for r in open(fileName,"r").read().strip().replace("\n","").split(",")]
    total = 0

    for start, end in ids:
        for i in range(start, end+1):
            if isRepeated(i):
                total += i

    return total

def isRepeated(n: int):
    num = str(n)

    # Check all possible sub-string lengths
    for i in range(1, len(num)//2 + 1):
        if num.replace(num[:i], "") == "":
            return True

    return False

#print(solve("Solutions/Day2/unitTest.txt"))
print(solve("Solutions/Day2/input.txt"))