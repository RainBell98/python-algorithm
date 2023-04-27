for i in range(10):
    p1 = int(input())
    p2 = list(map(int,input().split()))
    p3 = int(input())
    p4 = list(map(str,input().split()))
    for j in range(0,len(p4)):
        if p4[j] == 'I':
            for k in range(int(p4[j+2])):
                p2.insert(p3,p4[k+4])
        elif p4[j] == 'D':
            for k in range(int(p4[j+1])+1,int(p4[j+1])+int(p4[j+2])+1):
                del p2[k]
        elif p4[j] == 'A':
            for k in range(int(p4[j+1])):
                p2.append(p4[j+2])
    print("#{}".format(i+1),end=" ")
    for k in range(10):
        print(p2[k],end=" ")
    print()

