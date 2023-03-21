count = 1
temp = True
stack = []
a = []

N = int(input())
for i in range(N):
    num = int(input())

    while count <= num:
        stack.append(count)
        a.append('+')
        count += 1


    if stack[-1] == num:
        stack.pop()
        a.append('-')

    else:
        temp = False
        break


if temp == False:
    print("NO")
else:
    for i in a:
        print(i)