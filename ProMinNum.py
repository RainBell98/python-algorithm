def solution(A,B):
    res = []
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        res.append(A[i]*B[i])
    return sum(res)