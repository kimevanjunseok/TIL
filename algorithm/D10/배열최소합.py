import sys
sys.stdin = open('배열최소합_input.txt')

# T = int(input())

# def make_candidates(a, k, input, c):
#     in_perm = [False] * NMAX

#     for i in range(1, k):
#         in_perm[a[i]] = True
    
#     ncands = 0
#     for i in range(1, input+1):
#         if in_perm[i] == False:
#             c[ncands] = i
#             ncands += 1
    
#     return ncands

# def backtrack(a, k, input):

#     global MAXCANDIDATES, result, min_sum
#     c = [0] * MAXCANDIDATES

#     if sum(min_sum) > result:
#         min_sum.pop()
#         return

#     if k == input:
#         if sum(min_sum) <= result:
#             result = sum(min_sum)
#     else:
#         k += 1
#         ncands = make_candidates(a, k, input, c)
#         for i in range(ncands):
#             a[k] = c[i]
#             min_sum.append(arr[k-1][data[a[k]]-1])
#             backtrack(a, k, input)

#     if not min_sum:
#         return
#     min_sum.pop()
        

# for i in range(1, T+1):

#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = []
#     min_sum = []
#     result = 100

#     MAXCANDIDATES = N+1
#     NMAX = N+1
#     data = list(range(N+1))
#     a = [0] * NMAX
#     backtrack(a, 0, N)

#     print(f'#{i} {result}')

##############################################################################

# 혜리누나 코드

def permute(k, n, total):
    global mint
    if total >= mint:
        return
    if k==n:
        mint = min(mint, total)
        return
    else:
        for i in range(n):
            if not v[i]:
                v[i] = True
                permute(k+1, n, total + numbers[k][i])
                v[i] = False

for tc in range(int(input())):
    n = int(input())
    numbers=[list(map(int, input().split())) for i in range(n)]
    mint = 500
    for i in range(n):
        v = [False]*n
        v[i] = True
        permute(1, n, numbers[0][i])
    print(f'#{tc+1}',mint)
