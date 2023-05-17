from itertools import *

T = int(input())

for i in range(T):
    tc = input()
    ac = int(tc)
    tc = list(tc)
    ans = []
    res = 1
    check = False
    tc_list = list(permutations(tc, len(tc)))
    for j in range(len(tc_list)):
        at = ''
        for k in range(len(tc_list[j])):
            at += tc_list[j][k]
        at = int(at)
        ans.append(at)
    for j in range(len(tc_list)):
        if ans[j] != ac:
            if ans[j] % ac == 0:
                check = True
                break

    if check == True:
        print("#{}".format(i + 1), "possible")
    else:
        print("#{}".format(i + 1), "impossible")






