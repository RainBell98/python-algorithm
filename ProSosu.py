def convert(n, k):  # n을 k진수로 반환
    ret = ""
    while n > 0:
        ret += str(n % k)
        n = n //  k
    return ''.join(reversed(ret))
def prime(x):
    if x<2:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def solution(n,k):
    base = convert(n,k)
    base = base.split("0")
    result = 0
    for i in base:
        if len(i) == 0 :
            continue
        if prime(int(i)):
            result +=1

    return result
print(solution(437674,3))
