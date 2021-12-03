from collections import defaultdict
import operator

def solution(numbers):

    answer = ''

    string_nums = [str(x) for x in numbers]

    num_dict = defaultdict(list)

    for number in string_nums:
        num_dict[number[0]].append(number)

    for k,v in num_dict.items():
        num_dict[k] = sorted(v,key=lambda x : len(x))
    print(num_dict)
    num_tuple_ordered = sorted(num_dict.items(),key=operator.itemgetter(0),reverse=True)

    for num_tuple in num_tuple_ordered:
        temp = []
        if len(num_tuple[1]) == 1:
            answer += str(num_tuple[1][0])
        else:
            sum_dict = {}
            for i,v in enumerate(num_tuple[1]):



    return answer


numbers = [23, 232, 21, 212]

print(solution(numbers))
