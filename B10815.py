n = int(input())
p = list(input().split())
m = int(input())
x = list(input().split())

for i in x:
    if i in p:
        print(1,end=' ')
    else:
        print(0,end=' ')
