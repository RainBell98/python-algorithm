import sys
sys.setrecursionlimit(10**5)
# def fibo(n):
#     if n == 2:
#         return 1
#     elif n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         return fibo(n - 1) + fibo(n - 2)
def solution(n):
    answer = 1
    arr = [0,1,1]
    for i in range(2,n):
         arr.append(arr[-1]+arr[-2])
    return arr[-1]%1234567
print(solution(3))
