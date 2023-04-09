N = int(input())

for i in range(N):
    test_case = int(input())
    nu = ""
    for j in range(test_case):
        alp,num = input().split()
        num = int(num)
        nu += alp*num

    print("#{}".format(i+1))
    for i in range(1, len(nu) + 1, 10):
        print(nu[i - 1:i + 10 - 1])

