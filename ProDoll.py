def solution(board,moves):
    p = []
    cnt = 0
    for k in moves:
        for i in range(len(board)):
            if board[i][k-1] != 0:
                p.append(board[i][k-1])
                board[i][k-1] = 0
                break
        if len(p)>=2:
            if p[-2] == p[-1]:
                p.pop()
                p.pop()
                cnt+=2

    return cnt







print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))