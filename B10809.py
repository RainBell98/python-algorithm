n = input()
p = list(n)

for i in range(97,123):
    if chr(i) in p:
        print(p.index(chr(i)),end=" ")
    else:
        print("-1",end=" ")



