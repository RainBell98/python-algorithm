T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    char = 'Alice'
    if n % 2 == 0:
        print("#{}".format(test_case),char)
    else:
        char = 'Bob'
        print("#{}".format(test_case),char)
