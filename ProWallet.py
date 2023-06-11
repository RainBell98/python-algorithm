def solution(sizes):
    p = []
    MAX = 0
    for w,h in sizes:
        if MAX<=w:
            MAX = w
        if MAX<=h:
            MAX = h
    for w,h in sizes:
        if w>=h:
            p.append(h)
        else:
            p.append(w)
    return MAX*max(p)
print(solution(	[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))