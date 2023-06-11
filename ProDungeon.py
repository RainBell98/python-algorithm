from itertools import permutations
def solution(k,dungeons):
    answer = 0
    cnt_list = []
    for p in permutations(dungeons,len(dungeons)):
        piro = k
        cnt = 0
        for a,b in p:
            if piro>=a:
                piro-=b
                cnt+=1
        cnt_list.append(cnt)
    return max(cnt_list)