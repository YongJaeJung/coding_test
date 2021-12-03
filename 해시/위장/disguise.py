def factorial(v):
    result = 1
    for i in range(1,v+1):
        result = result * i

    return result

def combination(n,k):
    return factorial(n) / (factorial(k) * factorial(n-k))


def solution(clothes):

    category = []

    for item in clothes:
        category.append(item[1])

    categories = set(category)

    dic = {}

    for category in categories:
        dic[category] = 0
        for item in clothes:
            if item[1] == category:
                dic[category] = dic[category] + 1
    answer = 1

    for key in dic:
        temp = 0
        for i in range(0,2):
            temp = temp + combination(dic[key],i)
        answer = answer * temp
    answer = answer - 1
    return answer
