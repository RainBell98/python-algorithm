def devide(i):
    cnt = 0
    while i % 5 != 0 and i>=0:
        i -= 3
        cnt += 1
    if i % 5 == 0:
        cnt = cnt + i//5
    else:
        cnt = -1
    return cnt
N = int(input())
print(devide(N))