# https://adventofcode.com/2025/day/2

def solve(fileName: str):
    ids = [list(map(lambda x: int(x),r.split("-"))) for r in open(fileName,"r").read().strip().replace("\n","").split(",")]
    total = 0

    for start, end in ids:
        for i in range(start, end+1):
            num = str(i)
            if num[:len(num)//2] == num[len(num)//2:]:
                total += i

            i += 1

    return total

#print(solve("Solutions/Day2/unitTest.txt"))
print(solve("Solutions/Day2/input.txt"))