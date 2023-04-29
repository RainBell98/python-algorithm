T = int(input())
for i in range(T):
    tc = int(input())
    print("#{}".format(i+1),end=" ")
    for j in range(tc):
        print('1/{}'.format(tc),end=" ")
    print()