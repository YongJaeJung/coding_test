def solution(n, lost, reserve):
    answer = 0

    inter = set(lost).intersection(reserve)

    for val in inter:
        lost.remove(val)
        reserve.remove(val)

    s_lost = lost.copy()
    s_reserve = reserve.copy()

    for student in sorted(lost):

        left = student - 1
        right = student + 1

        if s_reserve.count(left) > 0:
            s_reserve.remove(left)
            s_lost.remove(student)

        elif s_reserve.count(right) > 0:
            s_reserve.remove(right)
            s_lost.remove(student)
        else:
            continue

    answer = n-len(s_lost)
        
    return answer


n = 5
lost = [4,2]
reserve = [3,1] 

print(solution(n, lost, reserve))