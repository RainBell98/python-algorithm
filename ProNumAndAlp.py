def solution(s):
    answer = 0
    Num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    Alp = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    res = ''
    result = ''
    for i in s:
        if (i.isnumeric()):
            result += i
        else:
            res += i
            if res in Alp:
                result += str(Alp.index(res))
                res = ''
    return int(result)
for i in range(4):
    s = input()
    print(solution(s))