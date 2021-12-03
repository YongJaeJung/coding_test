from collections import defaultdict

def solution(genres, plays):

    # 정답을 저장할 list
    answer = []

    # 장르 play 횟수를 더해줄 딕셔너리
    genres_ddict = defaultdict(int)

    # 특정 장르내의 id와 play횟수를 모아줄 딕셔너리
    genres_id_play = defaultdict(list)

    # 장르별 play 횟수 집계
    for g,p in zip(genres,plays):
        genres_ddict[g] += p

    # {장르:[(id,play)]} 형식의 딕셔너리
    for i,gp in enumerate(zip(genres,plays)):
        genres_id_play[gp[0]].append((i,gp[1]))

    # 장르 play횟수가 많은 순으로 정렬
    genres_ordered = sorted(genres_ddict.items(),key=lambda x : x[1],reverse=True)

    # 장르내에서 play횟수가 많은 id 순으로 정렬
    for k,v in genres_id_play.items():
        genres_id_play[k] = sorted(v,key=lambda x : x[1],reverse=True)

    print(genres_ordered)

    # 만든 해시를 이용해서 정답을 구함
    for a,b in genres_ordered:

        if len(genres_id_play[a]) == 1:
            answer.append(genres_id_play[a][0][0])
        else:
            for i in range(2):
                answer.append(genres_id_play[a][i][0])

    return answer




genres = ["classic"]
plays = [500]

print(solution(genres, plays))
