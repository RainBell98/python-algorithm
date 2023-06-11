def solution(brown,yellow):
    total = brown+yellow
    answer = []
    for y in range(1,total+1):
        if (total/y)%1 == 0:
            x = total//y
            if x>=y:
                if 2*x + 2*y == brown+4:
                    answer.append(x)
                    answer.append(y)
    return answer
