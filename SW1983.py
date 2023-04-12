N = int(input())

for i in range(1,N+1):

    std,num = map(int,input().split())
    p = [0 for k in range(std)]
    rank = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    ans = 0
    for j in range(std):
        score = list(map(int,input().split()))
        p[j] = score[0]*0.35+score[1]*0.45+score[2]*0.2

    ans = p[num-1]
    p.sort(reverse=True)
    ans_score = p.index(ans)//(std//10)

    print(f'#{i} {rank[ans_score]}')
