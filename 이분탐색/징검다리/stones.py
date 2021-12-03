from collections import defaultdict

def solution(distance, rocks, n):
    answer = 0

    sorted_rocks = [0]
    sorted_rocks.extend(sorted(rocks))
    sorted_rocks.append(distance)

    diffs = []

    for i in range(len(sorted_rocks)-1):
        diffs.append(sorted_rocks[i+1] - sorted_rocks[i])

    value_indexes = defaultdict(list)

    for i,v in enumerate(diffs):
        value_indexes[v].append(i)

    diff_unique = list(sorted(set(diffs)))

    left = 0

    right = len(diff_unique)

    print(value_indexes)

    while left <= right:
        mid = diff_unique[len(diff_unique)//2]

    return answer


distance = 25
rocks =	[2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n))
