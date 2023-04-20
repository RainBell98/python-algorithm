from itertools import combinations
T = int(input())
for i in range(T):
    ls =[]
    ls1 = []
    a = list(map(int,input().split()))
    for j in combinations(a,3):
        ls.append(j)
    for j in range(len(ls)):
        ls1.append(sum(ls[j]))
    ls2 = set(ls1)
    ls3 = list(ls2)
    ls3.sort(reverse=True)


    print("#{}".format(i+1),ls3[4])