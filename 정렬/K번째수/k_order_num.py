def solution(array, commands):

    # 답으로 제출할 array
    answer = []

    # command에 있는 요소를 돌면서
    for command in commands:

        # 시작 점 저장
        start = command[0]

        # 끝 점 저장
        end = command[1]

        # 정렬 후 N번째 위치 저장
        order = command[2]

        # command에 맞게 배열 슬라이싱
        temp_array = array[start-1:end]

        # 슬라이싱한 배열 정렬
        sorted_temp_array = sorted(temp_array)

        # N번째의 값을 append
        answer.append(sorted_temp_array[order-1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
