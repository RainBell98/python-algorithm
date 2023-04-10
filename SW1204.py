from collections import Counter
def Max(w):
    counter = Counter(w)
    max_counter = -1
    for letter in counter:
        if counter[letter]>max_counter:
            max_counter = counter[letter]
            max_letter = letter
    return max_letter
N = int(input())
for i in range(N):
    tc = int(input())
    score = list(map(int,input().split()))
    res = Max(score)
    print("#{}".format(i+1),res)


