import sys
N = int(sys.stdin.readline())
S = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [0 for _ in range(N)]
res = 1e9
def sol(idx, mem):
    global res, N, S
    if mem == N//2:
        start = 0
        link = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += S[i][j]
                elif not visited[i] and not visited[j]:
                    link += S[i][j]
        res = min(res, abs(start - link))
    for i in range(idx, N):
        if visited[i]:
            continue
        visited[i] = 1
        sol(i+1, mem+1)
        visited[i] = 0
sol(0,0)
print(res)



