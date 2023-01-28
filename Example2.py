N = int(input())

arr = []
for i in range(1,N+1):
    arr.append(i)
while len(arr)>1:
    arr.pop(0)
    arr.append(arr.pop(0))

print(arr.pop())