n = int(input())

for k in range(n):
    a = []
    p = input()
    for i in p:
        if i == '(':
            a.append(i)
        elif i == ')':
            if a:
                a.pop()
            else:
                print("NO")
                break
    else:
        if not a:
            print("YES")
        else:
            print("NO")



