def chicken1(num,cnt):
    num = num//10
    cnt = num%10
    if num>=10:
        return chicken1(num,cnt)
    else:
        return num,cnt

def solution(chicken):
    return chicken1(chicken,0)
