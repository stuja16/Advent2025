# Must input a correct answer for part 1 before part 2 can be viewed
# https://adventofcode.com/2025/day/5#part2

import re
from collections import deque

def solve(fileName: str) -> int:
    freshIngredientRanges, _ = open(fileName,"r").read().strip().split("\n\n")
    freshIngredientRanges = [int(i) for i in re.findall("\d+",freshIngredientRanges)]

    dq = deque()
    dq.extend(freshIngredientRanges)
    freshTotal = 0

    # Regroup overlapping ranges
    cleanedRanges = [(dq.popleft(),dq.popleft())]
    while dq:
        start = dq.popleft()
        end = dq.popleft()
        overlap = False
        for s,e in cleanedRanges:
            if start <= s and s <= end and end <= e:
                cleanedRanges.remove((s,e))
                dq.append(start)
                dq.append(e)
                overlap = True
                break
            elif s <= start and start <= e and e <= end:
                cleanedRanges.remove((s,e))
                dq.append(s)
                dq.append(end)
                overlap = True
                break
            elif start <= s and e <= end:   # Existing range included in current range
                cleanedRanges.remove((s,e))
                dq.append(start)
                dq.append(end)
                overlap = True
                break
            elif s <= start and end <= e:   # Current range included in existing range
                overlap = True
                break
        # If there is no overlap
        if not overlap:
            cleanedRanges.append((start,end))

    # Count new list
    for iRange in cleanedRanges:
        freshTotal += iRange[1] - iRange[0] + 1

    return freshTotal

#print(solve("Solutions/Day5/unitTest.txt"))
print(solve("Solutions/Day5/input.txt"))