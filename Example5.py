from itertools import combinations

height = [int(input()) for _ in range(9)]
for co in combinations(height,7):
    if sum(co) == 100:
        #print(sorted(co))
        for height in sorted(co):
            print(height)
        break


