def solution(s,skip,index):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha = list(alpha)
    answer = ''
    ans = []
    for i in alpha:
        if i not in skip:
            ans.append(i) 
    for i in s:
        a =  ans[(ans.index(i) + index) % len(ans)]
        answer += a
    return answer
print(solution("aukks","wbqd",5))