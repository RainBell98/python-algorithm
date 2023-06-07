def a(cnt):
    if cnt <= 1:
        win = 6
    elif cnt == 2:
        win = 5
    elif cnt == 3:
        win = 4
    elif cnt == 4:
        win = 3
    elif cnt == 5:
        win = 2
    elif cnt == 6:
        win = 1
    return win

def solution(lottos,win_nums):
    answer = []
    cnt = 0
    for num in lottos:
        if num in win_nums:
            cnt +=1
    chance = lottos.count(0) + cnt
    answer.append(a(chance))
    answer.append(a(cnt))
    return answer
print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))
