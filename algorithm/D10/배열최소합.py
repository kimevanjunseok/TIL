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

T = int(input())

def finder(L, cnt):
    global visited, min_sum, result, arr
    print(visited)
    for idx, i in enumerate(L):
        if idx not in visited:
            visited.append(idx)
            min_sum.append(i)
            
            if cnt == N-1:
                if result > sum(min_sum):
                    result = sum(min_sum)
                    visited.pop()
                    min_sum.pop()
                    cnt += -1
                else:
                    visited.pop()
                    min_sum.pop()
                    cnt += -1

            elif sum(min_sum) > result:
                visited.pop()
                min_sum.pop()
                cnt += -1
                break
                   
            else:
                finder(arr[cnt+1], cnt+1)

    if not min_sum:
        return
    cnt += -1
    min_sum.pop()
    visited.pop()

    

for n in range(1, T+1):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    min_sum = []
    cnt = 0
    result = 90
    finder(arr[cnt], cnt)
    print(f'#{n} {result}')
