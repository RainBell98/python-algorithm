def solution(keymap,targets): 
    res = []
    for i in range(len(targets)):
        ans = 0
        for j in range(len(targets[i])):
            answer = []
            for k in range(len(keymap)):             
                if targets[i][j] in keymap[k]:
                    answer.append(keymap[k].index(targets[i][j]))
            if len(answer) != 0:
                ans += (min(answer)+1)
            else:
                ans = -1
                break
        res.append(ans)
    return res
print(solution(["ACC","CAC"], ["CD","C"]))
