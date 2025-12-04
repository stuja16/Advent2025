# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2025/day/3#part2

def solve(fileName: str, joltageLength: int):
    banks = [list(map(lambda x: int(x),r)) for r in open(fileName,"r").read().strip().split("\n")]
    totalJoltage = 0

    for b in banks:
        totalJoltage += int(findJoltage(b,joltageLength))

    return totalJoltage

# Recursive function
# Use strs>ints so can easily append digits
def findJoltage(bank, remainingJoltLength):
    if remainingJoltLength <= 0:
        return ""

    maxDigit = max(bank)
    maxDigitIndex = bank.index(maxDigit)
    distFromEnd = len(bank) - maxDigitIndex

    # If highest digit is near the end, put everything to the right of it to the joltage
    if remainingJoltLength >= distFromEnd:
        joltage = ""
        for i in range(maxDigitIndex,len(bank)):
            joltage += str(bank[i])

        return findJoltage(bank[:maxDigitIndex], remainingJoltLength-distFromEnd) + joltage

    # Else if highest digit is near the beginning, put it on the left
    return str(maxDigit) + findJoltage(bank[maxDigitIndex+1:], remainingJoltLength-1)

#print(solve("Solutions/Day3/unitTest.txt", 12))
print(solve("Solutions/Day3/input.txt", 12))