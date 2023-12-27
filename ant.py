def solution(hp):
    result = 0
    a1 = hp%5
    result += hp//5
    a2 = a1%3
    result += a1//3
    a3 = a2%1
    result += a2//1
    return result
print(solution(23))