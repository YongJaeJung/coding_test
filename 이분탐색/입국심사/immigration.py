def solution(n, times):
    
    answer = 0
    
    # 걸리는 시간 정렬
    sorted_times = sorted(times)
    
    # 가장 적게 걸릴 시간은 대기자가 한 명이고 가장 처리가 빠른 사람이 처리 할때!
    min_time = sorted_times[0]
    
    # 가장 오래 걸릴 시간은 가장 처리 시간이 긴 사람이 전부 처리 할때!
    max_time = n*sorted_times[-1]


    # 이분 탐색의 조건 이 두 변수를 고쳐가면서 진행
    while min_time <= max_time:
        
        # 중간 지점을 계산
        mid = int((min_time+max_time)/2)
        
        # 최대로 처리 할 수 있는 고객의 수를 구하기
        customer = 0
        
        
        for time in times:
            customer += mid // time
            if customer >= n:
                break
        if customer >= n:
            answer = mid
            max_time = mid-1
        else:
            min_time = mid+1

    return answer



n = 6
times = [7,10]

print(solution(n,times))
