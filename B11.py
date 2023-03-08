import sys

input = sys.stdin.readline
a, c = map(int, input().split())
b = []


def k(x, y):
    if y == 0:
        for i in b:
            print(i, end=' ')
        print()


    else:

        for i in range(1, x + 1):
            if i in b:
                pass
            else:
                b.append(i)
                k(x, y - 1)
                b.pop()


k(a, c)