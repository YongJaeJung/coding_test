def solution(phone_book):

    number_length = [len(x) for x in phone_book]

    min_len = min(number_length)
    max_len = max(number_length)

    answer = True
    return answer




phone_book = ["12","123","1235","567","88"]

print(solution(phone_book))
