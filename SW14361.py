from itertools import*
T = int(input())

for i in range(T):
    tc = list(map(int,input()))
    res = 1
    check = False
    for j in range(1,len(tc)+1):
        res *= j
    tc_list = list(permutations(tc,len(tc)))

    for j in range(res):
        if tc_list[j] != tc:
            if tc_list[j]%tc == 0:
                check = True
                break
    

    if check == True:
        print("#{}".format(i+1),"possible")
    else:
        print("#{}".format(i+1),"impossible")





