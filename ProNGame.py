def convert(n, k):
    tmp = "0123456789ABCDEF"
    q,r = divmod(n,k)
    if q == 0:
        return tmp[r]
    else:
        return convert(q,k)+tmp[r]
def solution(n,t,m,p):
    res = ''
    answer = ''
    for i in range(m*t):
        res += str(convert(i,n))
    while len(answer)<t:
        answer += res[p-1]
        p+=m
    return answer